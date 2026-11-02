"""Loan Underwriting

Task: Evaluate a 250k small-business loan application.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'loan_underwriting'
TITLE = 'Loan Underwriting'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Evaluate a 250k small-business loan application.'

# (key, role, instruction)
AGENTS = [
    ('applicant_profiler', 'Applicant Profiler', 'Summarize applicant data.'),
    ('credit_analyst', 'Credit Analyst', 'Assess credit history.'),
    ('cash_flow_analyst', 'Cash Flow Analyst', 'Evaluate repayment capacity.'),
    ('collateral_appraiser', 'Collateral Appraiser', 'Value the collateral.'),
    ('risk_officer', 'Risk Officer', 'Assign risk grade.'),
    ('decision_writer', 'Decision Writer', 'Draft the decision letter.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
