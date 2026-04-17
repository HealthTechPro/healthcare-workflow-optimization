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


# Read input and write output
with open("sample_data.csv", mode="r") as infile, open("routing_results.csv", mode="w", newline="") as outfile:
    reader = csv.DictReader(infile)

    fieldnames = reader.fieldnames + ["routing_decision"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for case in reader:
        decision = route_case(case)
        case["routing_decision"] = decision
        writer.writerow(case)

        print(f'Patient {case["patient_id"]}: {decision}')
