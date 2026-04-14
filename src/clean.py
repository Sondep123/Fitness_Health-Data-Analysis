import pandas as pd
from pathlib import Path

def clean_activity(activity_file: str, output_file: str):
    """Làm sạch dữ liệu hoạt động hàng ngày"""
    print("🔄 Đang làm sạch dữ liệu Activity...")
    activity = pd.read_csv(activity_file)

    activity = activity[['Id', 'ActivityDate', 'TotalSteps', 'Calories', 'VeryActiveMinutes']]

    # Chuẩn hóa ngày tháng
    activity['ActivityDate'] = pd.to_datetime(
        activity['ActivityDate'], format='%m/%d/%Y'
    ).dt.normalize()
    # xử lý missing values
    activity.fillna(activity.mean(numeric_only=True), inplace=True)
    # loại bỏ trùng lặp
    activity.drop_duplicates(inplace=True)

    # Xử lý outlier
    outliers = activity[(activity['TotalSteps'] == 0) & (activity['Calories'] > 2000)]
    activity = activity.drop(outliers.index)

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    activity.to_csv(output_file, index=False)
    print(f"✅ Clean Activity xong → {output_file} | Shape: {activity.shape}")
    return activity


def clean_sleep(sleep_file: str, output_file: str):
    """Làm sạch dữ liệu giấc ngủ"""
    print("🔄 Đang làm sạch dữ liệu Sleep...")
    sleep = pd.read_csv(sleep_file)

    sleep = sleep[['Id', 'SleepDay', 'TotalMinutesAsleep', 'TotalTimeInBed']]
     #chuẩn hóa ngày tháng
    sleep['SleepDay'] = pd.to_datetime(
        sleep['SleepDay'], format='%m/%d/%Y %I:%M:%S %p'
    ).dt.normalize()
    # xử lý missing values
    sleep.fillna(sleep.mean(numeric_only=True), inplace=True)
    #loại bỏ trùng lặp
    sleep.drop_duplicates(inplace=True)

    # Outlier
    outliers = sleep[sleep['TotalMinutesAsleep'] > sleep['TotalTimeInBed']]
    sleep = sleep.drop(outliers.index)

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    sleep.to_csv(output_file, index=False)
    print(f"✅ Clean Sleep xong → {output_file} | Shape: {sleep.shape}")
    return sleep


if __name__ == "__main__":
    # Test chạy riêng clean.py
    base = Path(__file__).parent
    project_root = base.parent

    clean_activity(
        activity_file=str(project_root / "dailyActivity_merged.csv"),
        output_file=str(project_root / "result" / "dailyActivity_cleaned.csv")
    )
    clean_sleep(
        sleep_file=str(project_root / "sleepDay_merged.csv"),
        output_file=str(project_root / "result" / "sleepDay_cleaned.csv")
    )