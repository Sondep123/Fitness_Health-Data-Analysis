import pandas as pd
from clean import clean_activity, clean_sleep
from eda import run_eda
from visualization import visualize
from modeling import linear_regression

activity_file = "../dailyActivity_merged.csv"
sleep_file = "../sleepDay_merged.csv"

# 1. Làm sạch dữ liệu
activity = clean_activity(activity_file, "../result/dailyActivity_cleaned.csv")
sleep = clean_sleep(sleep_file, "../result/sleepDay_cleaned.csv")

# Merge dữ liệu
merged = pd.merge(activity, sleep, left_on=['Id','ActivityDate'], right_on=['Id','SleepDay'], how='inner')

# 2. Khám phá dữ liệu
run_eda(merged)

# 3. Trực quan hóa
visualize(merged)

# 4. Mô hình dự báo
linear_regression(merged)
