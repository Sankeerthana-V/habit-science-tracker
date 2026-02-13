import os
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = os.path.join("data", "habit_log.csv")

def make_charts():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    df = pd.read_csv(FILE_NAME)
    df["done"] = df["done"].astype(str).str.lower().str.strip()
    df["sleep_hours"] = pd.to_numeric(df["sleep_hours"], errors="coerce")
    df["stress_level"] = pd.to_numeric(df["stress_level"], errors="coerce")

    os.makedirs("visuals", exist_ok=True)

    # Chart 1: Sleep vs completion
    sleep_avg = df.groupby("done")["sleep_hours"].mean()
    plt.figure()
    sleep_avg.plot(kind="bar")
    plt.title("Average Sleep vs Completion")
    plt.tight_layout()
    plt.savefig(os.path.join("visuals", "sleep_vs_completion.png"))
    plt.close()

    # Chart 2: Stress vs completion
    stress_avg = df.groupby("done")["stress_level"].mean()
    plt.figure()
    stress_avg.plot(kind="bar")
    plt.title("Average Stress vs Completion")
    plt.tight_layout()
    plt.savefig(os.path.join("visuals", "stress_vs_completion.png"))
    plt.close()

    print("Charts saved in visuals/ folder.")