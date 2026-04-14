from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def linear_regression(df):
    # Dự báo Calo dựa trên bước chân và phút hoạt động mạnh
    X = df[['TotalSteps','VeryActiveMinutes']]
    y = df['Calories']

    model = LinearRegression()
    model.fit(X, y)

    y_pred = model.predict(X)

    # Đánh giá mô hình
    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)

    print("\n📈 Linear Regression:")
    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R²:", r2)
