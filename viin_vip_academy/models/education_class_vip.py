from odoo import models, fields

class EducationClassVIP(models.Model):
    _name = 'education.class.vip'
    _description = 'Education Class VIP'
    _inherit = 'education.class'
    
    currency_id = fields.Many2one(
        comodel_name = 'res.currency',
        string = 'Currency'
        )
    credit = fields.Monetary(
        string = 'Credit'
        )
    
    student_ids = fields.One2many(
        comodel_name='education.student',
        inverse_name='class_vip_id',
        string='Students',
        )
    
    historical_student_ids = fields.Many2many(
        comodel_name='education.student',
        relation='class_education_vip_rel',
        column1='student_id',
        column2='class_id',
        string='Historical Students'
        )
    