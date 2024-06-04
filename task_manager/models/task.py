from odoo import models, fields


class Task(models.Model):
    _name = "task.manager.task"
    _description = "Task"

    name = fields.Char(string="Task name", required=True)
    description = fields.Text(string='Description')
    due_date = fields.Date(string='Due Date')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Priority', default='medium')
    status = fields.Selection([
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string='Status', default='todo')
    category_ids = fields.Many2many(
        'task.manager.category', string='Categories')
    user_id = fields.Many2one('res.users', string='Assigned User')
