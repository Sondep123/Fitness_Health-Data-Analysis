from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.gridspec import GridSpec

def linear_regression(df):
    print("\n📈 ĐANG XÂY DỰNG MÔ HÌNH LINEAR REGRESSION (dự báo Calories)...")

    # ===== CHUẨN BỊ DỮ LIỆU =====
    model_df = df.dropna(subset=['TotalSteps', 'VeryActiveMinutes', 'Calories'])

    X = model_df[['TotalSteps', 'VeryActiveMinutes']]
    y = model_df['Calories']

    # ===== TRAIN MODEL =====
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # ===== ĐÁNH GIÁ =====
    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)

    print("✅ KẾT QUẢ MÔ HÌNH:")
    print(f"   MAE  = {mae:.2f} calories")
    print(f"   RMSE = {rmse:.2f} calories")
    print(f"   R²   = {r2:.4f} → {r2 * 100:.1f}%")

    # ===== TẠO LAYOUT =====
    fig = plt.figure(figsize=(14, 6))
    gs = GridSpec(1, 2, width_ratios=[2.5, 1.2])

    # ================== BÊN TRÁI: BIỂU ĐỒ ==================
    ax = fig.add_subplot(gs[0])

    ax.scatter(y, y_pred, alpha=0.6, label="Dữ liệu dự đoán")
    ax.plot([y.min(), y.max()], [y.min(), y.max()],
            'r--', label="Dự đoán hoàn hảo (y = x)")

    ax.set_xlabel("Actual Calories")
    ax.set_ylabel("Predicted Calories")
    ax.set_title("Biểu đồ dự báo: Actual vs Predicted")
    ax.legend(loc='upper left', frameon=True, bbox_to_anchor=(0.02, 0.98))

    # ================== BÊN PHẢI: NHẬN XÉT ==================
    ax_text = fig.add_subplot(gs[1])
    ax_text.axis('off')

    residuals = y - y_pred
    mean_res = np.mean(residuals)
    std_res = np.std(residuals)

    # Đánh giá model
    if r2 > 0.7:
        quality = "Mô hình dự đoán tốt"
    elif r2 > 0.4:
        quality = "Mô hình ở mức trung bình"
    else:
        quality = "Mô hình còn yếu"

    bias = "Không có bias rõ rệt" if abs(mean_res) < 50 else "Có dấu hiệu bias"

    comment = (
        "NHẬN XÉT:\n\n"
        f"• {quality}\n"
        f"• {bias}\n"
        f"• Sai số trung bình: ±{std_res:.0f} calo\n\n"
       "* Các điểm gần đường đỏ → dự đoán chính xác\n"
       "* Điểm xa đường → sai số lớn"
    )

    ax_text.text(
        0.05, 0.95, comment,
        fontsize=11,
        va='top',
        ha='left',
        linespacing=1.6
    )

    # ===== TIÊU ĐỀ CHUNG =====
    plt.suptitle("Đánh giá mô hình Linear Regression",
                 fontsize=14, fontweight='bold')

    # ===== LƯU ẢNH =====
    output_dir = Path(__file__).parent.parent / "result" / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)
    save_path = output_dir / "7_prediction_final.png"

    fig.savefig(save_path, dpi=300, bbox_inches='tight')
    print("   ✅ Đã lưu: 7_prediction_final.png")

    plt.show()
    plt.close()

    return model