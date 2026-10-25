"""
=============================================================================
Project: python-utility-module
File: main.py
Description: Example program demonstrating the usage of the reusable 'utils'
             module for Level 1 Python Internship (Day 25).
Features: Interactive menu, demonstration of all 23 functions across 4 sections,
          exception handling, and non-interactive demo mode.
=============================================================================
"""

import sys
from datetime import date, datetime
from pathlib import Path

# Ensure UTF-8 console encoding on Windows to support currency symbols like ₹
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, io.UnsupportedOperation):
        pass

# Import our custom reusable utility module
import utils


def print_header(title: str) -> None:
    """Helper to display clean section dividers."""
    print("\n" + "=" * 65)
    print(f"  {title.upper()}")
    print("=" * 65)


def demo_validation() -> None:
    """Demonstrates all validation functions from utils.py."""
    print_header("1. Validation Utilities Demonstration")

    # 1. Email validation
    test_emails = [
        "intern.success@example.com",
        "john.doe@company.org",
        "invalid-email-address",
        "@missingusername.com",
    ]
    print("\n[A] Email Validation (is_valid_email):")
    for email in test_emails:
        result = utils.is_valid_email(email)
        status = "VALID" if result else "INVALID"
        print(f"  - '{email}': {status}")

    # 2. Phone validation (Indian 10-digit mobile numbers)
    test_phones = [
        "9876543210",
        "+91 98765-43210",
        "08123456789",
        "5123456789",   # Starts with 5 (invalid)
        "98765",        # Too short
    ]
    print("\n[B] Phone Number Validation (is_valid_phone - 10-digit Indian Mobile):")
    for phone in test_phones:
        result = utils.is_valid_phone(phone)
        status = "VALID" if result else "INVALID"
        print(f"  - '{phone}': {status}")

    # 3. Positive number validation
    test_numbers = [42, 3.1415, 0, -15.5]
    print("\n[C] Positive Number Check (is_positive_number):")
    for num in test_numbers:
        result = utils.is_positive_number(num)
        print(f"  - {num} is positive? {result}")

    # 4. Non-empty string validation
    test_strings = ["Python Utility Module", "   ", ""]
    print("\n[D] Non-Empty String Check (is_non_empty_string):")
    for text in test_strings:
        result = utils.is_non_empty_string(text)
        print(f"  - '{text}' contains visible characters? {result}")

    # 5. Range validation
    print("\n[E] In-Range Check (is_in_range):")
    print(f"  - Is 75 in range [50, 100]? {utils.is_in_range(75, 50, 100)}")
    print(f"  - Is 25 in range [50, 100]? {utils.is_in_range(25, 50, 100)}")

    # Edge case: low > high handled with try/except
    try:
        utils.is_in_range(10, 100, 20)
    except ValueError as err:
        print(f"  - Handled invalid range (low > high): Caught ValueError -> '{err}'")


def demo_formatting() -> None:
    """Demonstrates all formatting functions from utils.py."""
    print_header("2. Formatting Utilities Demonstration")

    # 1. Currency formatting
    print("\n[A] Currency Formatting (format_currency):")
    print(f"  - 2500000 -> {utils.format_currency(2500000)}")
    print(f"  - 1234.5 -> {utils.format_currency(1234.5)}")
    print(f"  - -450.75 in USD -> {utils.format_currency(-450.75, symbol='$')}")

    # 2. Percentage formatting
    print("\n[B] Percentage Formatting (format_percentage):")
    print(f"  - 87.6543 (default 2 decimals) -> {utils.format_percentage(87.6543)}")
    print(f"  - 99.5 (0 decimals) -> {utils.format_percentage(99.5, decimals=0)}")
    print(f"  - 12.3456 (3 decimals) -> {utils.format_percentage(12.3456, decimals=3)}")

    # 3. Title case formatting
    raw_title = "python utility module for beginner interns"
    print("\n[C] Title Case Formatting (to_title_case):")
    print(f"  - Original: '{raw_title}'")
    print(f"  - Result  : '{utils.to_title_case(raw_title)}'")

    # 4. Date formatting
    today = date(2026, 10, 25)
    now = datetime(2026, 10, 25, 15, 30, 0)
    print("\n[D] Date Formatting (format_date):")
    print(f"  - Default (DD-MM-YYYY) : {utils.format_date(today)}")
    print(f"  - Custom (YYYY/MM/DD)  : {utils.format_date(today, fmt='%Y/%m/%d')}")
    print(f"  - Full Date with Time  : {utils.format_date(now, fmt='%B %d, %Y at %I:%M %p')}")

    # 5. Text truncation
    long_text = "Modular programming allows developers to write reusable and testable components."
    print("\n[E] Text Truncation (truncate_text):")
    print(f"  - Original ({len(long_text)} chars): '{long_text}'")
    print(f"  - Truncated to 35 chars: '{utils.truncate_text(long_text, 35)}'")
    print(f"  - Truncated to 100 chars (no change): '{utils.truncate_text(long_text, 100)}'")


