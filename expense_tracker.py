from datetime import datetime
from typing import List, Dict, Optional

def print_banner():
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
    """Print a formatted message when no expenses are found."""
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
    """Print a formatted summary of expenses."""
    if not summary['categories']:
        print_no_expenses_message()
        return

    # Calculate the maximum category name length for proper alignment
    max_category_length = max(len(cat) for cat in summary['categories'].keys()) if summary['categories'] else 0
    max_category_length = max(max_category_length, len("Category"))

    # Print header
    print("\n" + "=" * (max_category_length + 20))
    print(f"{'EXPENSE SUMMARY':^{max_category_length + 20}}")
    print("=" * (max_category_length + 20))

    # Print category breakdown
    print("\nCategory Breakdown:")
    print("-" * (max_category_length + 20))
    print(f"{'Category':<{max_category_length}} | {'Amount':>10}")
    print("-" * (max_category_length + 20))

    # Sort categories by amount in descending order
    sorted_categories = sorted(summary['categories'].items(),
                             key=lambda x: x[1],
                             reverse=True)

    for category, amount in sorted_categories:
        print(f"{category:<{max_category_length}} | ${amount:>9.2f}")

    # Print total
    print("-" * (max_category_length + 20))
    print(f"{'TOTAL':<{max_category_length}} | ${summary['total']:>9.2f}")
    print("=" * (max_category_length + 20))

def print_expenses(expenses: List[Dict]):
    """Print a formatted list of expenses."""
    if not expenses:
        print_no_expenses_message()
        return

    # Calculate column widths
    date_width = 12  # YYYY-MM-DD format
    amount_width = 10
    category_width = max(len(exp['Category']) for exp in expenses)
    category_width = max(category_width, len("Category"))
    desc_width = max(len(exp['Description']) for exp in expenses)
    desc_width = max(desc_width, len("Description"))

    # Calculate total width
    total_width = date_width + amount_width + category_width + desc_width + 9  # 9 for separators and spaces

    # Print header
    print("\n" + "=" * total_width)
    print(f"{'EXPENSE LIST':^{total_width}}")
    print("=" * total_width)

    # Print column headers
    print(f"{'Date':<{date_width}} | {'Amount':>{amount_width}} | {'Category':<{category_width}} | {'Description':<{desc_width}}")
    print("-" * total_width)

    # Print expenses
    for expense in expenses:
        print(f"{expense['Date']:<{date_width}} | ${float(expense['Amount']):>{amount_width-1}.2f} | "
              f"{expense['Category']:<{category_width}} | {expense['Description']:<{desc_width}}")

    # Print footer
    print("=" * total_width)
    print(f"Total Expenses: {len(expenses)}")
    print("=" * total_width)

class ExpenseTracker:
    def __init__(self):
        self.expenses: List[Dict] = []

    def add_expense(self, date: str, amount: float, category: str, description: str):
        """Add a new expense to the tracker."""
        try:
            # Validate date format
            datetime.strptime(date, '%Y-%m-%d')

            expense = {
                'Date': date,
                'Amount': amount,
                'Category': category,
                'Description': description
            }
            self.expenses.append(expense)
            print("Expense added successfully!")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD format.")
        except Exception as e:
            print(f"Error adding expense: {str(e)}")

    def get_expenses(self, start_date: Optional[str] = None,
                    end_date: Optional[str] = None,
                    category: Optional[str] = None) -> List[Dict]:
        """Get expenses filtered by date range and/or category."""
        filtered_expenses = []

        for expense in self.expenses:
            try:
                expense_date = datetime.strptime(expense['Date'], '%Y-%m-%d')

                # Apply filters
                if start_date:
                    start = datetime.strptime(start_date, '%Y-%m-%d')
                    if expense_date < start:
                        continue

                if end_date:
                    end = datetime.strptime(end_date, '%Y-%m-%d')
                    if expense_date > end:
                        continue

                if category and expense['Category'].lower() != category.lower():
                    continue

                filtered_expenses.append(expense)
            except ValueError:
                print(f"Warning: Skipping expense with invalid date: {expense.get('Date', 'Unknown')}")
                continue

        return filtered_expenses

    def get_summary(self) -> Dict:
        """Get summary of expenses by category and total."""
        summary = {'categories': {}, 'total': 0}

        for expense in self.expenses:
            try:
                amount = float(expense['Amount'])
                category = expense['Category']

                # Update category total
                if category not in summary['categories']:
                    summary['categories'][category] = 0
                summary['categories'][category] += amount

                # Update overall total
                summary['total'] += amount
            except (ValueError, KeyError):
                print(f"Warning: Skipping invalid expense entry")
                continue

        return summary

def main():
    print_banner()
    tracker = ExpenseTracker()

    while True:
        try:
            print("\n=== Expense Tracker Menu ===")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Get Summary")
            print("4. Exit")

            choice = input("\nEnter your choice (1-4): ")

            if choice == '1':
                try:
                    date = input("Enter date (YYYY-MM-DD): ")
                    amount_input = input("Enter amount: ")
                    amount = float(amount_input)
                    category = input("Enter category: ")
                    description = input("Enter description: ")
                    tracker.add_expense(date, amount, category, description)
                except ValueError:
                    print("Error: Please enter a valid amount (number).")
                except KeyboardInterrupt:
                    print("\nOperation cancelled.")
                    continue

            elif choice == '2':
                try:
                    print("\nFilter options:")
                    print("1. View all expenses")
                    print("2. Filter by date range")
                    print("3. Filter by category")

                    filter_choice = input("Enter filter choice (1-3): ")

                    if filter_choice == '1':
                        expenses = tracker.get_expenses()
                    elif filter_choice == '2':
                        start_date = input("Enter start date (YYYY-MM-DD): ")
                        end_date = input("Enter end date (YYYY-MM-DD): ")
                        expenses = tracker.get_expenses(start_date, end_date)
                    elif filter_choice == '3':
                        category = input("Enter category: ")
                        expenses = tracker.get_expenses(category=category)
                    else:
                        print("Invalid choice!")
                        continue

                    print_expenses(expenses)
                except ValueError:
                    print("Error: Invalid date format. Please use YYYY-MM-DD format.")
                except KeyboardInterrupt:
                    print("\nOperation cancelled.")
                    continue

            elif choice == '3':
                summary = tracker.get_summary()
                print_summary(summary)

            elif choice == '4':
                print("\nThank you for using Expense Tracker!")
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    main()