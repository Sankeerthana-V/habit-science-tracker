import os
import pandas as pd
import matplotlib.pyplot as plt
import logging

FILE_NAME = os.path.join("data", "habit_log.csv")

logger = logging.getLogger(__name__)


def make_charts():
    logger.info("Chart generation started.")

    if not os.path.exists(FILE_NAME):
        logger.warning("CSV file not found during chart generation.")
        print("No data found.")
        return

    try:
        df = pd.read_csv(FILE_NAME)
        logger.info("CSV file loaded successfully for chart generation.")

        df["done"] = df["done"].astype(str).str.lower().str.strip()
        df["sleep_hours"] = pd.to_numeric(df["sleep_hours"], errors="coerce")
        df["stress_level"] = pd.to_numeric(df["stress_level"], errors="coerce")

        os.makedirs("visuals", exist_ok=True)


        
        sleep_avg = df.groupby("done")["sleep_hours"].mean()
        logger.debug("Sleep averages by done: %s", sleep_avg.to_dict())

        plt.figure()
        sleep_avg.plot(kind="bar")
        plt.title("Average Sleep vs Completion")
        plt.tight_layout()

        sleep_path = os.path.join("visuals", "sleep_vs_completion.png")
        plt.savefig(sleep_path)
        plt.close()

        logger.info("Sleep chart saved at: %s", sleep_path)

        
        stress_avg = df.groupby("done")["stress_level"].mean()
        logger.debug("Stress averages by done: %s", stress_avg.to_dict())

        plt.figure()
        stress_avg.plot(kind="bar")
        plt.title("Average Stress vs Completion")
        plt.tight_layout()

        stress_path = os.path.join("visuals", "stress_vs_completion.png")
        plt.savefig(stress_path)
        plt.close()

        logger.info("Stress chart saved at: %s", stress_path)

        print("Charts saved in visuals/ folder.")

    except Exception:
        logger.exception("Error occurred during chart generation.")
        print("Chart generation failed. Check logs/app.log for details.")