import logging
import os

from input.log_day import log_day
from analysis.view_logs import view_logs
from analysis.streaks import streak_analysis
from analysis.failure_patterns import failure_patterns
from analysis.correlations import correlation_analysis
from visuals.charts import make_charts


def setup_logging():
    os.makedirs("logs", exist_ok=True)  

    logging.basicConfig(
        level=logging.INFO,  
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(os.path.join("logs", "app.log"), encoding="utf-8"),
            logging.StreamHandler()  
        ],
    )


logger = logging.getLogger(__name__)


def main():
    setup_logging()
    logger.info("Habit Tracker application started.")

    while True:
       
        print("\n==== Habit Tracker ====")
        print("1. Log Day")
        print("2. View Logs")
        print("3. Streak Analysis")
        print("4. Failure Patterns")
        print("5. Correlations")
        print("6. Create Charts")
        print("7. Exit")

        choice = input("Choose option (1-7): ").strip()
        logger.info("User selected menu option: %s", choice)

        try:
            if choice == "1":
                logger.info("Calling log_day()")
                log_day()

            elif choice == "2":
                logger.info("Calling view_logs()")
                view_logs()

            elif choice == "3":
                logger.info("Calling streak_analysis()")
                streak_analysis()

            elif choice == "4":
                logger.info("Calling failure_patterns()")
                failure_patterns()

            elif choice == "5":
                logger.info("Calling correlation_analysis()")
                correlation_analysis()

            elif choice == "6":
                logger.info("Calling make_charts()")
                make_charts()

            elif choice == "7":
                print("Goodbye!")
                logger.info("User exited the application.")
                break

            else:
                print("Invalid choice. Try again.")
                logger.warning("Invalid menu choice entered: %s", choice)

        except Exception:
        
            logger.exception("An error occurred while processing choice: %s", choice)
            print("Something went wrong. Check logs/app.log for details.")

    logger.info("Habit Tracker application ended.")


if __name__ == "__main__":
    main()