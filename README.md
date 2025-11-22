🚀 Project Overview

This project is a simple Python-based Budget Tracker designed to help users manage their personal finances by recording daily expenses, categorizing them, and viewing summarized reports. The application provides a menu-driven interface, and all data is saved persistently using a CSV file to ensure nothing is lost.

✨ Features

Expense Entry with Details 📝: Users can add new expenses by entering the date, category, amount, and a short description.

Category-Based Organization 🏷️: Every expense is tagged with a category, allowing the user to easily track where most of the money is being spent.

Data Persistence (CSV) 💾: All expenses are stored in a human-readable file named expenses.csv, guaranteeing data persistence across program sessions.

Automatic Summary of Expenses 📊: The system loads all records, calculates the total spending per category, and provides a clear, aggregated summary.

Graphic Visualization 📈: The project displays a bar chart (powered by Matplotlib) showing total expenses per category, helping users quickly understand their spending patterns.

Simple Menu-Driven Interface 💻: The application is easy to use and navigate, even for beginners.

🛠️ Tools & Technologies Used

Tool/Technology

Purpose

Python

The core programming language.

Pandas

Used for efficient data loading, storing, and aggregation (summarizing) from the CSV file.

Matplotlib

Used to generate the graphical bar charts for visualization.

OS Module

Used to check if the data file exists before attempting to load it.

CSV File

The storage mechanism (expenses.csv) for all expense records.

⬇️ Installation and Running

1. Install Python

Ensure Python 3.x is installed on your system.

Verify your installation by running python --version or python3 --version in your terminal.

2. Install Required Libraries

Open your command prompt or terminal.

Run the command below to install the necessary Python packages (Pandas and Matplotlib):

pip install pandas matplotlib


3. Download Project Files

Save the Python script (budget_tracker.py) to a local folder.

4. Run the Program ▶️

Navigate to the project folder in your command prompt.

Run the program by executing:

python budget_tracker.py
# OR (depending on your system setup)
python3 budget_tracker.py


📋 Using the Program

Choose 1. Add Expense to record new spending details.

Choose 2. Show Summary & Visualization to view your totals and the bar chart.

Choose 3. Exit to safely close the application.

🧪 Instructions for Testing

Verify Setup: Ensure all requirements are installed and the program starts without errors.

Test Adding Expenses: Add several expenses across different categories and confirm the success message.

Test Summary Display: Check that the calculated totals are correct and the bar chart accurately reflects the data.

Input Validation Checks ❌: Test entering an invalid category or non-numeric amount to ensure the program handles these errors gracefully and prompts the user again.

Persistence Testing ✅: Close the program and immediately re-open it. Choose 2. Show Summary—the expenses added in the previous session must be present (loaded from expenses.csv).

