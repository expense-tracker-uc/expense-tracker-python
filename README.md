# Python Expense Tracker

A simple console-based expense tracking application written in Python 3. This application helps you track your daily expenses, categorize them, and generate summaries.

## Features

- Add expenses with date, amount, category, and description
- In-memory storage using Python dictionaries
- Filter and search expenses by:
  - Date range
  - Category
- Generate expense summaries:
  - Total expenses by category
  - Overall total expenses

## Requirements

- Python 3.x
- No external dependencies required

## Usage

1. Run the application:
   ```bash
   python expense_tracker.py
   ```

2. Follow the menu options:
   - Option 1: Add a new expense
   - Option 2: View expenses (with filtering options)
   - Option 3: Get expense summary
   - Option 4: Exit the application

## Data Storage

Expenses are stored in memory using a list of dictionaries. Each expense entry contains:
- Date (YYYY-MM-DD format)
- Amount
- Category
- Description

Note: Since the data is stored in memory, all expenses will be cleared when the program exits.

## Example Usage

1. Adding an expense:
   ```
   Enter date (YYYY-MM-DD): 2024-03-20
   Enter amount: 25.50
   Enter category: Groceries
   Enter description: Weekly groceries
   ```

2. Viewing expenses:
   - View all expenses
   - Filter by date range
   - Filter by category

3. Getting summary:
   - Shows total expenses by category
   - Shows overall total expenses

## Error Handling

The application includes error handling for:
- Invalid date formats
- Invalid user inputs
