from odoo import api, models, fields, _
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'
    
    # patient_id = fields.Many2one(comodel_name="hospital.patient", string="Appointment", ondelete="restrict")
    patient_id = fields.Many2one(comodel_name="hospital.patient", string="Appointment", ondelete="cascade")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    # gender = fields.Selection(related="patient_id.gender", readonly=False)
    gender = fields.Selection(related="patient_id.gender")
    ref = fields.Char(string="Reference", help="Reference from patient record")
    prescription = fields.Html(string="Prescription", placeholder="Enter your prescription")
    priority = fields.Selection([('0', 'Normal'), ('1', 'Low'), ('2', 'Hight'), ('3', 'Very Hight')], string="Priority")
    state = fields.Selection([('draft', 'Draft'), ('in_consultation', 'In Consultation'), ('done', 'Done'), ('cancel', 'Cancel')], string="Status", default="draft")
    doctor_id = fields.Many2one('res.users', string="Doctor", tracking=True)
    pharmacy_line_ids = fields.One2many("appointment.pharmacy.lines", "appointment_id", string="Pharmacy Lines")
    hide_sales_price = fields.Boolean(string="Hide Sales Price")
    
    def unlink(self):
        for rec in self:
            if rec.state == 'done':
                raise ValidationError(_("You cannot delete appointment with 'Done' status!"))
        return super(HospitalAppointment, self).unlink()
    
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
        
    def action_test(self):
        print("Action button triggered")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click successful',
                'type': 'rainbow_man'
            }
        }

    def action_in_consultation(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = "in_consultation"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        # for rec in self:
        #     rec.state = "cancel"
        action = self.env.ref('om_hospital.action_cancel_appointmet').read()[0]
        return action
    
    def action_draft(self):
        for rec in self:
            rec.state = "draft"
            
class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'
    
    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related="product_id.list_price")
    qty = fields.Integer(string="Quantity", default=1)
    appointment_id = fields.Many2one(comodel_name="hospital.appointment", string="Appointment")