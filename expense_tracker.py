# ===================================================================
# MSCS 632 Advanced Programming Languages
# Group Project - Expense Tracker Application
# Python Implementation
# ===================================================================
# Demonstrates Python's dynamic typing, built-in data structures,
# datetime module, type hints, and exception handling

from datetime import datetime
from typing import List, Dict, Optional

# ===================================================================
# UTILITY FUNCTIONS FOR USER INTERFACE
# ===================================================================

def print_banner():
    """
    Displays the ASCII art banner and welcome message for the application.
    Uses Python's triple-quoted strings for multi-line string literals.
    """
    banner = """
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $                                                                              $
    $  EEEEE  X   X  PPPPP   EEEEE  N   N   SSSS   EEEEE                           $
    $  E       X X   P    P  E      NN  N  S       E                               $
    $  EEEE     X    PPPPP   EEEE   N N N   SSS    EEEE                            $
    $  E       X X   P       E      N  NN      S   E                               $
    $  EEEEE  X   X  P       EEEEE  N   N  SSSS    EEEEE                           $
    $                                                                              $
    $  TTTTT  RRRR    A    CCC   K   K  EEEEE  RRRR                                $
    $    T    R   R  A A   C     K  K   E      R   R                               $
    $    T    RRRR  AAAAA  C     KKK    EEEE   RRRR                                $
    $    T    R  R  A   A  C     K  K   E      R  R                                $
    $    T    R   R A   A   CCC  K   K  EEEEE  R   R                               $
    $                                                                              $
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """
    print(banner)
    print("Welcome to your personal expense tracking system!")
    print("=" * 60)

def print_no_expenses_message():
    """
    Print a formatted message when no expenses are found.
    Demonstrates Python's docstring conventions and Unicode box drawing characters.
    """
    message = """
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║                                                                            ║
    ║                        No Expenses Found!                                  ║
    ║                                                                            ║
    ║  You haven't recorded any expenses yet.                                    ║
    ║  Use option 1 from the main menu to add your first expense.                ║
    ║                                                                            ║
    ╚════════════════════════════════════════════════════════════════════════════╝
    """
    print(message)

def print_summary(summary: Dict):
    """
    Print a formatted summary of expenses by category.

    Args:
        summary (Dict): Dictionary containing 'categories' and 'total' keys
                       where 'categories' maps category names to amounts

    Demonstrates:
    - Python's type hints
    - Dictionary operations and comprehensions
    - String formatting with f-strings
    - Dynamic formatting based on content length
    """
    # Check if there are any expenses to display
    if not summary['categories']:
        print_no_expenses_message()
        return

    # Calculate dynamic column width based on longest category name
    # Demonstrates Python's generator expressions and built-in functions
    max_category_length = max(len(cat) for cat in summary['categories'].keys()) if summary['categories'] else 0
    max_category_length = max(max_category_length, len("Category"))

    # Print formatted header using f-string centering
    print("\n" + "=" * (max_category_length + 20))
    print(f"{'EXPENSE SUMMARY':^{max_category_length + 20}}")
    print("=" * (max_category_length + 20))

    # Print category breakdown section
    print("\nCategory Breakdown:")
    print("-" * (max_category_length + 20))
    print(f"{'Category':<{max_category_length}} | {'Amount':>10}")
    print("-" * (max_category_length + 20))

    # Sort categories by amount in descending order
    # Demonstrates Python's sorted() function with lambda key function
    sorted_categories = sorted(summary['categories'].items(),
                             key=lambda x: x[1],  # Sort by amount (second element)
                             reverse=True)

    # Print each category with proper alignment
    # Demonstrates f-string formatting with alignment and precision
    for category, amount in sorted_categories:
        print(f"{category:<{max_category_length}} | ${amount:>9.2f}")

    # Print total with visual separation
    print("-" * (max_category_length + 20))
    print(f"{'TOTAL':<{max_category_length}} | ${summary['total']:>9.2f}")
    print("=" * (max_category_length + 20))

