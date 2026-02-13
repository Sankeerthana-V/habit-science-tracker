import csv
import os

FILE_NAME = os.path.join("data", "habit_log.csv")


def view_logs():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    print("\n--- All Habit Logs ---\n")

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print("|".join(row))