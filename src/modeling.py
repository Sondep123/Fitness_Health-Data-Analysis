from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


def linear_regression(df):
    print("\n📈 ĐANG XÂY DỰNG MÔ HÌNH LINEAR REGRESSION (dự báo Calories)...")

    # Loại bỏ dòng NaN trước khi train
    model_df = df.dropna(subset=['TotalSteps', 'VeryActiveMinutes', 'Calories'])

    X = model_df[['TotalSteps', 'VeryActiveMinutes']]
    y = model_df['Calories']

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)

    print("✅ KẾT QUẢ MÔ HÌNH:")
    print(f"   MAE  = {mae:.2f} calories")
    print(f"   RMSE = {rmse:.2f} calories")
    print(f"   R²   = {r2:.4f} → Giải thích được {r2 * 100:.1f}% biến thiên của Calories")

    return model