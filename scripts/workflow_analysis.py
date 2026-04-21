import pandas as pd

# Load dataset from data folder
df = pd.read_csv("data/sample_operational_data.csv")

print("=== Healthcare Workflow Analysis ===\n")
print("Operational Data:")
print(df)
print("\n")

# Total cases
total_cases = df["cases_reviewed"].sum()
print(f"Total cases reviewed: {total_cases}")

# Delay breakdown
print("\nDelay Reason Counts:")
print(df["delay_reason"].value_counts())

# Queue totals
print("\nCases Reviewed by Queue:")
print(df.groupby("queue_name")["cases_reviewed"].sum())

# Save output
summary = df.groupby("queue_name")["cases_reviewed"].sum().reset_index()
summary.columns = ["queue_name", "total_cases_reviewed"]
summary.to_csv("data/queue_summary.csv", index=False)

print("\nSummary saved as data/queue_summary.csv")
