"""Expense Audit

Task: Audit a month of employee expense reports.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'expense_audit'
TITLE = 'Expense Audit'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Audit a month of employee expense reports.'

# (key, role, instruction)
AGENTS = [
    ('receipt_reader', 'Receipt Reader', 'Parse receipts.'),
    ('policy_auditor', 'Policy Auditor', 'Compare against travel policy.'),
    ('duplicate_detector', 'Duplicate Detector', 'Find duplicate claims.'),
    ('anomaly_analyst', 'Anomaly Analyst', 'Flag unusual spend.'),
    ('audit_reporter', 'Audit Reporter', 'Write findings.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
