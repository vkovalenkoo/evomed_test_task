from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class Employee(models.Model):
    _inherit = "hr.employee"
    _description = 'Employee Extends'

    # TODO: Create field Pension Fund Tax with type boolean 1.2
    is_pension_fund_tax = fields.Boolean(string='Pension Fund Tax')

    employee_position_ids = fields.One2many('hr.employee.position', 'employee_id', string='Positions')


class HrJob(models.Model):
    _inherit = 'hr.job'
    # TODO: Create field of recommended working hourse per week for specific job position 3.4.2
    working_hours = fields.Float(string='Working Hours (per week)', default=40)


class HrEmployeePosition(models.Model):
    _name = 'hr.employee.position'
    _description = 'Employee Position'

    employee_id = fields.Many2one('hr.employee', string='Employee', default=lambda self: self.env.user.employee_id,
                                  readonly=True)

    # TODO: Task 3.1.1
    department_id = fields.Many2one('hr.department', string='Department', required=True)
    manager_id = fields.Many2one('hr.employee', string='Manager')
    coach_id = fields.Many2one('hr.employee', string='Coach')

    # TODO: Task 3.1.2
    job_position_id = fields.Many2one('hr.job', string='Job Position', domain="[('department_id', '=', department_id)]",
                                      required=True)

    # TODO: Task 3.1.3
    employee_type = fields.Selection(related='employee_id.employee_type', string='Employee Type', readonly=True)

    # TODO: Task 3.1.4
    current_contract_id = fields.Many2one('hr.contract', string='Current Contract',
                                          domain="[('employee_id', '=', employee_id), ('job_id', '=', job_position_id)]")

    date_start = fields.Date(string='Date Start', required=True)
    date_end = fields.Date(string='Date End')

    # TODO: Task 3.3.3
    vacation_direct_supervisor_id = fields.Many2one('hr.employee', string='Vacation (Direct Supervisor)',
                                                    domain=lambda self: self._get_admin_leave_manager_domain())
    vacation_hr_manager_id = fields.Many2one('hr.employee', string='Vacation (HR Manager)',
                                             domain=lambda self: self._get_admin_leave_manager_domain())

    # TODO: Task 3.3.4
    expenses_id = fields.Many2one('hr.employee', string='Expenses')

    # TODO: Task 3.4.1
    work_location = fields.Char(string='Work Location')

    # TODO: Task 3.4.2
    working_hours = fields.Char(string='Working Hours', compute='_compute_working_hours', store=True, readonly=True)

    # TODO: Tasks 3.5.1 - 3.5.4
    total_vacation_days = fields.Integer(string='Total Vacation, days', readonly=True)
    used_vacation_days = fields.Integer(string='Used Vacation, days', readonly=True)
    rest_vacation_days = fields.Integer(string='Rest of Vacation, days', readonly=True)
    note = fields.Text(string='Note')

    def _get_admin_leave_manager_domain(self):
        admin_user = self.env.ref('base.user_admin')
        if admin_user:
            admin_id = admin_user.id
            return [
                ('leave_manager_id', '=', admin_id),
                ('leave_manager_id', '!=', False)
            ]
        else:
            return []

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for record in self:
            if record.date_end and record.date_start and record.date_end < record.date_start:
                raise ValidationError('The end date cannot be earlier than the start date.')

    # TODO: Set recommended working hours per week from job card 3.4.1
    @api.depends('job_position_id')
    def _compute_working_hours(self):
        for record in self:
            record.working_hours = record.job_position_id.working_hours if record.job_position_id else ''

    @api.onchange('job_position_id')
    def _onchange_job_position(self):
        self.current_contract_id = False
