from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def linear_regression(df):
    """Mô hình hồi quy tuyến tính dự báo Calories"""
    print("\n📈 ĐANG XÂY DỰNG MÔ HÌNH LINEAR REGRESSION...")

    X = df[['TotalSteps', 'VeryActiveMinutes']]
    y = df['Calories']

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Đánh giá mô hình
    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)

    print("✅ KẾT QUẢ MÔ HÌNH:")
    print(f"   MAE  = {mae:.2f}")
    print(f"   RMSE = {rmse:.2f}")
    print(f"   R²   = {r2:.4f}  (càng gần 1 càng tốt)")
    print("   → Mô hình giải thích được {:.1f}% biến thiên của Calories".format(r2*100))