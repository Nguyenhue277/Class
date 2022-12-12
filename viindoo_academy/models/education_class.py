from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EducationClass(models.Model):
    _name = "education.class"
    _description = "Education Class"
    
    name = fields.Char(
        string="Class Name",
        help="The name odd the class for identification",
        required=True,
        )
    teacher_name = fields.Char(
        string="Teacher",
        )
    start_date = fields.Date(
        string="Start Date"
        )
    end_date = fields.Date(
        string="End Date"
        )
    
    note=fields.Char(
        string="Note"
        )
    
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed','Confirmed'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled')
            ],
        string='Status',
        default='draft',
        help="Status of the class"
        )
    
    description = fields.Text(
        string="Description"
        )
    
    active = fields.Boolean(default=True)
    
    student_ids = fields.One2many(
        comodel_name='education.student',
        inverse_name='class_id',
        string='Students',
        )
    
    historical_student_ids = fields.Many2many(
        comodel_name="education.student",
        relation='class_education_rel',
        column1='student_id',
        column2='class_id',
        string='Historical Students'
        )
    
    company_id=fields.Many2one(
        comodel_name='res.company', 
        string="Company",
        default=lambda self: self.env.company
        )
    
class EducationStudent(models.Model):
    _inherit = 'education.class'
    
    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country'
        )
    
    historical_student_ids = fields.Many2many(
        comodel_name="education.student",
        relation='class_education_extend_rel',
        column1='student_id',
        column2='class_id',
        string='Historical Students'
        )
    
    students_count = fields.Integer(
        string='Number of Student',
        compute='_compute_students_count'
        )
    
    historical_students_count = fields.Integer(
        string = 'Number of historical students',
        compute = '_compute_historical_students_count'
        )
    
    _sql_constraints = [
        (
            'class_name_unique',
            'unique(name)',
            "The name of class must be unique"
            )
        ]
    
    @api.depends('student_ids')
    def _compute_students_count(self):
        for r in self:
            r.students_count = len(r.student_ids)
    
    
    @api.depends('historical_student_ids')
    def _compute_historical_students_count(self):
        for r in self:
            r.historical_students_count = len(r.historical_student_ids)
            
    @api.constrains('start_date','end_date')
    def _check_date(self):
        if self.filtered(lambda self: self.start_date and self.end_date and self.end_date < self.start_date):
            raise ValidationError("The start date must be earlier than or equal to end date.")
        
    
    