from odoo import http
from odoo.http import request

class WorkerPerformanceAPI(http.Controller):

    @http.route("/api/performance", type="json", auth="user", methods=["POST"])
    def create_performance(self, **data):
        rec = request.env["worker.performance"].sudo().create({
            "worker_id": data.get("worker_id"),
            "score": data.get("score"),
            "note": data.get("note"),
        })
        return {"id": rec.id, "state": rec.state}
