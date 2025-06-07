# ===================================================================
# MSCS 632 Advanced Programming Languages
# Group Project - Expense Tracker Testing Suite
# Python Implementation Tests
# ===================================================================

import unittest
from datetime import datetime
import sys
from expense_tracker import ExpenseTracker


class TestExpenseTracker(unittest.TestCase):
    """Basic test suite for the ExpenseTracker class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.tracker = ExpenseTracker()

    def test_initialization(self):
        """Test that ExpenseTracker initializes correctly."""
        self.assertIsInstance(self.tracker.expenses, list)
        self.assertEqual(len(self.tracker.expenses), 0)
        print("✓ Initialization test passed")

    def test_add_valid_expense(self):
        """Test adding a valid expense."""
        self.tracker.add_expense("2025-05-01", 15.99, "Food", "Lunch")

        self.assertEqual(len(self.tracker.expenses), 1)
        expense = self.tracker.expenses[0]
        self.assertEqual(expense['Date'], "2025-05-01")
        self.assertEqual(expense['Amount'], 15.99)
        self.assertEqual(expense['Category'], "Food")
        self.assertEqual(expense['Description'], "Lunch")
        print("✓ Valid expense addition test passed")

    def test_add_invalid_date(self):
        """Test handling of invalid date formats."""
        initial_count = len(self.tracker.expenses)

        # Test invalid date format
        self.tracker.add_expense("invalid-date", 10.0, "Test", "Test")

        # Should not add invalid expense
        self.assertEqual(len(self.tracker.expenses), initial_count)
        print("✓ Invalid date handling test passed")

    def test_get_all_expenses(self):
        """Test retrieving all expenses."""
        # Add sample expenses
        self.tracker.add_expense("2025-05-01", 15.99, "Food", "Lunch")
        self.tracker.add_expense("2025-05-02", 50.00, "Transport", "Gas")

        all_expenses = self.tracker.get_expenses()
        self.assertEqual(len(all_expenses), 2)
        print("✓ Get all expenses test passed")

    def test_filter_by_category(self):
        """Test filtering expenses by category."""
        # Add sample expenses
        self.tracker.add_expense("2025-05-01", 15.99, "Food", "Lunch")
        self.tracker.add_expense("2025-05-02", 50.00, "Transport", "Gas")
        self.tracker.add_expense("2025-05-03", 25.50, "Food", "Dinner")

        # Filter by Food category
        food_expenses = self.tracker.get_expenses(category="Food")
        self.assertEqual(len(food_expenses), 2)

        for expense in food_expenses:
            self.assertEqual(expense['Category'], "Food")
        print("✓ Category filtering test passed")

    def test_filter_by_date_range(self):
        """Test filtering expenses by date range."""
        # Add sample expenses
        self.tracker.add_expense("2025-05-01", 15.99, "Food", "Lunch")
        self.tracker.add_expense("2025-05-02", 50.00, "Transport", "Gas")
        self.tracker.add_expense("2025-05-05", 25.50, "Food", "Dinner")

        # Filter by date range
        filtered = self.tracker.get_expenses("2025-05-01", "2025-05-02")
        self.assertEqual(len(filtered), 2)
        print("✓ Date range filtering test passed")

    def test_summary_calculation(self):
        """Test expense summary calculation."""
        # Add sample expenses
        self.tracker.add_expense("2025-05-01", 15.99, "Food", "Lunch")
        self.tracker.add_expense("2025-05-02", 50.00, "Transport", "Gas")
        self.tracker.add_expense("2025-05-03", 25.50, "Food", "Dinner")

        summary = self.tracker.get_summary()

        # Check structure
        self.assertIn('categories', summary)
        self.assertIn('total', summary)

        # Check totals
        self.assertAlmostEqual(summary['categories']['Food'], 41.49, places=2)
        self.assertAlmostEqual(summary['categories']['Transport'], 50.00, places=2)
        self.assertAlmostEqual(summary['total'], 91.49, places=2)
        print("✓ Summary calculation test passed")

    def test_empty_tracker(self):
        """Test operations on empty tracker."""
        # Test getting expenses from empty tracker
        all_expenses = self.tracker.get_expenses()
        self.assertEqual(len(all_expenses), 0)

        # Test summary of empty tracker
        summary = self.tracker.get_summary()
        self.assertEqual(summary['categories'], {})
        self.assertEqual(summary['total'], 0)
        print("✓ Empty tracker test passed")

def run_integration_test():
    """Simple integration test for complete workflow."""
    print("\n" + "="*40)
    print("INTEGRATION TEST")
    print("="*40)

    tracker = ExpenseTracker()

    # Add expenses
    tracker.add_expense("2025-05-01", 15.99, "Food", "Lunch")
    tracker.add_expense("2025-05-02", 50.00, "Transport", "Gas")
    tracker.add_expense("2025-05-03", 25.50, "Food", "Groceries")

    # Test complete workflow
    all_expenses = tracker.get_expenses()
    assert len(all_expenses) == 3, "Should have 3 expenses"

    food_expenses = tracker.get_expenses(category="Food")
    assert len(food_expenses) == 2, "Should have 2 food expenses"

    summary = tracker.get_summary()
    assert abs(summary['total'] - 91.49) < 0.01, "Total should be 91.49"

    print("✓ Integration test passed - All workflows working correctly")

if __name__ == '__main__':
    print("EXPENSE TRACKER PYTHON TEST SUITE")
    print("="*50)

    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=1)

    # Run integration test
    run_integration_test()

    print("\n" + "="*50)
    print("ALL TESTS COMPLETED")
    print("="*50)