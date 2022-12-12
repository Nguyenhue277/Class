from odoo import models, fields

class EducationStudent(models.Model):
    _inherit = 'education.student'
    
    class_vip_id = fields.Many2one(
        comodel_name='education.class.vip',
        string='Class VIP'
        )
    