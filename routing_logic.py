import csv

def route_case(case):
    if case["patient_status"] == "admitted":
        return "HOLD_ADMITTED"

    elif case["discharge_summary_status"] == "complete":
        return "READY_FOR_OPERATOR"

    elif case["discharge_summary_status"] in ["missing", "unsigned"]:
        if int(case["hours_since_discharge"]) < int(case["expected_tat"]):
            return "PROVIDER_QUEUE"
        else:
            return "PROVIDER_ALERT_OVERDUE"

    else:
        return "REVIEW"


# Read data from CSV
with open("sample_data.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for case in reader:
        result = route_case(case)
        print(f'Patient {case["patient_id"]}: {result}')
