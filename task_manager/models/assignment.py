from odoo import models, fields


class Assignment(models.Model):
    _name = "task.manager.assignment"
    _description = "Assignment"

    task_id = fields.Many2one("task.manager.task", string='Task')
    user_id = fields.Many2one("res.users", string='User')
