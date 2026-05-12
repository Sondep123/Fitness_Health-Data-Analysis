import pandas as pd
from pathlib import Path

def clean_activity(activity_file: str, output_file: str):
    print("🔄 Đang làm sạch dữ liệu Activity...")
    activity = pd.read_csv(activity_file)

    activity = activity[['Id', 'ActivityDate', 'TotalSteps', 'Calories', 'VeryActiveMinutes']]

    activity['ActivityDate'] = pd.to_datetime(
        activity['ActivityDate'], format='%m/%d/%Y'
    ).dt.normalize()

    # Fillna bằng median
    numeric_cols = ['TotalSteps', 'Calories', 'VeryActiveMinutes']
    activity[numeric_cols] = activity[numeric_cols].fillna(activity[numeric_cols].median())

    # Đếm trùng lặp trước khi xóa
    duplicates_count = activity.duplicated().sum()
    activity.drop_duplicates(inplace=True)
    # Xóa outlier rõ ràng
    outliers = activity[(activity['TotalSteps'] == 0) & (activity['Calories'] > 2000)]
    outliers_count = outliers.shape[0]
    activity = activity.drop(outliers.index)

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    activity.to_csv(output_file, index=False)

    print(f"✅ Clean Activity xong → {output_file} | Shape: {activity.shape}")
    print(f"   → Trùng lặp bị xóa: {duplicates_count}")
    print(f"   → Outlier bị xóa: {outliers_count}")
    return activity


def clean_sleep(sleep_file: str, output_file: str):
    print("🔄 Đang làm sạch dữ liệu Sleep...")
    sleep = pd.read_csv(sleep_file)

    sleep = sleep[['Id', 'SleepDay', 'TotalMinutesAsleep', 'TotalTimeInBed']]

    sleep['SleepDay'] = pd.to_datetime(
        sleep['SleepDay'], format='%m/%d/%Y %I:%M:%S %p'
    ).dt.normalize()

    # Fillna bằng median
    numeric_cols = ['TotalMinutesAsleep', 'TotalTimeInBed']
    sleep[numeric_cols] = sleep[numeric_cols].fillna(sleep[numeric_cols].median())

    # Đếm trùng lặp trước khi xóa
    duplicates_count = sleep.duplicated().sum()
    sleep.drop_duplicates(inplace=True)

    # Xóa outlier: ngủ nhiều hơn thời gian nằm giường
    outliers = sleep[sleep['TotalMinutesAsleep'] > sleep['TotalTimeInBed']]
    outliers_count = outliers.shape[0]
    sleep = sleep.drop(outliers.index)

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    sleep.to_csv(output_file, index=False)

    print(f"✅ Clean Sleep xong → {output_file} | Shape: {sleep.shape}")
    print(f"   → Trùng lặp bị xóa: {duplicates_count}")
    print(f"   → Outlier bị xóa: {outliers_count}")
    return sleep
