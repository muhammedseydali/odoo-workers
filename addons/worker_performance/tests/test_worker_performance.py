from odoo.tests.common import TransactionCase

class TestWorkerPerformance(TransactionCase):

    def setUp(self):
        super().setUp()
        self.employee = self.env["hr.employee"].create({
            "name": "Test Worker"
        })

    def test_bonus_calculation(self):
        perf = self.env["worker.performance"].create({
            "worker_id": self.employee.id,
            "score": 9,
        })
        perf.action_submit()
        perf.action_approve()
        self.assertEqual(perf.performance_amount, 300)

    def test_payroll_input_created(self):
        slip = self.env["hr.payslip"].create({
            "employee_id": self.employee.id,
        })
        perf = self.env["worker.performance"].create({
            "worker_id": self.employee.id,
            "score": 6,
        })
        perf.action_submit()
        perf.action_approve()

        inputs = slip.input_line_ids.filtered(
            lambda i: i.code == "PERF_BONUS"
        )
        self.assertTrue(inputs)

    def test_api_creation(self):
        response = self.env["worker.performance"].create({
            "worker_id": self.employee.id,
            "score": 7,
        })
        self.assertEqual(response.score, 7)
