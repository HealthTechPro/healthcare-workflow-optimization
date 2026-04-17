def route_case(case):
    if case["patient_status"] == "admitted":
        return "HOLD_ADMITTED"
    elif case["discharge_summary_status"] == "complete":
        return "READY_FOR_OPERATOR"
    elif case["discharge_summary_status"] in ["missing", "unsigned"]:
        if case["hours_since_discharge"] < case["expected_tat"]:
            return "PROVIDER_QUEUE"
        else:
            return "PROVIDER_ALERT_OVERDUE"
    else:
        return "REVIEW"


sample_cases = [
    {
        "patient_id": "001",
        "patient_status": "admitted",
        "discharge_summary_status": "missing",
        "hours_since_discharge": 0,
        "expected_tat": 24,
    },
    {
        "patient_id": "002",
        "patient_status": "discharged",
        "discharge_summary_status": "unsigned",
        "hours_since_discharge": 12,
        "expected_tat": 24,
    },
    {
        "patient_id": "003",
        "patient_status": "discharged",
        "discharge_summary_status": "missing",
        "hours_since_discharge": 30,
        "expected_tat": 24,
    },
    {
        "patient_id": "004",
        "patient_status": "discharged",
        "discharge_summary_status": "complete",
        "hours_since_discharge": 10,
        "expected_tat": 24,
    },
]

for case in sample_cases:
    result = route_case(case)
    print(f'Patient {case["patient_id"]}: {result}')
