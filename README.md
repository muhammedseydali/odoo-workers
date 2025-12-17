# Worker Performance Evaluation (Odoo Custom Module)

**Version:** 1.0  
**Author:** Muhammed Seydali  
**Description:**  
Odoo module for managing worker performance evaluations and optionally integrating computed bonuses into payroll.

---

## Features

- A new model `worker.performance` to record evaluations:
  - Worker (employee)
  - Evaluation date
  - Score (1–10)
  - Notes
  - State (draft / submitted / approved)
  - Computed bonus amount based on score
- Approval workflow with buttons
- Smart button on employee form to view performance records
- PDF report for evaluations in the last 30 days
- Optional API endpoint to create evaluations via JSON RPC
- Security rules to restrict access
  - HR managers have full access
  - HR officers can read/create
  - Employees can only see their own records
- Optional integration with payroll 

