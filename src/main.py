import pandas as pd
from pathlib import Path
from clean import clean_activity, clean_sleep
from eda import run_eda
from visualization import visualize
from modeling import linear_regression

if __name__ == "__main__":
    print("🚀 BẮT ĐẦU PHÂN TÍCH DỮ LIỆU FITNESS & GIẤC NGỦ\n")

    # Đường dẫn từ src/ ra ngoài
    project_root = Path(__file__).parent.parent

    activity_file = str(project_root / "dailyActivity_merged.csv")
    sleep_file    = str(project_root / "sleepDay_merged.csv")

    activity_output = str(project_root / "result" / "dailyActivity_cleaned.csv")
    sleep_output    = str(project_root / "result" / "sleepDay_cleaned.csv")

    # 1. LÀM SẠCH DỮ LIỆU
    activity = clean_activity(activity_file, activity_output)
    sleep    = clean_sleep(sleep_file, sleep_output)

    # 2. MERGE DỮ LIỆU
    print("\n🔄 Đang merge hai bảng Activity và Sleep...")
    merged = pd.merge(
        activity,
        sleep,
        left_on=['Id', 'ActivityDate'],
        right_on=['Id', 'SleepDay'],
        how='left'
    )

    merged = merged.drop(columns=['SleepDay'], errors='ignore')
    merged.rename(columns={'ActivityDate': 'Date'}, inplace=True)

    print(f"✅ Merge hoàn tất! Tổng số dòng: {merged.shape[0]}")
    print(f"   → Số ngày không có dữ liệu ngủ: {merged['TotalMinutesAsleep'].isna().sum()}")

    # 3. KHÁM PHÁ DỮ LIỆU (EDA)
    run_eda(merged)

    # 4. TRỰC QUAN HÓA
    visualize(merged)

    # 5. MÔ HÌNH DỰ BÁO
    linear_regression(merged)
