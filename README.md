 VITYARTHI PROJECT : BUDGET TRACKER
 
 PROJECT OVERVIEW : This project is a simple Python- based Budget Tracker designed to help the users manage their personal finances by recording daily expenses , categorising them and viewing summarized reportts . The application provides a menu driven interface where users can add expenses with details such as date , category , amount and description  and then generate summaries of total spending category .

Features of the project 

1 . Expense entry with details
Users can add new expense by entering the date , category , amount and short descriptions

2. Category bases organization
   Every expenses is tagged with a category so the user can see where most of the money is being spent

3. Storage using CSV
   All expenses are stored in a CSV file , so the data is not lost when the program is closed and can be resued in future sessions .

4. Automatic summary of expenses
The system can load all records and calculate the total spending per category , giving a clear summary of how much was spent in each category .

5. Graphic Visualization
The project displaus a bar chart that shows total expenses per category helping users quickly understand their spending pattern.

6 . Simple menu driven interface
The application is easy to use even for beginners . 

TOOLS / TECHNOLOGIES USED

1. Python
2.  Libraries / modules used
   i) Pandas - used to load and store the data
   ii) matplotlib - used to generate bar charts that visually show total expenses per category .
  iii) os - used to chek if the csv file exists before loading it
3. CSV file  - tp save all expense records
4. Python interpreter : to run the script

Steps to install and run the project 

1. Install Python
i) Make sure Python 3.x is installed on your system
ii) Verify installation by running python --version or python3 --version in your command prompt .

2. Install Required libraries
   i) Open command prompt
   ii) Run the commands below to install required Python packages
      ( pip install pandas matplotlib )

3 . Download Project files 
Save the python script (budget_tracker.py) to a folder on your system . 

4. Run the program
   i) Navigate to the project folder in command prompt
   ii) Run the program by executing
   (python / python3 budget_tracker.py )

5 .Using the Program
 i) Choose “Add Expense” to add new spending records with date, category, amount, and description.
 ii)Choose “Show Summary” to view total spending per category and see a bar chart.
 iii)Choose “Exit” to close the application.

6. Data Storage

i) All expenses are saved automatically to expenses.csv in the project folder.
ii) This file can be backed up or opened manually in a spreadsheet for inspection.

Instructions for testing 

1. Verify Setup
Ensure python and required libraries are installed  and the program runs without errors

2. Test Adding Expenses
 i)Launch the program.
 ii)Choose the "Add Expense" option.
iii)Enter valid inputs for date (e.g., 2025-11-22), category (choose from defined categories), amount (positive number), and description.
 iv)Verify the program confirms that the expense was added successfully.
  v)Repeat to add multiple expenses across different categories and dates.

3 . Test summary display 
i) Choose the "Show Summary " option
ii) Confirm that the total expenses by category are displayed correctly based on added data 
iii) Verify that the bar chart accurately depicts these totals.

4 . Input Validation Checks
i)Try entering an invalid category and verify that the program warns about it and does not add the expense.
ii)Test inputting invalid amount formats (e.g., letters) and check for errors or prompts

5.Persistence Testing
i)Close the program and reopen it.
ii)Show the summary without adding new expenses.
iii)Confirm previously added expenses are retained and summaries reflect all records.

6. Boundary Conditions
i)Add an expense with the minimum possible amount (like 0.01).
ii)Optionally, explore if the system handles an empty CSV gracefully when showing the summary.
