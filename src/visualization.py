import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from matplotlib.gridspec import GridSpec


def visualize(df):
    output_dir = Path(__file__).parent.parent / "result" / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (14, 8)  # Kích thước tổng thể

    print("🎨 Đang tạo biểu đồ kèm nhận xét bên phải...\n")

    # Chuẩn bị dữ liệu
    df_plot = df.copy()
    df_plot['DayOfWeek'] = df_plot['Date'].dt.day_name()

    # ==================== NHẬN XÉT MỚI DỰA TRÊN DỮ LIỆU THỰC TẾ ====================
    plots_info = [
        ("1_steps_vs_sleep.png",
         lambda ax: sns.scatterplot(data=df, x='TotalSteps', y='TotalMinutesAsleep', alpha=0.7, color='blue', ax=ax),
         "Mối quan hệ giữa số bước chân và thời gian ngủ",
         "• Không có mối tương quan rõ ràng giữa số bước chân và thời gian ngủ.\n"
         "• Đa số điểm dữ liệu tập trung ở vùng 400–550 phút ngủ (khoảng 6.5–9 giờ).\n"
         "• Một số người đi trên 15.000 bước vẫn ngủ đủ, cho thấy hoạt động nhiều không nhất thiết làm giảm giấc ngủ."),

        ("2_correlation_heatmap.png",
         lambda ax: sns.heatmap(
             df[['TotalSteps', 'Calories', 'TotalMinutesAsleep', 'TotalTimeInBed', 'VeryActiveMinutes']].corr(),
             annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax),
         "Ma trận tương quan giữa các biến",
         "• TotalSteps và Calories có tương quan dương mạnh nhất (0.60).\n"
         "• VeryActiveMinutes cũng tương quan tốt với Calories (0.61).\n"
         "• Giấc ngủ (TotalMinutesAsleep) có tương quan âm nhẹ với TotalSteps (-0.19) và gần như không liên quan đến Calories."),

        ("3_steps_trend_over_time.png",
         lambda ax: sns.lineplot(data=df.groupby('Date')['TotalSteps'].mean().reset_index(),
                                 x='Date', y='TotalSteps', marker='o', color='green', ax=ax),
         "Xu hướng số bước chân theo thời gian",
         "• Số bước chân trung bình dao động khá ổn định ở mức 7.000 – 9.000 bước/ngày trong hầu hết khoảng thời gian.\n"
         "• Có sự sụt giảm mạnh vào ngày cuối cùng (13/05/2016), có thể do dữ liệu không đầy đủ hoặc người dùng ít hoạt động."),

        ("4_steps_distribution.png",
         lambda ax: sns.histplot(data=df, x='TotalSteps', kde=True, color='skyblue', ax=ax),
         "Phân bố số bước chân của người dùng",
         "• Phân bố gần với phân phối chuẩn, tập trung chủ yếu từ 5.000 – 12.000 bước/ngày.\n"
         "• Rất nhiều ngày có dưới 2.000 bước (có thể là ngày không đeo thiết bị hoặc nghỉ ngơi).\n"
         "• Ít người đạt trên 20.000 bước/ngày."),

        ("5_calories_vs_active_minutes.png",
         lambda ax: sns.regplot(data=df, x='VeryActiveMinutes', y='Calories',
                                scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'}, ax=ax),
         "Calories tiêu thụ theo phút hoạt động mạnh",
         "• Có mối quan hệ tuyến tính dương rõ ràng: càng nhiều phút hoạt động mạnh, càng tiêu thụ nhiều calo.\n"
         "• Khi VeryActiveMinutes = 0, calo vẫn ở mức khoảng 2.000 (calo cơ bản).\n"
         "• Đây là biến có sức ảnh hưởng mạnh nhất đến lượng calo đốt cháy."),

        ("6_steps_by_day_of_week.png",
         lambda ax: sns.barplot(data=df_plot, x='DayOfWeek', y='TotalSteps', estimator='mean',
                                order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                                palette='viridis', hue='DayOfWeek', legend=False, ax=ax),
         "Trung bình số bước chân theo ngày trong tuần",
         "• Hoạt động cao nhất vào Thứ Ba và Thứ Bảy (trên 8.000 bước).\n"
         "• Thấp nhất vào Chủ Nhật (khoảng 7.200 bước).\n"
         "• Người dùng duy trì hoạt động khá đều trong tuần, "
         "không có sự chênh lệch quá lớn giữa ngày thường và cuối tuần.")
    ]

    for filename, plot_func, title, comment in plots_info:
        # Tạo figure với 2 phần: biểu đồ (trái) và text (phải)
        fig = plt.figure(figsize=(14, 8))
        gs = GridSpec(1, 2, width_ratios=[2.2, 1.0])  # Biểu đồ rộng hơn, text hẹp hơn

        # Phần 1: Biểu đồ (bên trái)
        ax = fig.add_subplot(gs[0])
        plot_func(ax)
        ax.set_title(title, fontsize=14, pad=15)

        if 'trend' in filename or 'Date' in str(plot_func):
            plt.xticks(rotation=45)

        # Phần 2: Nhận xét (bên phải)
        ax_text = fig.add_subplot(gs[1])
        ax_text.axis('off')  # Tắt trục

        ax_text.text(0.05, 0.95, "NHẬN XÉT:", fontsize=13, fontweight='bold',
                     va='top', ha='left', transform=ax_text.transAxes, color='darkblue')

        ax_text.text(0.05, 0.85, comment, fontsize=11, va='top', ha='left',
                     transform=ax_text.transAxes, linespacing=1.6)

        plt.suptitle(f"Biểu đồ {filename.split('_', 1)[1].replace('.png', '').replace('_', ' ').title()}",
                     fontsize=16, y=0.98, fontweight='bold')

        # Lưu file
        save_path = output_dir / filename
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"   ✅ Đã lưu: {filename}")

        # Hiển thị biểu đồ
        plt.show()
        plt.close(fig)

    print(f"\n🎉 Hoàn thành! Tất cả biểu đồ kèm nhận xét đã được lưu vào:\n   {output_dir}")