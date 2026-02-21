import os
import pandas as pd
import logging

FILE_NAME = os.path.join("data", "habit_log.csv")

logger = logging.getLogger(__name__)


def correlation_analysis():
    logger.info("Correlation analysis started.")

    if not os.path.exists(FILE_NAME):
        logger.warning("CSV file not found during correlation analysis.")
        print("No data found.")
        return

    try:
        df = pd.read_csv(FILE_NAME)
        logger.info("CSV file loaded successfully for correlation analysis.")

        df["done"] = df["done"].astype(str).str.lower().str.strip()
        df["sleep_hours"] = pd.to_numeric(df["sleep_hours"], errors="coerce")
        df["stress_level"] = pd.to_numeric(df["stress_level"], errors="coerce")

        yes_days = df[df["done"] == "yes"]
        no_days = df[df["done"] == "no"]

        if yes_days.empty or no_days.empty:
            logger.info("Not enough data for comparison (need both yes and no days).")
            print("Need both YES and NO days to compare.")
            return

        sleep_yes = yes_days["sleep_hours"].mean()
        sleep_no = no_days["sleep_hours"].mean()
        stress_yes = yes_days["stress_level"].mean()
        stress_no = no_days["stress_level"].mean()

        logger.info(
            "Correlation results -> Sleep YES: %.2f | Sleep NO: %.2f | Stress YES: %.2f | Stress NO: %.2f",
            sleep_yes, sleep_no, stress_yes, stress_no
        )

        print("\n--- Correlation Analysis ---")
        print("Avg sleep (YES days):", round(sleep_yes, 2))
        print("Avg sleep (NO days): ", round(sleep_no, 2))
        print("Avg stress (YES days):", round(stress_yes, 2))
        print("Avg stress (NO days): ", round(stress_no, 2))

    except Exception:
        logger.exception("Error occurred during correlation analysis.")
        print("Correlation analysis failed. Check logs/app.log for details.")