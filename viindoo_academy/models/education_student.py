from odoo import models, fields, api

class EducationStudent(models.Model):
    _name = "education.student"
    _description = "Education Student"
    
    name = fields.Char(
        string='Name',
        required=True,
        )
    
    age = fields.Integer(
        string="Age of Student"
        )
    
    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country'
        )
    
    ethnicity_id = fields.Many2one(
        comodel_name='education.ethnicity',
        string='Ethnicity'
        )
    # ethnicity_code = fields.Char(releted="ethnicity_id.code")
    
    class_id = fields.Many2one(
        comodel_name='education.class',
        string='Current Class'
        )
    
    class_ids = fields.Many2many(
        comodel_name='education.class',
        relation='class_education_rel',
        column1='class_id',
        column2='student_id',
        string='Enrolled Classes'
        )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User'
        )

    @api.onchange('ethnicity_id')
    def _onchange_ethnicity_id(self):
        self.country_id = self.ethnicity_id.country_ids[:1]
            
            
            
            