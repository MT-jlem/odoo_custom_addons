from odoo import models, fields


class Category(models.Model):
    _name = 'task.manager.category'
    _description = "Category"

    name = fields.Char("Category name", required=True)
    task_ids = fields.Many2many('task.manager.task', string='Tasks')
