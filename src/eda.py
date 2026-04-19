import pandas as pd

def run_eda(df: pd.DataFrame):
    print("="*70)
    print("📊 1. THỐNG KÊ MÔ TẢ")
    print(df[['TotalSteps', 'Calories', 'TotalMinutesAsleep',
              'TotalTimeInBed', 'VeryActiveMinutes']].describe().round(2))

    print("\n🔗 2. MA TRẬN TƯƠNG QUAN")
    corr = df[['TotalSteps', 'Calories', 'TotalMinutesAsleep',
               'TotalTimeInBed', 'VeryActiveMinutes']].corr()
    print(corr.round(3))

    print(f"\n📉 Số ngày có dữ liệu giấc ngủ: {df['TotalMinutesAsleep'].notna().sum()}")
    print(f"   Tỷ lệ missing sleep: {df['TotalMinutesAsleep'].isna().mean():.1%}")
    print("="*70)