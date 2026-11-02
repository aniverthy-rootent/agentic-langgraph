"""B2B Customer Onboarding

Task: Onboard a 200-seat enterprise customer onto a SaaS platform.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'customer_onboarding'
TITLE = 'B2B Customer Onboarding'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Onboard a 200-seat enterprise customer onto a SaaS platform.'

# (key, role, instruction)
AGENTS = [
    ('kickoff_planner', 'Kickoff Planner', 'Build the onboarding plan.'),
    ('data_migrator', 'Data Migrator', 'Plan data import.'),
    ('integration_engineer', 'Integration Engineer', 'Plan SSO and API setup.'),
    ('training_designer', 'Training Designer', 'Design training sessions.'),
    ('success_manager', 'Success Manager', 'Define success metrics.'),
    ('go_live_reviewer', 'Go-Live Reviewer', 'Check readiness.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
