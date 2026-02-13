import os
import pandas as pd

FILE_NAME = os.path.join("data", "habit_log.csv")

def failure_patterns():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    df = pd.read_csv(FILE_NAME)

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    df["done"] = df["done"].astype(str).str.lower().str.strip()

    failures = df[df["done"] == "no"].copy()

    if failures.empty:
        print("No failure days found (all are yes).")
        return

    failures["sleep_hours"] = pd.to_numeric(failures["sleep_hours"], errors="coerce")
    failures["stress_level"] = pd.to_numeric(failures["stress_level"], errors="coerce")

    avg_sleep = failures["sleep_hours"].mean()
    avg_stress = failures["stress_level"].mean()

    failures["weekday"] = failures["date"].dt.day_name()
    worst_day = failures["weekday"].value_counts().idxmax()

    print("\n--- Failure Pattern Analysis ---")
    print("Average sleep on failure days:", round(avg_sleep, 2))
    print("Average stress on failure days:", round(avg_stress, 2))
    print("Most common failure weekday:", worst_day)