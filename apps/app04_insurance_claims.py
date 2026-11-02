"""Insurance Claims Adjudication

Task: Handle a water-damage home insurance claim of 8,000 USD.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'insurance_claims'
TITLE = 'Insurance Claims Adjudication'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Handle a water-damage home insurance claim of 8,000 USD.'

# (key, role, instruction)
AGENTS = [
    ('claim_intake', 'Claim Intake', 'Structure the claim.'),
    ('policy_checker', 'Policy Checker', 'Verify coverage and exclusions.'),
    ('damage_estimator', 'Damage Estimator', 'Estimate repair cost.'),
    ('fraud_detector', 'Fraud Detector', 'Look for suspicious patterns.'),
    ('settlement_negotiator', 'Settlement Negotiator', 'Propose a payout.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
