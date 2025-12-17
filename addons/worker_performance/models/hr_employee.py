from odoo import models

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def action_view_performance(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Performance Evaluations",
            "res_model": "worker.performance",
            "view_mode": "tree,form",
            "domain": [("worker_id", "=", self.id)],
        }
