import csv
import os
import logging

FILE_NAME = os.path.join("data", "habit_log.csv")

logger = logging.getLogger(__name__)


def view_logs():
    logger.info("View logs function called.")

    if not os.path.exists(FILE_NAME):
        logger.warning("CSV file not found when attempting to view logs.")
        print("No data found.")
        return

    print("\n--- All Habit Logs ---\n")

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            row_count = 0

            for row in reader:
                print("|".join(row))
                row_count += 1

        logger.info("Displayed %d rows from CSV file.", row_count)

    except Exception:
        logger.exception("Error occurred while reading CSV file.")
        print("Failed to read logs. Check logs/app.log for details.")