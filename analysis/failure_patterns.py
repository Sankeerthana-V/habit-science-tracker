import os
import pandas as pd
import logging

FILE_NAME = os.path.join("data", "habit_log.csv")

logger = logging.getLogger(__name__)


def failure_patterns():
    logger.info("Failure pattern analysis started.")

    if not os.path.exists(FILE_NAME):
        logger.warning("CSV file not found during failure pattern analysis.")
        print("No data found.")
        return

    try:
        df = pd.read_csv(FILE_NAME)
        logger.info("CSV file loaded successfully for failure pattern analysis.")

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])

        df["done"] = df["done"].astype(str).str.lower().str.strip()

        failures = df[df["done"] == "no"].copy()

        if failures.empty:
            logger.info("No failure days found (all entries are yes).")
            print("No failure days found (all are yes).")
            return

        failures["sleep_hours"] = pd.to_numeric(failures["sleep_hours"], errors="coerce")
        failures["stress_level"] = pd.to_numeric(failures["stress_level"], errors="coerce")

        avg_sleep = failures["sleep_hours"].mean()
        avg_stress = failures["stress_level"].mean()

        failures["weekday"] = failures["date"].dt.day_name()
        worst_day = failures["weekday"].value_counts().idxmax()

        logger.info(
            "Failure analysis results -> Avg Sleep: %.2f | Avg Stress: %.2f | Worst Day: %s",
            avg_sleep,
            avg_stress,
            worst_day,
        )

        print("\n--- Failure Pattern Analysis ---")
        print("Average sleep on failure days:", round(avg_sleep, 2))
        print("Average stress on failure days:", round(avg_stress, 2))
        print("Most common failure weekday:", worst_day)

    except Exception:
        logger.exception("Error occurred during failure pattern analysis.")
        print("Failure pattern analysis failed. Check logs/app.log for details.")