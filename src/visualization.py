import matplotlib.pyplot as plt
import seaborn as sns

def visualize(df):
    # Scatter plot: Bước chân vs Thời gian ngủ
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x='TotalSteps', y='TotalMinutesAsleep')
    plt.title("Mối quan hệ giữa bước chân và thời gian ngủ")
    plt.show()

    # Heatmap: Ma trận tương quan
    plt.figure(figsize=(8,6))
    sns.heatmap(df[['TotalSteps','Calories','TotalMinutesAsleep','TotalTimeInBed']].corr(), annot=True, cmap='coolwarm')
    plt.title("Ma trận tương quan giữa các biến")
    plt.show()

    # Line chart: Xu hướng bước chân theo ngày
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df, x='ActivityDate', y='TotalSteps')
    plt.title("Xu hướng số bước chân theo thời gian")
    plt.show()
