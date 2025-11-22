# main.py
from expense_manager import load_expenses, save_expenses, add_expense
from summarizer import show_summary
from visualizer import plot_expenses
from utils import validate_category

DATA_FILE = "expenses.csv"

def main():
    df = load_expenses(DATA_FILE)
    while True:
        print("\n1. Add expense\n2. Show summary\n3. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            if validate_category(category):
                try:
                    amt = float(amount)
                    df = add_expense(df, date, category, amt, description)
                    save_expenses(df, DATA_FILE)
                    print("Expense added.")
                except ValueError:
                    print("Invalid amount entered.")
        elif choice == '2':
            show_summary(df)
            plot_expenses(df)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
