"""Supply Chain Disruption Response

Task: A port strike delays chip shipments by 3 weeks.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'supply_chain_disruption'
TITLE = 'Supply Chain Disruption Response'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'A port strike delays chip shipments by 3 weeks.'

# (key, role, instruction)
AGENTS = [
    ('disruption_monitor', 'Disruption Monitor', 'Quantify the delay.'),
    ('supplier_finder', 'Supplier Finder', 'Identify alternative suppliers.'),
    ('cost_modeler', 'Cost Modeler', 'Compare costs of alternatives.'),
    ('production_planner', 'Production Planner', 'Re-sequence production.'),
    ('customer_communicator', 'Customer Communicator', 'Notify affected customers.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
