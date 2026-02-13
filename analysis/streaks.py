import pandas as pd
import os

FILE_NAME = os.path.join("data", "habit_log.csv")


def streak_analysis():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    df = pd.read_csv(FILE_NAME)

    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values("date")

    streaks = []
    current_streak = 0

    for done in df["done"]:
        if done.lower() == "yes":
            current_streak += 1
        else:
            if current_streak > 0:
                streaks.append(current_streak)
            current_streak = 0

    
    if current_streak > 0:
        streaks.append(current_streak)

    if not streaks:
        print("No successful streaks found.")
        return

    longest = max(streaks)
    average = sum(streaks) / len(streaks)

    print("\n--- Streak Analysis ---")
    print("Longest streak:", longest)
    print("Average streak:", round(average, 2))
