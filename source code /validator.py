def save_expenses_to_file(expenses, filename="expenses.txt"):
    with open(filename, "w") as f:
        for e in expenses:
            f.write(f"{e[0]},{e[1]},{e[2]},{e[3]}\n")
    print("Expenses saved to file.")

def load_expenses_from_file(filename="expenses.txt"):
    loaded = []
    try:
        with open(filename, "r") as f:
            for line in f:
                loaded.append(line.strip().split(","))
    except FileNotFoundError:
        pass
    print("Expenses loaded from file:", loaded)
    return loaded

# Example usage
expenses = [["2025-11-23", "Food", 150, "Coffee"]]
save_expenses_to_file(expenses)
load_expenses_from_file()
