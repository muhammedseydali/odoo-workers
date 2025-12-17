{
    "name": "Worker Performance Evaluation",
    "version": "17.0.1.0.0",
    "summary": "Performance reviews linked to payroll",
    "description": "Manage worker performance, calculate bonus, and integrate with payroll.",
    "category": "Human Resources",
    "author": "Muhammed Seydali",
    "website": "https://muhammedseydali.github.io/Portfolio-personal/",
    "depends": ["hr", "hr_payroll"],
    "data": [
        "security/ir.model.access.csv",
        "security/worker_performance_rules.xml",
        "data/payroll_input_type.xml",
        "views/worker_performance_views.xml",
        "views/hr_employee_views.xml",
        "report/worker_performance_report.xml",
        "report/worker_performance_report_template.xml"
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False
}
