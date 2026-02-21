import pandas as pd
import os
import logging

FILE_NAME = os.path.join("data", "habit_log.csv")

logger = logging.getLogger(__name__)


def streak_analysis():
    logger.info("Streak analysis started.")

    if not os.path.exists(FILE_NAME):
        logger.warning("CSV file not found during streak analysis.")
        print("No data found.")
        return

    try:
        df = pd.read_csv(FILE_NAME)
        logger.info("CSV file loaded successfully for streak analysis.")

        
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.sort_values("date")

        df["done"] = df["done"].astype(str).str.lower().str.strip()

        streaks = []
        current_streak = 0

        for done in df["done"]:
            if done == "yes":
                current_streak += 1
            else:
                if current_streak > 0:
                    streaks.append(current_streak)
                current_streak = 0

        if current_streak > 0:
            streaks.append(current_streak)

        if not streaks:
            logger.info("No successful streaks found.")
            print("No successful streaks found.")
            return

        longest = max(streaks)
        average = sum(streaks) / len(streaks)

        logger.info(
            "Streak analysis completed. Longest=%d, Average=%.2f",
            longest,
            average,
        )

        print("\n--- Streak Analysis ---")
        print("Longest streak:", longest)
        print("Average streak:", round(average, 2))

    except Exception:
        logger.exception("Error occurred during streak analysis.")
        print("Streak analysis failed. Check logs/app.log for details.")