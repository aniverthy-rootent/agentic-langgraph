"""Workforce Scheduling

Task: Build next week's shift schedule for 40 retail staff.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'workforce_scheduling'
TITLE = 'Workforce Scheduling'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = "Build next week's shift schedule for 40 retail staff."

# (key, role, instruction)
AGENTS = [
    ('demand_forecaster', 'Demand Forecaster', 'Forecast hourly traffic.'),
    ('availability_collector', 'Availability Collector', 'Gather staff constraints.'),
    ('schedule_builder', 'Schedule Builder', 'Draft shifts.'),
    ('compliance_checker', 'Compliance Checker', 'Check labor rules.'),
    ('fairness_auditor', 'Fairness Auditor', 'Balance weekends and overtime.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
