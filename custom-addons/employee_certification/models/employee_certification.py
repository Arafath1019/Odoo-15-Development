from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class HREmployeeCertificate(models.Model):
    _name = 'employee.certificate'
    _inherits = {'res.company': 'company_id'}

    name = fields.Char(string='Certificate Name', size=100, required=True)
    # company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id.id)


class HRCertificateIssuedBy(models.Model):
    _name = 'certificate.issued.by'

    name = fields.Char(string='Issued By', size=100, required=1)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id.id)


class HREmployeeInherited(models.Model):
    _inherit = 'hr.employee'

    certification_ids = fields.One2many(comodel_name="employee.certification", inverse_name="employee_id",
                                        string="Certification")
    job_status = fields.Char(string='Job Status', help='Short not whats his/her job status currently')


class HREmployeeCertification(models.Model):
    _name = "employee.certification"
    _rec_name = 'certification_id'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=False)
    certification_id = fields.Many2one('employee.certificate', string="Certification", required=True, )
    institute = fields.Many2one('certificate.issued.by', string="Issued by", required=True, )
    start_date = fields.Date(string="Start date", required=True, )
    end_date = fields.Date(string="End date", required=True, )
    cert_duration = fields.Char(string="Certification duration", compute='calculate_certificate_duration')
    certificate_status = fields.Selection(string="Status",
                                          selection=[('completed', 'Completed'),
                                                     ('in_progress', 'In Progress'), ('certified', 'Certified'),
                                                     ], default='in_progress', required=True, )
    certificate_photo = fields.Many2many('ir.attachment', string="Upload")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id.id)
