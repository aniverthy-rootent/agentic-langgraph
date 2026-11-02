"""Procurement RFP Evaluation

Task: Compare 4 vendor proposals for a cloud contact-center system.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'procurement_rfp'
TITLE = 'Procurement RFP Evaluation'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Compare 4 vendor proposals for a cloud contact-center system.'

# (key, role, instruction)
AGENTS = [
    ('requirement_extractor', 'Requirement Extractor', 'List must-have requirements.'),
    ('proposal_scorer', 'Proposal Scorer', 'Score each proposal.'),
    ('cost_analyst', 'Cost Analyst', 'Compute total cost of ownership.'),
    ('risk_assessor', 'Risk Assessor', 'Assess vendor risk.'),
    ('recommendation_writer', 'Recommendation Writer', 'Write the recommendation memo.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
