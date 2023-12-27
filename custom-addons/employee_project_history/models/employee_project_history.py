from odoo import models, fields

class HREmployeeProjectHistory(models.Model):
    _name= "employee.project.history"
    _description = "Employee Project History"
    
    project_name = fields.Char(string="Project Name", required=True)
    role = fields.Char(string="Role", required=True)
    responsibility = fields.Char(string="Responsibility", required=True)
    assigned_from = fields.Date(string="Assigned From", required=True)
    assigned_to = fields.Date(string="Assigned To")
    notes = fields.Char(string="Notes")
    number_of_members = fields.Integer(string="Number of members", required=True)