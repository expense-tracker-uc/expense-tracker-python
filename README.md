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

### Components

1. **User Interface Layer**
   - Handles all user interactions
   - Provides formatted output
   - Implements the main menu system
   - Functions:
     - `print_banner()`: Displays welcome message
     - `print_expenses()`: Formats expense display
     - `print_summary()`: Formats summary display
     - `print_no_expenses_message()`: Handles empty state

2. **Business Logic Layer (ExpenseTracker Class)**
   - Core application logic
   - Data validation
   - Expense management
   - Methods:
     - `add_expense()`: Validates and adds new expenses
     - `get_expenses()`: Retrieves and filters expenses
     - `get_summary()`: Generates expense summaries

3. **Data Storage Layer**
   - In-memory storage using Python list and dictionaries
   - Simple and efficient for this application
   - Structure:
     ```python
     expenses = [
         {
             'Date': '2024-03-20',
             'Amount': 25.50,
             'Category': 'Groceries',
             'Description': 'Weekly groceries'
         }
     ]
     ```

### Design Patterns

1. **Single Responsibility Principle**
   - Each component has a specific, well-defined purpose
   - UI functions handle display only
   - ExpenseTracker class manages business logic
   - Data storage is separate from business logic

2. **Command Pattern**
   - Menu options map to specific actions
   - Each action is encapsulated in its own method
   - Easy to extend with new commands

3. **Data Transfer Objects (DTOs)**
   - Expenses are represented as dictionaries
   - Consistent data structure throughout the application
   - Easy to serialize/deserialize if needed

### Error Handling Strategy

1. **Input Validation**
   - Date format validation
   - Amount type checking
   - Category and description presence

2. **Graceful Degradation**
   - User-friendly error messages
   - Clear instructions for correction
   - No application crashes

3. **Empty State Handling**
   - Dedicated message for no expenses
   - Clear user guidance
   - Consistent formatting

### Future Extensibility

The architecture allows for easy extension in several ways:

1. **Storage Layer**
   - Could be extended to use databases
   - File-based storage could be added
   - Multiple storage backends could be supported

2. **Business Logic**
   - Additional expense types could be added
   - More complex filtering could be implemented
   - Budget tracking could be added

3. **User Interface**
   - Could be extended to a GUI
   - Web interface could be added
   - API endpoints could be exposed
