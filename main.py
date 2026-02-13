from input.log_day import log_day
from analysis.view_logs import view_logs
from analysis.streaks import streak_analysis
from analysis.failure_patterns import failure_patterns
from analysis.correlations import correlation_analysis
from visuals.charts import make_charts

def main():
    while True:
        print("\n==== Habit Tracker ====")
        print("1. Log Day")
        print("2. View Logs")
        print("3. Streak Analysis")
        print("4. Failure Patterns")
        print("5. Correlations")
        print("6. Create Charts")
        print("7. Exit")

        choice = input("Choose option (1-7): ")

        if choice == "1":
            log_day()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            streak_analysis()
        elif choice== "4":
            failure_patterns()
        elif choice=="5":
            correlation_analysis()
        elif choice== "6":
            make_charts()
        elif choice== "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()