# Agent roster: agentic-langgraph

_Business & operations workflows as stateful graphs_


## 1. Order Fulfillment Graph (`apps/app01_order_fulfillment.py`)

Task: Process an order for 3 laptops shipping to Berlin with express delivery.

- **Order Validator** (`order_validator`): Check order fields and stock.
- **Inventory Allocator** (`inventory_allocator`): Reserve stock from warehouses.
- **Fraud Screener** (`fraud_screener`): Score payment risk.
- **Shipping Planner** (`shipping_planner`): Choose carrier and route.
- **Notification Agent** (`notification_agent`): Draft customer updates.

## 2. Invoice Processing (`apps/app02_invoice_processing.py`)

Task: Process a vendor invoice of 12,400 EUR with PO mismatch.

- **OCR Extractor** (`ocr_extractor`): Extract invoice fields.
- **PO Matcher** (`po_matcher`): Match invoice to purchase order.
- **Tax Checker** (`tax_checker`): Verify VAT and totals.
- **Approval Router** (`approval_router`): Pick the approver by amount.
- **Ledger Poster** (`ledger_poster`): Prepare the accounting entry.

## 3. Loan Underwriting (`apps/app03_loan_underwriting.py`)

Task: Evaluate a 250k small-business loan application.

- **Applicant Profiler** (`applicant_profiler`): Summarize applicant data.
- **Credit Analyst** (`credit_analyst`): Assess credit history.
- **Cash Flow Analyst** (`cash_flow_analyst`): Evaluate repayment capacity.
- **Collateral Appraiser** (`collateral_appraiser`): Value the collateral.
- **Risk Officer** (`risk_officer`): Assign risk grade.
- **Decision Writer** (`decision_writer`): Draft the decision letter.

## 4. Insurance Claims Adjudication (`apps/app04_insurance_claims.py`)

Task: Handle a water-damage home insurance claim of 8,000 USD.

- **Claim Intake** (`claim_intake`): Structure the claim.
- **Policy Checker** (`policy_checker`): Verify coverage and exclusions.
- **Damage Estimator** (`damage_estimator`): Estimate repair cost.
- **Fraud Detector** (`fraud_detector`): Look for suspicious patterns.
- **Settlement Negotiator** (`settlement_negotiator`): Propose a payout.

## 5. Supply Chain Disruption Response (`apps/app05_supply_chain_disruption.py`)

Task: A port strike delays chip shipments by 3 weeks.

- **Disruption Monitor** (`disruption_monitor`): Quantify the delay.
- **Supplier Finder** (`supplier_finder`): Identify alternative suppliers.
- **Cost Modeler** (`cost_modeler`): Compare costs of alternatives.
- **Production Planner** (`production_planner`): Re-sequence production.
- **Customer Communicator** (`customer_communicator`): Notify affected customers.

## 6. Meeting Follow-up Automation (`apps/app06_meeting_followup.py`)

Task: Turn a raw 45-minute product sync transcript into actions.

- **Transcript Cleaner** (`transcript_cleaner`): Remove filler and fix names.
- **Decision Extractor** (`decision_extractor`): List decisions made.
- **Action Item Tracker** (`action_item_tracker`): List owners and deadlines.
- **Risk Spotter** (`risk_spotter`): Flag unresolved risks.
- **Summary Writer** (`summary_writer`): Write the recap email.

## 7. Expense Audit (`apps/app07_expense_audit.py`)

Task: Audit a month of employee expense reports.

- **Receipt Reader** (`receipt_reader`): Parse receipts.
- **Policy Auditor** (`policy_auditor`): Compare against travel policy.
- **Duplicate Detector** (`duplicate_detector`): Find duplicate claims.
- **Anomaly Analyst** (`anomaly_analyst`): Flag unusual spend.
- **Audit Reporter** (`audit_reporter`): Write findings.

## 8. B2B Customer Onboarding (`apps/app08_customer_onboarding.py`)

Task: Onboard a 200-seat enterprise customer onto a SaaS platform.

- **Kickoff Planner** (`kickoff_planner`): Build the onboarding plan.
- **Data Migrator** (`data_migrator`): Plan data import.
- **Integration Engineer** (`integration_engineer`): Plan SSO and API setup.
- **Training Designer** (`training_designer`): Design training sessions.
- **Success Manager** (`success_manager`): Define success metrics.
- **Go-Live Reviewer** (`go_live_reviewer`): Check readiness.

## 9. Warehouse Slotting Optimizer (`apps/app09_warehouse_slotting.py`)

Task: Re-slot 500 SKUs to reduce picker travel time.

- **Demand Profiler** (`demand_profiler`): Classify SKUs by velocity.
- **Affinity Analyst** (`affinity_analyst`): Find items bought together.
- **Layout Planner** (`layout_planner`): Propose slot assignments.
- **Labor Estimator** (`labor_estimator`): Estimate time savings.
- **Change Manager** (`change_manager`): Plan the transition.

## 10. Procurement RFP Evaluation (`apps/app10_procurement_rfp.py`)

Task: Compare 4 vendor proposals for a cloud contact-center system.

- **Requirement Extractor** (`requirement_extractor`): List must-have requirements.
- **Proposal Scorer** (`proposal_scorer`): Score each proposal.
- **Cost Analyst** (`cost_analyst`): Compute total cost of ownership.
- **Risk Assessor** (`risk_assessor`): Assess vendor risk.
- **Recommendation Writer** (`recommendation_writer`): Write the recommendation memo.

## 11. Workforce Scheduling (`apps/app11_workforce_scheduling.py`)

Task: Build next week's shift schedule for 40 retail staff.

- **Demand Forecaster** (`demand_forecaster`): Forecast hourly traffic.
- **Availability Collector** (`availability_collector`): Gather staff constraints.
- **Schedule Builder** (`schedule_builder`): Draft shifts.
- **Compliance Checker** (`compliance_checker`): Check labor rules.
- **Fairness Auditor** (`fairness_auditor`): Balance weekends and overtime.