def print_expenses(expenses: List[Dict]):
    """
    Print a formatted table of expenses.

    Args:
        expenses (List[Dict]): List of expense dictionaries with keys:
                              'Date', 'Amount', 'Category', 'Description'

    Demonstrates:
    - List comprehensions for calculating column widths
    - Dynamic table formatting
    - String formatting and alignment
    - Error handling for missing data
    """
    # Check if there are expenses to display
    if not expenses:
        print_no_expenses_message()
        return

    # Calculate optimal column widths based on content
    # Demonstrates Python's list comprehensions and max() function
    date_width = 12  # Fixed width for YYYY-MM-DD format
    amount_width = 10

    # Dynamic width calculation for category column
    category_width = max(len(exp['Category']) for exp in expenses)
    category_width = max(category_width, len("Category"))

    # Dynamic width calculation for description column
    desc_width = max(len(exp['Description']) for exp in expenses)
    desc_width = max(desc_width, len("Description"))

    # Calculate total table width including separators
    total_width = date_width + amount_width + category_width + desc_width + 9  # 9 for separators and spaces

    # Print table header with centered title
    print("\n" + "=" * total_width)
    print(f"{'EXPENSE LIST':^{total_width}}")
    print("=" * total_width)

    # Print column headers with proper alignment
    print(f"{'Date':<{date_width}} | {'Amount':>{amount_width}} | {'Category':<{category_width}} | {'Description':<{desc_width}}")
    print("-" * total_width)

    # Print each expense row
    # Demonstrates string formatting, type conversion, and error handling
    for expense in expenses:
        print(f"{expense['Date']:<{date_width}} | ${float(expense['Amount']):>{amount_width-1}.2f} | "
              f"{expense['Category']:<{category_width}} | {expense['Description']:<{desc_width}}")

    # Print table footer with count
    print("=" * total_width)
    print(f"Total Expenses: {len(expenses)}")
    print("=" * total_width)

# ===================================================================
# MAIN EXPENSE TRACKER CLASS
# ===================================================================

class ExpenseTracker:
    """
    Main class for managing expense data and operations.

    Demonstrates:
    - Object-oriented programming in Python
    - Type hints for class attributes and methods
    - Instance variable initialization
    - Method organization and encapsulation

    Attributes:
        expenses (List[Dict]): List storing all expense records as dictionaries
    """

    def __init__(self):
        """
        Initialize the ExpenseTracker with an empty list of expenses.

        Demonstrates:
        - Constructor method in Python
        - Type-hinted instance variable
        - Python's dynamic list initialization
        """
        self.expenses: List[Dict] = []

    def add_expense(self, date: str, amount: float, category: str, description: str):
        """
        Add a new expense to the tracker with validation.

        Args:
            date (str): Date in YYYY-MM-DD format
            amount (float): Expense amount (must be positive)
            category (str): Expense category
            description (str): Expense description

        Demonstrates:
        - Method parameter type hints
        - Exception handling with try-except blocks
        - datetime module for date validation
        - Dictionary creation and list manipulation
        - Python's automatic memory management
        """
        try:
            # Validate date format using datetime.strptime()
            # Demonstrates Python's datetime module for date parsing
            datetime.strptime(date, '%Y-%m-%d')

            # Create expense dictionary
            # Demonstrates Python's dictionary literals and dynamic typing
            expense = {
                'Date': date,
                'Amount': amount,
                'Category': category,
                'Description': description
            }

            # Add to expenses list
            # Demonstrates Python's list append() method
            self.expenses.append(expense)
            print("Expense added successfully!")

        except ValueError:
            # Handle invalid date format
            # Demonstrates specific exception handling
            print("Error: Invalid date format. Please use YYYY-MM-DD format.")
        except Exception as e:
            # Handle any other unexpected errors
            # Demonstrates generic exception handling with error message
            print(f"Error adding expense: {str(e)}")

    def get_expenses(self, start_date: Optional[str] = None,
                    end_date: Optional[str] = None,
                    category: Optional[str] = None) -> List[Dict]:
        """
        Get expenses filtered by date range and/or category.

        Args:
            start_date (Optional[str]): Start date filter (YYYY-MM-DD)
            end_date (Optional[str]): End date filter (YYYY-MM-DD)
            category (Optional[str]): Category filter (case-insensitive)

        Returns:
            List[Dict]: Filtered list of expense dictionaries

        Demonstrates:
        - Optional parameters with default None values
        - Type hints with Optional type
        - List filtering with conditional logic
        - Date comparison using datetime objects
        - Case-insensitive string comparison
        - Exception handling within loops
        """
        filtered_expenses = []

        # Iterate through all expenses
        # Demonstrates Python's for loop and list iteration
        for expense in self.expenses:
            try:
                # Parse expense date for comparison
                # Demonstrates datetime object creation and comparison
                expense_date = datetime.strptime(expense['Date'], '%Y-%m-%d')

                # Apply start date filter if provided
                if start_date:
                    start = datetime.strptime(start_date, '%Y-%m-%d')
                    if expense_date < start:
                        continue  # Skip this expense

                # Apply end date filter if provided
                if end_date:
                    end = datetime.strptime(end_date, '%Y-%m-%d')
                    if expense_date > end:
                        continue  # Skip this expense

                # Apply category filter if provided (case-insensitive)
                # Demonstrates string method chaining and comparison
                if category and expense['Category'].lower() != category.lower():
                    continue  # Skip this expense

                # If all filters pass, add to results
                filtered_expenses.append(expense)

            except ValueError:
                # Handle invalid date in stored expense
                # Demonstrates error handling with .get() method for safe dictionary access
                print(f"Warning: Skipping expense with invalid date: {expense.get('Date', 'Unknown')}")
                continue

        return filtered_expenses

    def get_summary(self) -> Dict:
        """
        Generate summary of expenses by category and calculate total.

        Returns:
            Dict: Summary containing 'categories' dict and 'total' float

        Demonstrates:
        - Dictionary initialization and manipulation
        - Nested dictionary operations
        - Type conversion and validation
        - Accumulator pattern for calculations
        - Exception handling for data integrity
        """
        # Initialize summary structure
        # Demonstrates nested dictionary initialization
        summary = {'categories': {}, 'total': 0}

        # Process each expense
        for expense in self.expenses:
            try:
                # Extract and validate amount
                # Demonstrates type conversion and error handling
                amount = float(expense['Amount'])
                category = expense['Category']

                # Update category total
                # Demonstrates dictionary key checking and accumulation
                if category not in summary['categories']:
                    summary['categories'][category] = 0
                summary['categories'][category] += amount

                # Update overall total
                summary['total'] += amount

            except (ValueError, KeyError):
                # Handle invalid expense data
                # Demonstrates multiple exception types in one except block
                print(f"Warning: Skipping invalid expense entry")
                continue

        return summary