def demo_calculations() -> None:
    """Demonstrates all calculation functions from utils.py with edge case handling."""
    print_header("3. Calculation Utilities Demonstration")

    # 1. Average calculation
    scores = [85, 90, 78, 92, 88]
    avg = utils.calculate_average(scores)
    print("\n[A] Average Calculation (calculate_average):")
    print(f"  - Scores: {scores}")
    print(f"  - Average: {avg:.2f}")

    # Edge case: Empty list
    try:
        utils.calculate_average([])
    except ValueError as err:
        print(f"  - Handled edge case (empty list): Caught ValueError -> '{err}'")

    # 2. Percentage calculation
    marks_obtained = 425
    total_marks = 500
    pct = utils.calculate_percentage(marks_obtained, total_marks)
    print("\n[B] Percentage Calculation (calculate_percentage):")
    print(f"  - {marks_obtained} out of {total_marks} = {pct:.2f}%")

    # Edge case: Division by zero
    try:
        utils.calculate_percentage(50, 0)
    except ValueError as err:
        print(f"  - Handled edge case (zero total): Caught ValueError -> '{err}'")

    # 3. Simple interest
    principal = 50000
    rate = 7.5
    time_years = 3
    interest = utils.calculate_simple_interest(principal, rate, time_years)
    print("\n[C] Simple Interest Calculation (calculate_simple_interest):")
    print(f"  - Principal: {utils.format_currency(principal)}")
    print(f"  - Rate: {rate}%, Time: {time_years} years")
    print(f"  - Interest Earned: {utils.format_currency(interest)}")

    # 4. Temperature conversions
    celsius_temp = 37.0
    fahr_temp = 98.6
    print("\n[D] Temperature Conversions (celsius_to_fahrenheit & fahrenheit_to_celsius):")
    print(f"  - {celsius_temp}\u00b0C in Fahrenheit = {utils.celsius_to_fahrenheit(celsius_temp):.2f}\u00b0F")
    print(f"  - {fahr_temp}\u00b0F in Celsius    = {utils.fahrenheit_to_celsius(fahr_temp):.2f}\u00b0C")

    # 5. Prime number check
    test_integers = [2, 17, 27, 49, 97]
    print("\n[E] Prime Number Check (is_prime):")
    for n in test_integers:
        print(f"  - Is {n} prime? {utils.is_prime(n)}")

    # 6. Factorial calculation
    print("\n[F] Factorial Calculation (factorial):")
    for n in [0, 1, 5, 7]:
        print(f"  - {n}! = {utils.factorial(n)}")

    # Edge case: Negative factorial
    try:
        utils.factorial(-5)
    except ValueError as err:
        print(f"  - Handled edge case (negative number): Caught ValueError -> '{err}'")


