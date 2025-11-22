# visualizer.py
import matplotlib.pyplot as plt

def plot_expenses(df):
    if df.empty:
        print("Nothing to plot!")
        return
    summary = df.groupby('Category')['Amount'].sum()
    summary.plot(kind='bar', title="Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()