# ===================================================================
# MAIN PROGRAM EXECUTION
# ===================================================================

def main():
    """
    Main program function that handles the user interface and program flow.

    Demonstrates:
    - Function-based program organization
    - Infinite loop with break condition
    - User input handling and validation
    - Menu-driven interface design
    - Exception handling for user interruption
    - Input parsing and type conversion
    """
    # Display welcome banner
    print_banner()

    # Create ExpenseTracker instance
    # Demonstrates object instantiation
    tracker = ExpenseTracker()

    # Main program loop
    # Demonstrates infinite loop with controlled exit
    while True:
        try:
            # Display main menu
            print("\n=== Expense Tracker Menu ===")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Get Summary")
            print("4. Exit")

            # Get user choice
            # Demonstrates input() function for user interaction
            choice = input("\nEnter your choice (1-4): ")

            # Handle Add Expense option
            if choice == '1':
                try:
                    # Get expense details from user
                    # Demonstrates multiple input operations and type conversion
                    date = input("Enter date (YYYY-MM-DD): ")
                    amount_input = input("Enter amount: ")
                    amount = float(amount_input)  # Convert string to float
                    category = input("Enter category: ")
                    description = input("Enter description: ")

                    # Add expense using tracker method
                    tracker.add_expense(date, amount, category, description)

                except ValueError:
                    # Handle invalid amount input
                    print("Error: Please enter a valid amount (number).")
                except KeyboardInterrupt:
                    # Handle user cancellation (Ctrl+C)
                    print("\nOperation cancelled.")
                    continue

            # Handle View Expenses option
            elif choice == '2':
                try:
                    # Display filtering sub-menu
                    print("\nFilter options:")
                    print("1. View all expenses")
                    print("2. Filter by date range")
                    print("3. Filter by category")

                    filter_choice = input("Enter filter choice (1-3): ")

                    # Process filter choice
                    if filter_choice == '1':
                        # Get all expenses (no filters)
                        expenses = tracker.get_expenses()
                    elif filter_choice == '2':
                        # Get expenses by date range
                        start_date = input("Enter start date (YYYY-MM-DD): ")
                        end_date = input("Enter end date (YYYY-MM-DD): ")
                        expenses = tracker.get_expenses(start_date, end_date)
                    elif filter_choice == '3':
                        # Get expenses by category
                        category = input("Enter category: ")
                        expenses = tracker.get_expenses(category=category)
                    else:
                        print("Invalid choice!")
                        continue

                    # Display filtered expenses
                    print_expenses(expenses)

                except ValueError:
                    # Handle invalid date format
                    print("Error: Invalid date format. Please use YYYY-MM-DD format.")
                except KeyboardInterrupt:
                    # Handle user cancellation
                    print("\nOperation cancelled.")
                    continue

            # Handle Get Summary option
            elif choice == '3':
                # Generate and display summary
                # Demonstrates method chaining and function calls
                summary = tracker.get_summary()
                print_summary(summary)

            # Handle Exit option
            elif choice == '4':
                print("\nThank you for using Expense Tracker!")
                print("Goodbye!")
                break  # Exit the main loop

            # Handle invalid menu choice
            else:
                print("Invalid choice! Please try again.")

        except KeyboardInterrupt:
            # Handle program interruption (Ctrl+C)
            # Demonstrates graceful program termination
            print("\n\nGoodbye!")
            break
        except Exception as e:
            # Handle any unexpected errors
            # Demonstrates generic error handling for program stability
            print(f"An unexpected error occurred: {str(e)}")
            print("Please try again.")

# ===================================================================
# PROGRAM ENTRY POINT
# ===================================================================

if __name__ == "__main__":
    """
    Standard Python idiom for script execution.

    Demonstrates:
    - Python's __name__ == "__main__" pattern
    - Module vs script execution distinction
    - Program entry point best practices
    """
    main()