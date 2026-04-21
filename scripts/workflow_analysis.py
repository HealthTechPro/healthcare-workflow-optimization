import pandas as pd

# Sample operational workflow data
data = {
    "queue_name": [
        "Primary Work Queue",
        "Secondary Work Queue",
        "Primary Work Queue",
        "Secondary Work Queue",
        "Primary Work Queue"
    ],
    "cases_reviewed": [30, 75, 9, 26, 12],
    "delay_reason": [
        "Missing discharge summary",
        "Incomplete documentation",
        "Missing discharge summary",
        "Pending chart merge",
        "Active admission"
    ],
    "status": [
        "Reduced",
        "Triaged",
        "Reviewed",
        "Reviewed",
        "Pending"
    ]
}

df = pd.DataFrame(data)

print("=== Healthcare Workflow Analysis ===\n")
print("Operational Data:")
print(df)
print("\n")

# Summary 1: total cases reviewed
total_cases = df["cases_reviewed"].sum()
print(f"Total cases reviewed: {total_cases}")

# Summary 2: delay reason frequency
print("\nDelay Reason Counts:")
print(df["delay_reason"].value_counts())

# Summary 3: queue totals
print("\nCases Reviewed by Queue:")
print(df.groupby("queue_name")["cases_reviewed"].sum())

# Save summary to CSV
summary = df.groupby("queue_name")["cases_reviewed"].sum().reset_index()
summary.columns = ["queue_name", "total_cases_reviewed"]
summary.to_csv("queue_summary.csv", index=False)

print("\nSummary saved as queue_summary.csv")
