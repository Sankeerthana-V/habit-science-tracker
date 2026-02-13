import csv
import os
from datetime import datetime

FILE_NAME = os.path.join("data", "habit_log.csv")

HEADER = ["date", "habit", "done", "sleep_hours", "stress_level", "energy_level"]


def ensure_header():
    os.makedirs("data", exist_ok=True)

    if (not os.path.exists(FILE_NAME)) or os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADER)


def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")  
            return date
        except ValueError:
            print("Invalid date. Example: 2026-02-12")


def get_done():
    while True:
        ans = input("Did you complete your habit? (yes/no): ").strip().lower()
        if ans in ("yes", "no"):
            return ans
        print("Please type only: yes or no")


def get_sleep_hours():
    while True:
        value = input("Sleep hours (0-24): ").strip()
        try:
            hours = float(value)
            if 0 <= hours <= 24:
                return hours
            else:
                print("Enter a number between 0 and 24.")
        except ValueError:
            print("Please enter a valid number.")


def get_level(prompt):
    while True:
        value = input(prompt).strip()
        try:
            level = int(value)
            if 1 <= level <= 5:
                return level
            else:
                print("Enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a whole number.")


def log_day():
    ensure_header()

    print("\n--- Log Your Day ---")
    date = get_valid_date()
    habit = input("Enter habit name: ").strip()
    done = get_done()
    sleep_hours = get_sleep_hours()
    stress_level = get_level("Stress level (1-5): ")
    energy_level = get_level("Energy level (1-5): ")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, habit, done, sleep_hours, stress_level, energy_level])

    print("Data saved successfully!")