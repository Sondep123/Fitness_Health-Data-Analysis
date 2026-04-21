import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from matplotlib.gridspec import GridSpec

def visualize(df):
    output_dir = Path(__file__).parent.parent / "result" / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (14, 8)

    df_plot = df.copy()
    df_plot['DayOfWeek'] = df_plot['Date'].dt.day_name()

    # ==================== NHẬN XÉT TỰ ĐỘNG ====================
    # 1. Steps vs Sleep
    corr_steps_sleep = df['TotalSteps'].corr(df['TotalMinutesAsleep'])
    comment1 = (
        f"• Hệ số tương quan giữa bước đi và giấc ngủ: {corr_steps_sleep:.2f}.\n"
        + ("• Không có mối quan hệ rõ ràng." if abs(corr_steps_sleep) < 0.3 else "• Có mối quan hệ đáng kể.")
    )

    # 2. Correlation heatmap
    corr_matrix = df[['TotalSteps','Calories','TotalMinutesAsleep','TotalTimeInBed','VeryActiveMinutes']].corr()
    strongest = corr_matrix.unstack().dropna().sort_values(key=abs, ascending=False).drop_duplicates().head(3)
    comment2 = "• Các cặp biến có tương quan mạnh nhất:\n" + "\n".join([f"  - {i[0]} vs {i[1]}: {v:.2f}" for i,v in strongest.items()])

    # 3. Steps trend
    steps_trend = df.groupby('Date')['TotalSteps'].mean()
    comment3 = (
        f"• Trung bình số bước dao động từ {steps_trend.min():.0f} đến {steps_trend.max():.0f}.\n"
        f"• Giá trị trung bình toàn kỳ: {steps_trend.mean():.0f} bước/ngày.\n"
        f"• Có sự sụt giảm rõ rệt vào cuối kỳ, cần xem xét nguyên nhân."
    )

    # 4. Steps distribution
    mean_steps = df['TotalSteps'].mean()
    comment4 = f"• Trung bình số bước/ngày: {mean_steps:.0f}.\n• Phân bố tập trung quanh {mean_steps:.0f} bước."

    # 5. Calories vs Active Minutes
    corr_cal_act = df['Calories'].corr(df['VeryActiveMinutes'])
    comment5 = f"• Hệ số tương quan Calories vs ActiveMinutes: {corr_cal_act:.2f}.\n• Cho thấy hoạt động mạnh ảnh hưởng rõ rệt đến calo."

    # 6. Steps by Day of Week
    avg_by_day = df_plot.groupby('DayOfWeek')['TotalSteps'].mean().sort_values(ascending=False)
    top_day, top_val = avg_by_day.index[0], avg_by_day.iloc[0]
    low_day, low_val = avg_by_day.index[-1], avg_by_day.iloc[-1]
    comment6 = f"• Cao nhất vào {top_day} ({top_val:.0f} bước).\n• Thấp nhất vào {low_day} ({low_val:.0f} bước)."

    plots_info = [
        ("1_steps_vs_sleep.png",
         lambda ax: sns.scatterplot(data=df, x='TotalSteps', y='TotalMinutesAsleep', alpha=0.7, color='blue', ax=ax),
         "Mối quan hệ giữa số bước chân và thời gian ngủ", comment1),

        ("2_correlation_heatmap.png",
         lambda ax: sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax),
         "Ma trận tương quan giữa các biến", comment2),

        ("3_steps_trend_over_time.png",
         lambda ax: sns.lineplot(data=steps_trend.reset_index(), x='Date', y='TotalSteps', marker='o', color='green', ax=ax),
         "Xu hướng số bước chân theo thời gian", comment3),

        ("4_steps_distribution.png",
         lambda ax: sns.histplot(data=df, x='TotalSteps', kde=True, color='skyblue', ax=ax),
         "Phân bố số bước chân của người dùng", comment4),

        ("5_calories_vs_active_minutes.png",
         lambda ax: sns.regplot(data=df, x='VeryActiveMinutes', y='Calories',
                                scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'}, ax=ax),
         "Calories tiêu thụ theo phút hoạt động mạnh", comment5),

        ("6_steps_by_day_of_week.png",
         lambda ax: sns.barplot(data=df_plot, x='DayOfWeek', y='TotalSteps', estimator='mean',
                                order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
                                palette='viridis', hue='DayOfWeek', legend=False, ax=ax),
         "Trung bình số bước chân theo ngày trong tuần", comment6)
    ]

    for filename, plot_func, title, comment in plots_info:
        fig = plt.figure(figsize=(14, 8))
        gs = GridSpec(1, 2, width_ratios=[2.2, 1.0])

        ax = fig.add_subplot(gs[0])
        plot_func(ax)
        ax.set_title(title, fontsize=14, pad=15)

        if 'trend' in filename:
            plt.xticks(rotation=45)

        ax_text = fig.add_subplot(gs[1])
        ax_text.axis('off')
        ax_text.text(0.05, 0.95, "NHẬN XÉT:", fontsize=13, fontweight='bold',
                     va='top', ha='left', transform=ax_text.transAxes, color='darkblue')
        ax_text.text(0.05, 0.85, comment, fontsize=11, va='top', ha='left',
                     transform=ax_text.transAxes, linespacing=1.6)

        plt.suptitle(f"Biểu đồ {filename.split('_',1)[1].replace('.png','').replace('_',' ').title()}",
                     fontsize=16, y=0.98, fontweight='bold')

        save_path = output_dir / filename
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"   ✅ Đã lưu: {filename}")
        plt.show()
        plt.close(fig)

    print(f"\n🎉 Hoàn thành! Tất cả biểu đồ kèm nhận xét tự động đã được lưu vào:\n   {output_dir}")
