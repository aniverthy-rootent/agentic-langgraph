"""Meeting Follow-up Automation

Task: Turn a raw 45-minute product sync transcript into actions.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'meeting_followup'
TITLE = 'Meeting Follow-up Automation'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Turn a raw 45-minute product sync transcript into actions.'

# (key, role, instruction)
AGENTS = [
    ('transcript_cleaner', 'Transcript Cleaner', 'Remove filler and fix names.'),
    ('decision_extractor', 'Decision Extractor', 'List decisions made.'),
    ('action_item_tracker', 'Action Item Tracker', 'List owners and deadlines.'),
    ('risk_spotter', 'Risk Spotter', 'Flag unresolved risks.'),
    ('summary_writer', 'Summary Writer', 'Write the recap email.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
