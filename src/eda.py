import pandas as pd

def run_eda(df: pd.DataFrame):
    """Phân tích khám phá dữ liệu (EDA)"""
    print("="*60)
    print("📊 1. THỐNG KÊ MÔ TẢ")
    print(df[['TotalSteps', 'Calories', 'TotalMinutesAsleep', 'TotalTimeInBed']].describe())

    print("\n🔗 2. MA TRẬN TƯƠNG QUAN")
    corr = df[['TotalSteps', 'Calories', 'TotalMinutesAsleep', 'TotalTimeInBed']].corr()
    print(corr.round(3))

    print("\n📉 Số ngày có dữ liệu giấc ngủ:", df['TotalMinutesAsleep'].notna().sum())
    print("="*60)