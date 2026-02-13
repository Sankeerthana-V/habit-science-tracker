import os
import pandas as pd

FILE_NAME = os.path.join("data", "habit_log.csv")

def correlation_analysis():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    df = pd.read_csv(FILE_NAME)

    df["done"] = df["done"].astype(str).str.lower().str.strip()
    df["sleep_hours"] = pd.to_numeric(df["sleep_hours"], errors="coerce")
    df["stress_level"] = pd.to_numeric(df["stress_level"], errors="coerce")

    yes_days = df[df["done"] == "yes"]
    no_days = df[df["done"] == "no"]

    if yes_days.empty or no_days.empty:
        print("Need both YES and NO days to compare.")
        return

    print("\n--- Correlation Analysis ---")
    print("Avg sleep (YES days):", round(yes_days["sleep_hours"].mean(), 2))
    print("Avg sleep (NO days): ", round(no_days["sleep_hours"].mean(), 2))
    print("Avg stress (YES days):", round(yes_days["stress_level"].mean(), 2))
    print("Avg stress (NO days): ", round(no_days["stress_level"].mean(), 2))