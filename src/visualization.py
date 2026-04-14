import matplotlib.pyplot as plt
import seaborn as sns


def visualize(df):
    """Trực quan hóa dữ liệu Fitness & Sleep - Đã sửa FutureWarning"""
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (10, 6)

    print("🎨 Đang vẽ các biểu đồ...")

    # 1. Scatter: Bước chân vs Thời gian ngủ
    plt.figure()
    sns.scatterplot(data=df, x='TotalSteps', y='TotalMinutesAsleep', alpha=0.7)
    plt.title("Mối quan hệ giữa số bước chân và thời gian ngủ")
    plt.xlabel("Total Steps")
    plt.ylabel("Total Minutes Asleep (phút)")
    plt.show()

    # 2. Heatmap tương quan
    plt.figure()
    corr = df[['TotalSteps', 'Calories', 'TotalMinutesAsleep', 'TotalTimeInBed']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Ma trận tương quan giữa các biến")
    plt.show()

    # 3. Xu hướng bước chân theo thời gian
    plt.figure()
    daily_steps = df.groupby('Date')['TotalSteps'].mean().reset_index()
    sns.lineplot(data=daily_steps, x='Date', y='TotalSteps', marker='o')
    plt.title("Xu hướng trung bình số bước chân theo ngày")
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Average Total Steps")
    plt.show()

    # 4. Phân bố số bước chân
    plt.figure()
    sns.histplot(data=df, x='TotalSteps', kde=True, color='skyblue')
    plt.title("Phân bố số bước chân của người dùng")
    plt.xlabel("Total Steps")
    plt.show()

    # 5. Calories theo phút hoạt động mạnh
    plt.figure()
    sns.regplot(data=df, x='VeryActiveMinutes', y='Calories', scatter_kws={'alpha': 0.6})
    plt.title("Calories tiêu thụ theo phút hoạt động mạnh")
    plt.xlabel("Very Active Minutes")
    plt.ylabel("Calories")
    plt.show()

    # 6. Trung bình bước chân theo ngày trong tuần (ĐÃ SỬA WARNING)
    df['DayOfWeek'] = df['Date'].dt.day_name()
    order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    plt.figure()
    sns.barplot(
        data=df,
        x='DayOfWeek',
        y='TotalSteps',
        estimator='mean',
        order=order,
        palette='viridis',
        hue='DayOfWeek',  # ← Thêm dòng này để sửa warning
        legend=False  # ← Thêm dòng này
    )
    plt.title("Trung bình số bước chân theo ngày trong tuần")
    plt.xticks(rotation=45)
    plt.ylabel("Average Total Steps")
    plt.show()

    print("🎉 Đã vẽ xong tất cả 6 biểu đồ!")