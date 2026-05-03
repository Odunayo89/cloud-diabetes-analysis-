import pandas as pd

df = pd.read_csv("diabetes_with_header.csv")

print("Dataset shape:")
print(df.shape)

print("\nOutcome counts:")
print(df["Outcome"].value_counts())

print("\nSummary statistics:")
print(df.describe())

df["Outcome"].value_counts().to_csv("outcome_counts.csv")

print("\nSaved outcome_counts.csv")
