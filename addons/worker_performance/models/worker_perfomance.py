from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date

class WorkerPerformance(models.Model):
    _name = "worker.performance"
    _description = "Worker Performance Evaluation"
    _inherit = ["mail.thread"]

    worker_id = fields.Many2one(
        "hr.employee", required=True, tracking=True
    )
    date = fields.Date(default=fields.Date.today)
    score = fields.Integer(required=True)
    note = fields.Text()
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("submitted", "Submitted"),
            ("approved", "Approved"),
        ],
        default="draft",
        tracking=True,
    )
    approved_by = fields.Many2one("res.users")
    performance_amount = fields.Float(
        compute="_compute_performance_amount", store=True
    )

    @api.depends("score", "state")
    def _compute_performance_amount(self):
        for rec in self:
            if rec.state == "approved":
                if rec.score >= 8:
                    rec.performance_amount = 300
                elif rec.score >= 5:
                    rec.performance_amount = 150
                else:
                    rec.performance_amount = 0
            else:
                rec.performance_amount = 0

    def action_submit(self):
        for rec in self:
            rec.state = "submitted"

    def action_approve(self):
        for rec in self:
            if rec.state != "submitted":
                raise UserError("Only submitted records can be approved")
            rec.state = "approved"
            rec.approved_by = self.env.user
            rec._create_payroll_input()

    def _create_payroll_input(self):
        input_type = self.env.ref(
            "worker_performance.input_performance_bonus"
        )

        payslip = self.env["hr.payslip"].search([
            ("employee_id", "=", self.worker_id.id),
            ("state", "=", "draft"),
        ], limit=1)

        if not payslip:
            return

        self.env["hr.payslip.input"].create({
            "payslip_id": payslip.id,
            "input_type_id": input_type.id,
            "amount": self.performance_amount,
            "name": "Performance Bonus",
        })
