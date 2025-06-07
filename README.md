# Python Expense Tracker

A console-based expense tracking application written in Python 3 demonstrating Python's dynamic typing, built-in data structures, datetime module, type hints, and exception handling.

## Features

- Add expenses with date, amount, category, and description
- In-memory storage using Python lists and dictionaries
- Filter and search expenses by:
  - Date range
  - Category (case-insensitive)
- Generate expense summaries:
  - Total expenses by category
  - Overall total expenses
- Comprehensive error handling and input validation
- Formatted console output with ASCII art

## Requirements

- Python 3.x
- No external dependencies required

## How to Run/Execute the Application

### Method 1: Direct Execution
```bash
python expense_tracker.py
```

### Method 2: As a Module
```bash
python -m expense_tracker
```

### Method 3: Make Executable (Linux/Mac)
```bash
chmod +x expense_tracker.py
./expense_tracker.py
```

## Running Tests

Execute the test suite to verify functionality:

```bash
python expense_tracker_test.py
```

### Test Coverage
The test suite includes:
- **Unit Tests**: Core functionality testing (add, view, filter, summary)
- **Error Handling Tests**: Invalid date formats, empty data scenarios
- **Integration Tests**: Complete workflow testing
- **Python-Specific Feature Tests**: Dynamic typing, dictionary operations

## Language-Specific Features Demonstrated

### 1. **Dynamic Typing**
- Variables can change types at runtime
- No explicit type declarations required
- Runtime type checking and conversion

```python
# Example: amount can be int or float
amount = 15        # integer
amount = 15.99     # float - same variable, different type
```

### 2. **Built-in Data Structures**
- **Lists**: Dynamic arrays for storing expenses
- **Dictionaries**: Key-value pairs for expense data
- Automatic memory management

```python
expenses = [
    {
        'Date': '2025-05-01',
        'Amount': 15.99,
        'Category': 'Food',
        'Description': 'Lunch'
    }
]
```

### 3. **DateTime Module**
- Date parsing and validation
- Date comparisons for filtering
- Format validation

```python
from datetime import datetime
datetime.strptime(date, '%Y-%m-%d')  # Parse and validate date
```

### 4. **Type Hints**
- Enhanced code readability
- Better IDE support
- Static analysis capabilities

```python
def get_expenses(self, start_date: Optional[str] = None) -> List[Dict]:
```

### 5. **Exception Handling**
- Try-except blocks for error management
- Specific exception types
- Graceful error recovery

```python
try:
    amount = float(amount_input)
except ValueError:
    print("Error: Please enter a valid number.")
```

## Usage Instructions

### Starting the Application
1. Run the application using one of the methods above
2. The welcome banner will display
3. Main menu will appear with 4 options

### Menu Options

#### 1. Add Expense
```
Enter date (YYYY-MM-DD): 2025-05-01
Enter amount: 25.50
Enter category: Food
Enter description: Lunch at restaurant
```

#### 2. View Expenses
Choose from filtering options:
- **View all expenses**: Shows complete expense list
- **Filter by date range**:
  ```
  Enter start date (YYYY-MM-DD): 2025-05-01
  Enter end date (YYYY-MM-DD): 2025-05-31
  ```
- **Filter by category**:
  ```
  Enter category: Food
  ```

#### 3. Get Summary
Displays:
- Breakdown by category with totals
- Overall total expenses
- Formatted table output

#### 4. Exit
Closes the application gracefully

## Data Storage Structure

Expenses are stored in memory using Python's built-in data structures:

```python
expenses = [
    {
        'Date': '2025-05-01',
        'Amount': 25.50,
        'Category': 'Food',
        'Description': 'Lunch at restaurant'
    },
    {
        'Date': '2025-05-02',
        'Amount': 50.00,
        'Category': 'Transport',
        'Description': 'Gas for car'
    }
]
```

**Note**: Data is stored in memory only and will be lost when the program exits.

## Testing and Debugging

### Test Results Summary
✅ **All core functionality tested and working**:
- Expense addition with validation
- Date format validation
- Category filtering (case-insensitive)
- Date range filtering
- Summary calculations
- Error handling for invalid inputs

### Identified Issues and Status
1. **Date Validation**: ✅ **RESOLVED** - Added comprehensive date format validation
2. **Empty State Handling**: ✅ **RESOLVED** - Added user-friendly messages for empty data
3. **Case Sensitivity**: ✅ **RESOLVED** - Category filtering is now case-insensitive
4. **Memory Persistence**: ⚠️ **KNOWN LIMITATION** - Data not persisted between sessions (by design)

### Debugging Process
1. **Manual Testing**: Each feature tested with various input scenarios
2. **Automated Tests**: Unit tests cover edge cases and error conditions
3. **Error Handling**: All user inputs validated with appropriate error messages
4. **Integration Testing**: Complete workflows tested end-to-end

## Architecture Overview

### 1. **User Interface Layer**
- **Functions**: `print_banner()`, `print_expenses()`, `print_summary()`, `print_no_expenses_message()`
- **Purpose**: Handles all user interactions and formatted output
- **Features**: ASCII art, dynamic table formatting, user-friendly messages

### 2. **Business Logic Layer (ExpenseTracker Class)**
- **Methods**: `add_expense()`, `get_expenses()`, `get_summary()`
- **Purpose**: Core application logic and data validation
- **Features**: Input validation, filtering logic, summary calculations

### 3. **Data Storage Layer**
- **Structure**: Python lists containing dictionaries
- **Purpose**: In-memory data storage and retrieval
- **Features**: Dynamic data structures, automatic memory management

## Error Handling Strategy

### Input Validation
- **Date Format**: Validates YYYY-MM-DD format using datetime module
- **Amount Validation**: Ensures numeric input with proper error messages
- **Required Fields**: Validates presence of category and description

### Exception Types Handled
- `ValueError`: Invalid date formats, non-numeric amounts
- `KeyError`: Missing dictionary keys
- `KeyboardInterrupt`: Graceful handling of Ctrl+C
- `Exception`: Generic error handling for unexpected issues

### User Experience
- Clear error messages with correction instructions
- No application crashes on invalid input
- Consistent formatting for all error messages

## Performance Characteristics

- **Memory Usage**: Efficient in-memory storage using Python's optimized data structures
- **Search Performance**: Linear search for filtering (O(n) complexity)
- **Scalability**: Suitable for personal expense tracking (hundreds to thousands of entries)

## Known Limitations

1. **Data Persistence**: Data is not saved between sessions (intentional for this implementation)
2. **Concurrent Access**: Not designed for multi-user scenarios
3. **Large Dataset Performance**: Linear search may become slow with very large datasets
4. **Input Format**: Requires specific date format (YYYY-MM-DD)

## Future Enhancements for Final Deliverable

1. **File Persistence**: Add option to save/load data from files
2. **Export Functionality**: CSV export capabilities
3. **Advanced Filtering**: Multiple category selection, amount ranges
4. **Data Validation**: Enhanced validation for categories and descriptions
5. **Configuration**: User-configurable date formats and display options

## Development Information

- **Language**: Python 3.x
- **Paradigm**: Object-oriented programming with functional elements
- **Dependencies**: Standard library only (datetime, typing)
- **Test Coverage**: 8 unit tests + integration tests covering core functionality