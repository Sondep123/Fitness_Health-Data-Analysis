import pandas as pd

def clean_activity(activity_file, output_file):
    # 1. Đọc dữ liệu
    activity = pd.read_csv(activity_file)

    # 2. Giữ lại các cột liên quan
    activity = activity[['Id', 'ActivityDate', 'TotalSteps', 'Calories', 'VeryActiveMinutes']]

    # 3. Chuẩn hóa kiểu dữ liệu ngày tháng
    activity['ActivityDate'] = pd.to_datetime(activity['ActivityDate'], format='%m/%d/%Y')

    # 4. Xử lý missing values
    activity.fillna(activity.mean(numeric_only=True), inplace=True)

    # 5. Loại bỏ dữ liệu trùng lặp
    activity.drop_duplicates(inplace=True)

    # 6. Xử lý outlier: loại bỏ bước chân = 0 bất thường
    outliers_activity = activity[(activity['TotalSteps'] == 0) & (activity['Calories'] > 2000)]
    activity = activity.drop(outliers_activity.index)

    # 7. Xuất dữ liệu sạch
    activity.to_csv(output_file, index=False)
    print(f"✅ Đã lưu dữ liệu sạch vào {output_file}")
    return activity


def clean_sleep(sleep_file, output_file):
    # 1. Đọc dữ liệu
    sleep = pd.read_csv(sleep_file)

    # 2. Giữ lại các cột liên quan
    sleep = sleep[['Id', 'SleepDay', 'TotalMinutesAsleep', 'TotalTimeInBed']]

    # 3. Chuẩn hóa kiểu dữ liệu ngày tháng
    sleep['SleepDay'] = pd.to_datetime(sleep['SleepDay'], format='%m/%d/%Y %I:%M:%S %p')

    # 4. Xử lý missing values
    sleep.fillna(sleep.mean(numeric_only=True), inplace=True)

    # 5. Loại bỏ dữ liệu trùng lặp
    sleep.drop_duplicates(inplace=True)

    # 6. Xử lý outlier: loại bỏ trường hợp ngủ > thời gian trên giường
    outliers_sleep = sleep[sleep['TotalMinutesAsleep'] > sleep['TotalTimeInBed']]
    sleep = sleep.drop(outliers_sleep.index)

    # 7. Xuất dữ liệu sạch
    sleep.to_csv(output_file, index=False)
    print(f"✅ Đã lưu dữ liệu sạch vào {output_file}")
    return sleep


if __name__ == "__main__":
    # File gốc nằm ngoài src/
    activity_file = "dailyActivity_merged.csv"
    sleep_file = "sleepDay_merged.csv"

    # File kết quả lưu vào result/
    activity_output = "result/dailyActivity_cleaned.csv"
    sleep_output = "result/sleepDay_cleaned.csv"

    # Thực hiện làm sạch
    clean_activity(activity_file, activity_output)
    clean_sleep(sleep_file, sleep_output)
