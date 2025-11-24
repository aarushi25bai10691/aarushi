expenses = []

def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    amount = float(input("Amount: "))
    description = input("Description: ")
    expenses.append([date, category, amount, description])
    print("Expense added!")

def list_expenses():
    print("Date\t\tCategory\tAmount\tDescription")
    for e in expenses:
        print(f"{e[0]}\t{e[1]}\t{e[2]}\t{e[3]}")

# Example usage
add_expense()
list_expenses()
