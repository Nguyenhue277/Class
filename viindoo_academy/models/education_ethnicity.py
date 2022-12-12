from odoo import models, fields
from pickle import TRUE

class Ethnicity(models.Model):
    _name='education.ethnicity'
    _description='Ethnicity'
    
    name=fields.Char(
        string='Name',
        required=True,
        )
    description=fields.Char(
        string="Description"
        )
    # code = fields.Char(
    #     string="Code",
    #     required=True,
    #     groups='base.group_user'
    #     )
    

    student_ids = fields.One2many(
        comodel_name='education.student',
        inverse_name='ethnicity_id',
        string='Students',
        )

    
    country_ids=fields.Many2many(
        comodel_name='res.country',
        relation='class_education_ethnicity_rel',
        string='Countries',
        column1='country_id',
        column2='ethnicity_id'
        )
    