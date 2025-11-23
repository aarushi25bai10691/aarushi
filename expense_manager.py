# expense_manager.py
import pandas as pd
import os

def load_expenses(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

def save_expenses(df, filename):
    df.to_csv(filename, index=False)

def add_expense(df, date, category, amount, description):
    new_entry = {
        'Date': date,
        'Category': category,
        'Amount': amount,
        'Description': description
    }
    return df.append(new_entry, ignore_index=True)
