Dự án này nhằm phân tích dữ liệu hoạt động thể chất và giấc ngủ của người dùng từ Fitbit. 
Các bước bao gồm làm sạch dữ liệu, khám phá dữ liệu (EDA), trực quan hóa,
và xây dựng mô hình hồi quy tuyến tính để dự báo lượng Calories tiêu thụ.

Nguồn dữ liệu
Bộ dữ liệu được tham khảo và tải về từ Kaggle: Fitbit Fitness Tracker Data.
Link tham khảo: Kaggle Dataset "Fitbit Fitness Tracker Data" (kaggle.com/datasets/arashnic/fitbit).

Cấu trúc dự án

project_root/
│
├── dailyActivity_merged.csv   # Dữ liệu thô về hoạt động (từ Kaggle)
├── sleepDay_merged.csv        # Dữ liệu thô về giấc ngủ (từ Kaggle)
├── result/                    # Thư mục chứa dữ liệu sạch
│   ├── dailyActivity_cleaned.csv
│   └── sleepDay_cleaned.csv
├── src/
│   ├── clean.py               # Hàm làm sạch dữ liệu
│   ├── eda.py                 # Khám phá dữ liệu
│   ├── visualization.py       # Trực quan hóa dữ liệu
│   ├── modeling.py            # Mô hình hồi quy tuyến tính
│   └── main.py                # Chạy toàn bộ pipeline

Các bước thực hiện:

1. Làm sạch dữ liệu (clean.py)
Activity:
Giữ các cột quan trọng: Id, ActivityDate, TotalSteps, Calories, VeryActiveMinutes.
Chuẩn hóa ngày tháng.
Xử lý missing values bằng trung bình.
Loại bỏ trùng lặp.
Loại bỏ outlier: trường hợp bước chân = 0 nhưng Calories > 2000.
Sleep:
Giữ các cột: Id, SleepDay, TotalMinutesAsleep, TotalTimeInBed.
Chuẩn hóa ngày tháng.
Xử lý missing values bằng trung bình.
Loại bỏ trùng lặp.
Loại bỏ outlier: khi TotalMinutesAsleep > TotalTimeInBed.

2. Merge dữ liệu (main.py)
Merge bảng Activity và Sleep theo Id và ngày.
Đổi tên cột ActivityDate thành Date.
Kiểm tra số ngày không có dữ liệu ngủ.

3. Khám phá dữ liệu (EDA - eda.py)
Thống kê mô tả các biến chính.
Tính ma trận tương quan.
Đếm số ngày có dữ liệu giấc ngủ.

4. Trực quan hóa (visualization.py)
Scatter plot: số bước chân vs thời gian ngủ.
Heatmap: ma trận tương quan.
Line plot: xu hướng bước chân theo ngày.
Histogram: phân bố số bước chân.
Regplot: Calories vs phút hoạt động mạnh.
Barplot: trung bình bước chân theo ngày trong tuần.

5. Mô hình hồi quy tuyến tính (modeling.py)
Biến đầu vào: TotalSteps, VeryActiveMinutes.
Biến mục tiêu: Calories.
Huấn luyện mô hình Linear Regression.
Đánh giá bằng MAE, RMSE, R².
In kết quả và mức độ giải thích biến thiên Calories.

Kết quả:
Dữ liệu sạch được lưu trong thư mục result/.
Các biểu đồ trực quan giúp hiểu rõ mối quan hệ giữa hoạt động và giấc ngủ.
Mô hình hồi quy tuyến tính cho thấy khả năng dự báo Calories dựa trên bước chân và phút hoạt động mạnh.

Hướng dẫn chạy
Tải dữ liệu từ Kaggle và đặt file (dailyActivity_merged.csv, sleepDay_merged.csv) vào thư mục gốc.

Chạy file main.py

Kết quả sẽ hiển thị trên màn hình và lưu dữ liệu sạch vào thư mục result/.

Ghi chú
Mã nguồn được viết bằng Python, sử dụng các thư viện: pandas, numpy, matplotlib, seaborn, scikit-learn.