"""Warehouse Slotting Optimizer

Task: Re-slot 500 SKUs to reduce picker travel time.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'warehouse_slotting'
TITLE = 'Warehouse Slotting Optimizer'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Re-slot 500 SKUs to reduce picker travel time.'

# (key, role, instruction)
AGENTS = [
    ('demand_profiler', 'Demand Profiler', 'Classify SKUs by velocity.'),
    ('affinity_analyst', 'Affinity Analyst', 'Find items bought together.'),
    ('layout_planner', 'Layout Planner', 'Propose slot assignments.'),
    ('labor_estimator', 'Labor Estimator', 'Estimate time savings.'),
    ('change_manager', 'Change Manager', 'Plan the transition.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
