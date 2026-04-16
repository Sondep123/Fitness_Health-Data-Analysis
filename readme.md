# Fitness & Health Data Analysis  
**Phân tích mối quan hệ giữa hoạt động thể chất và giấc ngủ**

Dự án thực hiện phân tích dữ liệu Fitness & Sleep từ bộ dữ liệu FitBit, 
tập trung vào việc khám phá mối quan hệ giữa hoạt động hàng ngày (số bước chân, calories, thời gian hoạt động mạnh) và chất lượng giấc ngủ.

## 1 Giới thiệu
Dự án nhằm làm sạch, phân tích và mô hình hóa dữ liệu từ hai tập dữ liệu chính:
- `dailyActivity_merged.csv`: dữ liệu hoạt động hàng ngày
- `sleepDay_merged.csv`: dữ liệu giấc ngủ
Mục tiêu chính là hiểu rõ cách hoạt động thể chất ảnh hưởng đến thời gian ngủ,
đồng thời xây dựng mô hình dự báo lượng calories tiêu thụ dựa trên các chỉ số hoạt động.

## 2 Mục tiêu dự án
- Làm sạch và chuẩn hóa hai bộ dữ liệu Activity & Sleep.
- Merge dữ liệu theo `Id` và ngày.
- Phân tích khám phá dữ liệu (EDA).
- Trực quan hóa mối quan hệ giữa các biến quan trọng.
- Xây dựng mô hình hồi quy tuyến tính dự báo **Calories**.
- Đánh giá mô hình bằng MAE, RMSE và R².

## 3 Dataset
- **dailyActivity_merged.csv**: Chứa thông tin hoạt động hàng ngày (TotalSteps, Calories, VeryActiveMinutes, …)
- **sleepDay_merged.csv**: Chứa thông tin giấc ngủ (TotalMinutesAsleep, TotalTimeInBed, …)
- Số người dùng: Nhiều Id khác nhau
- Số dòng dữ liệu trong dailyActivity_merged.csv: 940
- Số cột ban đầu:15
- Số dòng dữ liệu trong sleepDay_merged_csv: 460
- Số cột ban đầu: 5
- Biến mục tiêu chính trong mô hình: **Calories**
- Các biến quan trọng khác: TotalSteps, VeryActiveMinutes, TotalMinutesAsleep, TotalTimeInBed

## 4 Quy trình thực hiện

### bước 1: Làm sạch dữ liệu (`clean.py`)
- Chuẩn hóa định dạng ngày tháng (`ActivityDate` và `SleepDay`).
- Xử lý giá trị thiếu bằng mean của các cột số.
- Loại bỏ dữ liệu trùng lặp.
- Xử lý outlier:
  - Loại bỏ trường hợp TotalSteps = 0 nhưng Calories > 2000.
  - Loại bỏ trường hợp TotalMinutesAsleep > TotalTimeInBed.
- Lưu kết quả vào thư mục `result/`:
  - `dailyActivity_cleaned.csv`
  - `sleepDay_cleaned.csv`

### bước 2. Merge dữ liệu
- Merge hai bảng theo `Id` và ngày (`ActivityDate` ↔ `SleepDay`).
- Sử dụng Left Join để giữ toàn bộ dữ liệu hoạt động.
- Đổi tên cột thành `Date` thống nhất.

### bước 3. Phân tích khám phá dữ liệu (EDA)
- Thống kê mô tả (describe) cho các biến chính.
- Tính ma trận tương quan giữa TotalSteps, Calories, TotalMinutesAsleep, TotalTimeInBed.
- Kiểm tra số lượng ngày có/ không có dữ liệu giấc ngủ.

### bước 4. Trực quan hóa (`visualization.py`)
Dự án tạo ra 6 biểu đồ chính:
- Scatter plot: TotalSteps vs TotalMinutesAsleep
- Heatmap tương quan giữa các biến
- Line plot: Xu hướng số bước chân theo thời gian
- Histogram: Phân bố số bước chân
- Regplot: Calories theo VeryActiveMinutes
- Barplot: Trung bình bước chân theo ngày trong tuần

### bước 5. Xây dựng mô hình (`modeling.py`)
- Mô hình: **Linear Regression**
- Features: `TotalSteps`, `VeryActiveMinutes`
- Target: `Calories`
- Đánh giá mô hình bằng: MAE, RMSE, R² Score

### bước 6. Entry point
Toàn bộ quy trình được chạy thống nhất qua file **`main.py`**.
- Tổng số dòng: 922
- Số ngày không có dữ liệu ngủ: 512
- Số ngày có dữ liệu ngủ: 410
**Ý nghĩa:**
- MAE = 434.37 cho biết sai số trung bình giữa lượng Calories dự đoán và Calories thực tế là khoảng **434 calories**.
- RMSE = 541.32 lớn hơn MAE vì nhạy cảm hơn với các dự đoán sai lớn. 
- Mô hình có độ chính xác chấp nhận được với dữ liệu fitness, giúp dự báo khá tốt lượng năng lượng tiêu thụ dựa trên số bước chân và thời gian hoạt động mạnh.

