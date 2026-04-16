import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def visualize(df):
    output_dir = Path(__file__).parent.parent / "result" / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (10, 5)

    print("🎨 Đang vẽ và lưu các biểu đồ...")
    plots = []

    # 1. Scatter: Bước chân vs Thời gian ngủ
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='TotalSteps', y='TotalMinutesAsleep', alpha=0.7, color='blue', ax=ax)
    plt.title("Mối quan hệ giữa số bước chân và thời gian ngủ")
    plt.xlabel("Total Steps")
    plt.ylabel("Total Minutes Asleep (phút)")
    plots.append(("1_steps_vs_sleep.png", fig))

    # 2. Heatmap tương quan
    fig, ax = plt.subplots()
    corr = df[['TotalSteps', 'Calories', 'TotalMinutesAsleep', 'TotalTimeInBed', 'VeryActiveMinutes']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
    plt.title("Ma trận tương quan giữa các biến quan trọng")
    plots.append(("2_correlation_heatmap.png", fig))

    # 3. Xu hướng bước chân theo thời gian
    fig, ax = plt.subplots()
    daily_steps = df.groupby('Date')['TotalSteps'].mean().reset_index()
    sns.lineplot(data=daily_steps, x='Date', y='TotalSteps', marker='o', color='green', ax=ax)
    plt.title("Xu hướng trung bình số bước chân theo ngày")
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Average Total Steps")
    plots.append(("3_steps_trend_over_time.png", fig))

    # 4. Phân bố số bước chân
    fig, ax = plt.subplots()
    sns.histplot(data=df, x='TotalSteps', kde=True, color='skyblue', ax=ax)
    plt.title("Phân bố số bước chân của người dùng")
    plt.xlabel("Total Steps")
    plots.append(("4_steps_distribution.png", fig))

    # 5. Calories theo phút hoạt động mạnh
    fig, ax = plt.subplots()
    sns.regplot(data=df, x='VeryActiveMinutes', y='Calories',
                scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'}, ax=ax)
    plt.title("Calories tiêu thụ theo phút hoạt động mạnh")
    plt.xlabel("Very Active Minutes")
    plt.ylabel("Calories")
    plots.append(("5_calories_vs_active_minutes.png", fig))

    # 6. Trung bình bước chân theo ngày trong tuần
    df['DayOfWeek'] = df['Date'].dt.day_name()
    order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    fig, ax = plt.subplots()
    sns.barplot(
        data=df,
        x='DayOfWeek',
        y='TotalSteps',
        estimator='mean',
        order=order,
        palette='viridis',
        hue='DayOfWeek',
        legend=False,
        ax=ax
    )
    plt.title("Trung bình số bước chân theo ngày trong tuần")
    plt.xticks(rotation=45)
    plt.ylabel("Average Total Steps")
    plots.append(("6_steps_by_day_of_week.png", fig))

    # ==================== LƯU VÀ HIỂN THỊ ====================
    for filename, fig in plots:
        # Lưu file với chất lượng cao
        save_path = output_dir / filename
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"   ✅ Đã lưu: {filename}")

        # Hiển thị biểu đồ
        plt.show()
        plt.close(fig)
    print(f"   • Lưu vào thư mục: {output_dir}")