def demo_file_utilities() -> None:
    """Demonstrates all file utility functions using sample_data.txt and temporary files."""
    print_header("4. File Utilities Demonstration")

    sample_file = Path("sample_data.txt")
    temp_demo_file = Path("demo_output.txt")

    print(f"\n[A] File Existence (file_exists):")
    print(f"  - Does '{sample_file}' exist? {utils.file_exists(sample_file)}")
    print(f"  - Does 'non_existent.txt' exist? {utils.file_exists('non_existent.txt')}")

    if utils.file_exists(sample_file):
        print(f"\n[B] File Extension (get_file_extension):")
        print(f"  - Extension of '{sample_file}': '{utils.get_file_extension(sample_file)}'")

        print(f"\n[C] Line Count (count_lines):")
        line_count = utils.count_lines(sample_file)
        print(f"  - Total lines in '{sample_file}': {line_count}")

        print(f"\n[D] Reading File Content (read_file):")
        content = utils.read_file(sample_file)
        print("  --- File Preview (First 3 lines) ---")
        for line in content.strip().splitlines()[:3]:
            print(f"    {line}")
        print("    ...")

    # Write and append demonstration
    try:
        print(f"\n[E] Writing to File (write_file):")
        utils.write_file(temp_demo_file, "This is line 1 written by main.py demo.\n")
        print(f"  - Successfully created '{temp_demo_file}'")

        print(f"\n[F] Appending to File (append_to_file):")
        utils.append_to_file(temp_demo_file, "This is line 2 appended by main.py demo.\n")
        print(f"  - Successfully appended to '{temp_demo_file}'")

        updated_lines = utils.count_lines(temp_demo_file)
        print(f"  - Verified line count after append: {updated_lines} lines")
        print(f"  - Verified content:\n    {utils.read_file(temp_demo_file).strip()}")
    finally:
        # Clean up temporary demonstration file
        if temp_demo_file.exists():
            temp_demo_file.unlink()
            print(f"  - Cleaned up temporary demonstration file '{temp_demo_file}'")

    # Error handling demonstration: missing file
    try:
        utils.read_file("file_that_does_not_exist.txt")
    except FileNotFoundError as err:
        print(f"\n[G] Handled FileNotFoundError gracefully:")
        print(f"  - Caught error: {err}")


def run_all_demos() -> None:
    """Executes all four demonstration categories consecutively."""
    print("\n" + "#" * 65)
    print("  EXECUTING COMPLETE PYTHON-UTILITY-MODULE DEMONSTRATION")
    print("#" * 65)
    demo_validation()
    demo_formatting()
    demo_calculations()
    demo_file_utilities()
    print("\n" + "#" * 65)
    print("  ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY")
    print("#" * 65 + "\n")


def interactive_menu() -> None:
    """Provides a simple interactive menu loop with robust input handling."""
    menu_text = """
=================================================================
             PYTHON UTILITY MODULE - MAIN MENU
=================================================================
  [1] Validation Utilities Demo
  [2] Formatting Utilities Demo
  [3] Calculation Utilities Demo
  [4] File Utilities Demo
  [5] Run All Demonstrations
  [6] Exit Program
================================================================="""

    while True:
        print(menu_text)
        try:
            choice = input("Enter your choice (1-6): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nExiting program. Goodbye!")
            break

        if choice == "1":
            demo_validation()
        elif choice == "2":
            demo_formatting()
        elif choice == "3":
            demo_calculations()
        elif choice == "4":
            demo_file_utilities()
        elif choice == "5":
            run_all_demos()
        elif choice == "6":
            print("\nThank you for using the Python Utility Module! Happy coding.\n")
            break
        else:
            print("\n[!] Invalid selection. Please enter a number between 1 and 6.")

        try:
            input("\nPress [Enter] to return to the main menu...")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting program.")
            break


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    # If launched with '--all' or '--demo', run all demos without waiting for input
    if len(sys.argv) > 1 and sys.argv[1].lower() in ("--all", "--demo", "-a"):
        run_all_demos()
    else:
        # Run the interactive menu by default
        interactive_menu()
