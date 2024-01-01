from odoo import api, models, fields

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'
    
    patient_id = fields.Many2one(comodel_name="hospital.patient", string="Appointment")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    # gender = fields.Selection(related="patient_id.gender", readonly=False)
    gender = fields.Selection(related="patient_id.gender")
    ref = fields.Char(string="Reference")
    prescription = fields.Html(string="Prescription", placeholder="Enter your prescription")
    priority = fields.Selection([('0', 'Normal'), ('1', 'Low'), ('2', 'Hight'), ('3', 'Very Hight')], string="Priority")
    
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref