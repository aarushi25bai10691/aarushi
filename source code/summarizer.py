# summarizer.py
def show_summary(df):
    if df.empty:
        print("No expense data found.")
        return
    summary = df.groupby('Category')['Amount'].sum()
    print("Expense Summary by Category:")
    for cat, amt in summary.items():
        print(f"{cat}: {amt:.2f}")
