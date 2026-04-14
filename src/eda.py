import pandas as pd

def run_eda(df):
    # Thống kê mô tả
    print("📊 Thống kê mô tả:")
    print(df[['TotalSteps','Calories','TotalMinutesAsleep','TotalTimeInBed']].describe())

    # Ma trận tương quan
    print("\n🔗 Ma trận tương quan:")
    print(df[['TotalSteps','Calories','TotalMinutesAsleep','TotalTimeInBed']].corr())