## 5. Giải thích chi tiết các file trong project
### 1. File dữ liệu
- dailyActivity_merged.csv: Bộ dữ liệu gốc chứa thông tin hoạt động thể chất hàng ngày (TotalSteps, Calories, VeryActiveMinutes, …). Đây là một trong hai file dữ liệu chính của dự án.
- sleepDay_merged.csv: Bộ dữ liệu gốc chứa thông tin giấc ngủ (TotalMinutesAsleep, TotalTimeInBed, …). Đây là file dữ liệu thứ hai quan trọng của dự án.
- dailyActivity_cleaned.csv: Dữ liệu hoạt động đã được làm sạch bởi clean.py, được lưu trong thư mục result/.
- sleepDay_cleaned.csv: Dữ liệu giấc ngủ đã được làm sạch bởi clean.py, được lưu trong thư mục result/.

### 2. File mã nguồn
- src/main.py: File chạy chính (entrypoint) của toàn bộ dự án. File này điều phối thứ tự thực hiện toàn bộ quy trình: làm sạch dữ liệu → merge dữ liệu → EDA → trực quan hóa → xây dựng mô hình.
- src/clean.py: Script làm sạch dữ liệu. Chứa hai hàm chính clean_activity() và clean_sleep(). Thực hiện chuẩn hóa định dạng ngày tháng, xử lý giá trị thiếu, loại bỏ dữ liệu trùng lặp và xử lý outlier.
- src/eda.py: Chứa hàm run_eda() thực hiện phân tích khám phá dữ liệu (EDA), in ra thống kê mô tả và ma trận tương quan giữa các biến.
- src/visualization.py: Chứa hàm visualize() dùng để vẽ và lưu 6 biểu đồ trực quan (scatter plot, heatmap, line plot, histogram, regplot và barplot theo ngày trong tuần).
- src/modeling.py: Chứa hàm linear_regression() xây dựng mô hình Linear Regression dự báo Calories từ TotalSteps và VeryActiveMinutes, đồng thời tính các chỉ số đánh giá MAE, RMSE, R².
- readme.md: Tài liệu mô tả dự án, bao gồm giới thiệu, quy trình thực hiện, cách chạy chương trình và giải thích chi tiết các file.

### 3. File kết quả trong thư mục result/
- result/dailyActivity_cleaned.csv: Dữ liệu hoạt động sau khi làm sạch.
- result/sleepDay_cleaned.csv: Dữ liệu giấc ngủ sau khi làm sạch.
- result/figures/: Thư mục chứa 6 biểu đồ được xuất ra khi chạy chương trình:
  + 1_steps_vs_sleep.png
  + 2_correlation_heatmap.png
  + 3_steps_trend_over_time.png
  + 4_steps_distribution.png
  + 5_calories_vs_active_minutes.png
  + 6_steps_by_day_of_week.png

## 6 Cấu trúc thư mục dự án
Fitness_Health Data Analy/
├── src/
│   ├── clean.py
│   ├── eda.py
│   ├── main.py
│   ├── modeling.py
│   └── visualization.py
├── result/
│   ├── dailyActivity_cleaned.csv
│   ├── sleepDay_cleaned.csv
│   └── figures/
│       ├── 1_steps_vs_sleep.png
│       ├── 2_correlation_heatmap.png
│       ├── 3_steps_trend_over_time.png
│       ├── 4_steps_distribution.png
│       ├── 5_calories_vs_active_minutes.png
│       └── 6_steps_by_day_of_week.png
├── dailyActivity_merged.csv
├── sleepDay_merged.csv
└── readme.md

## 7 Chạy toàn bộ dự án
 - python main.py

## 8 Kết luận
Project đã hoàn thành tốt các yêu cầu chính của đề bài:
- Có xử lý dữ liệu thiếu và outlier một cách hợp lý theo ngữ cảnh dữ liệu sức khỏe.
- Có merge hai bảng dữ liệu Activity và Sleep một cách chính xác.
- Có thực hiện phân tích mối quan hệ giữa hoạt động thể chất (số bước chân, calories, thời gian hoạt động mạnh) và giấc ngủ.
- Có trực quan hóa dữ liệu bằng 6 biểu đồ đa dạng (scatter plot, heatmap, line plot, histogram, regplot và barplot).
- Có xây dựng mô hình hồi quy tuyến tính dự báo lượng Calories tiêu thụ.
- Có đánh giá mô hình bằng các chỉ số MAE, RMSE và R².
- Mô hình Linear Regression hiện tại là một baseline tốt, với MAE = 434.37 và RMSE = 541.32. Kết quả cho thấy mô hình có khả năng dự báo khá ổn định lượng calories dựa trên số bước chân và thời gian hoạt động mạnh.

## 9 Thành viên làm dự án
- Nguyễn Lam Sơn - 20221628

