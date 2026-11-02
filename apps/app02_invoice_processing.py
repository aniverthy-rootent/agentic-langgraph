"""Invoice Processing

Task: Process a vendor invoice of 12,400 EUR with PO mismatch.
Framework: LangGraph
"""
from runtime import run_app

SLUG = 'invoice_processing'
TITLE = 'Invoice Processing'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Process a vendor invoice of 12,400 EUR with PO mismatch.'

# (key, role, instruction)
AGENTS = [
    ('ocr_extractor', 'OCR Extractor', 'Extract invoice fields.'),
    ('po_matcher', 'PO Matcher', 'Match invoice to purchase order.'),
    ('tax_checker', 'Tax Checker', 'Verify VAT and totals.'),
    ('approval_router', 'Approval Router', 'Pick the approver by amount.'),
    ('ledger_poster', 'Ledger Poster', 'Prepare the accounting entry.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
