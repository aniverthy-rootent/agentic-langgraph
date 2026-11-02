"""Order Fulfillment Graph

Task: Process an order for 3 laptops shipping to Berlin with express delivery.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'order_fulfillment'
TITLE = 'Order Fulfillment Graph'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Process an order for 3 laptops shipping to Berlin with express delivery.'

# (key, role, instruction)
AGENTS = [
    ('order_validator', 'Order Validator', 'Check order fields and stock.'),
    ('inventory_allocator', 'Inventory Allocator', 'Reserve stock from warehouses.'),
    ('fraud_screener', 'Fraud Screener', 'Score payment risk.'),
    ('shipping_planner', 'Shipping Planner', 'Choose carrier and route.'),
    ('notification_agent', 'Notification Agent', 'Draft customer updates.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
