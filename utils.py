"""
=============================================================================
Project: python-utility-module
File: utils.py
Description: A reusable Python utility module containing helper functions for
             Validation, Formatting, Mathematical Calculations, and File I/O.
Author: Level 1 Python Intern (Day 25: Create a Python Utility Module)
Python Version: 3.8+ (Standard Library Only)
=============================================================================
"""

from __future__ import annotations

import math
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import List, Union


# =============================================================================
# SECTION 1: VALIDATION UTILITIES
# =============================================================================

def is_valid_email(email: str) -> bool:
    """
    Validates whether an email string adheres to a standard email format.

    Parameters:
        email (str): The email address string to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.

    Example:
        >>> is_valid_email("intern@example.com")
        True
        >>> is_valid_email("invalid-email@")
        False
    """
    if not isinstance(email, str):
        return False

    # Standard regular expression for general email validation
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email.strip()) is not None


def is_valid_phone(phone: str) -> bool:
    """
    Validates whether the provided string is a valid 10-digit Indian mobile number.
    Accepts numbers with optional '+91', '91', or '0' prefixes, and optional
    hyphens or spaces. The core 10 digits must start with 6, 7, 8, or 9.

    Parameters:
        phone (str): The phone number string to validate.

    Returns:
        bool: True if the phone number is a valid 10-digit Indian mobile number,
              False otherwise.

    Example:
        >>> is_valid_phone("9876543210")
        True
        >>> is_valid_phone("+91 98765-43210")
        True
        >>> is_valid_phone("1234567890")
        False
    """
    if not isinstance(phone, str):
        return False

    # Remove all spaces, hyphens, and parenthesis
    cleaned = re.sub(r"[\s\-\(\)]", "", phone.strip())

    # Match: optional +91, 91, or 0 followed by 10 digits starting with 6-9
    pattern = r"^(?:\+91|91|0)?[6-9]\d{9}$"
    return re.match(pattern, cleaned) is not None


def is_positive_number(value: Union[int, float]) -> bool:
    """
    Checks if a given numeric value is strictly greater than zero (> 0).

    Parameters:
        value (int | float): The number to inspect.

    Returns:
        bool: True if value is a number and > 0, False otherwise.

    Example:
        >>> is_positive_number(42)
        True
        >>> is_positive_number(-5.5)
        False
        >>> is_positive_number(0)
        False
    """
    # Note: bool is a subclass of int in Python (isinstance(True, int) is True)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False

    return value > 0


def is_non_empty_string(text: str) -> bool:
    """
    Checks if a given value is a string containing non-whitespace characters.

    Parameters:
        text (str): The string to evaluate.

    Returns:
        bool: True if text is a non-empty string with visible characters,
              False otherwise.

    Example:
        >>> is_non_empty_string("Antigravity")
        True
        >>> is_non_empty_string("   ")
        False
    """
    if not isinstance(text, str):
        return False

    return len(text.strip()) > 0


def is_in_range(
    value: Union[int, float],
    low: Union[int, float],
    high: Union[int, float]
) -> bool:
    """
    Checks if a number falls within a specified inclusive range [low, high].

    Parameters:
        value (int | float): The number to test.
        low (int | float): The minimum acceptable boundary.
        high (int | float): The maximum acceptable boundary.

    Returns:
        bool: True if low <= value <= high, False otherwise.

    Raises:
        ValueError: If low is strictly greater than high.
        TypeError: If any of value, low, or high is not a numeric type.

    Example:
        >>> is_in_range(15, 10, 20)
        True
        >>> is_in_range(25, 10, 20)
        False
    """
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) for x in (value, low, high)):
        raise TypeError("All arguments (value, low, high) must be integers or floats.")

    if low > high:
        raise ValueError(f"Lower bound ({low}) cannot be greater than upper bound ({high}).")

    return low <= value <= high


# =============================================================================
# SECTION 2: FORMATTING UTILITIES
# =============================================================================

def format_currency(amount: Union[int, float], symbol: str = "₹") -> str:
    """
    Formats a numeric amount into a readable currency string with two decimal places
    and standard comma separation.

    Parameters:
        amount (int | float): The numeric money amount.
        symbol (str): The currency symbol (default: '₹').

    Returns:
        str: Formatted currency string (e.g., '₹1,234.50' or '-₹50.00').

    Raises:
        TypeError: If amount is not a numeric value or symbol is not a string.

    Example:
        >>> format_currency(1234567.89)
        '₹1,234,567.89'
        >>> format_currency(-500, symbol="$")
        '-$500.00'
    """
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise TypeError("The amount must be an integer or float.")
    if not isinstance(symbol, str):
        raise TypeError("The currency symbol must be a string.")

    if amount < 0:
        return f"-{symbol}{abs(amount):,.2f}"
    return f"{symbol}{amount:,.2f}"


def format_percentage(value: Union[int, float], decimals: int = 2) -> str:
    """
    Formats a numeric value as a percentage string with the specified decimals.

    Parameters:
        value (int | float): The percentage number (e.g., 85.5 for 85.5%).
        decimals (int): Number of digits following the decimal point (default: 2).

    Returns:
        str: Formatted percentage string (e.g., '85.50%').

    Raises:
        TypeError: If value or decimals are not numeric types.
        ValueError: If decimals is negative.

    Example:
        >>> format_percentage(75.256)
        '75.26%'
        >>> format_percentage(100, decimals=0)
        '100%'
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("Value must be an integer or float.")
    if isinstance(decimals, bool) or not isinstance(decimals, int):
        raise TypeError("Decimals must be an integer.")
    if decimals < 0:
        raise ValueError("Decimals count cannot be negative.")

    return f"{value:.{decimals}f}%"


def to_title_case(text: str) -> str:
    """
    Converts a text string to Title Case where each word begins with a capital letter.
    Preserves multiple whitespace spacing.

    Parameters:
        text (str): The input string to convert.

    Returns:
        str: The title-cased string.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> to_title_case("hello world of python")
        'Hello World Of Python'
    """
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    # Capitalize the first letter of each word while retaining whitespace
    words = text.split(" ")
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


def format_date(date_obj: Union[date, datetime], fmt: str = "%d-%m-%Y") -> str:
    """
    Formats a date or datetime object into a customized date string.

    Parameters:
        date_obj (date | datetime): The date object to format.
        fmt (str): The strftime format pattern (default: '%d-%m-%Y').

    Returns:
        str: Formatted date string (e.g., '25-10-2026').

    Raises:
        TypeError: If date_obj is not an instance of datetime.date or datetime.datetime.
        ValueError: If the format string is invalid.

    Example:
        >>> from datetime import date
        >>> format_date(date(2026, 10, 25))
        '25-10-2026'
    """
    if not isinstance(date_obj, (date, datetime)):
        raise TypeError("date_obj must be an instance of datetime.date or datetime.datetime.")

    return date_obj.strftime(fmt)


def truncate_text(text: str, max_length: int) -> str:
    """
    Truncates a string to a maximum character length and appends an ellipsis ('...')
    if truncation occurs.

    Parameters:
        text (str): The text to truncate.
        max_length (int): Maximum length of the returned string (including ellipsis).

    Returns:
        str: Truncated text with '...' appended if truncated, or original text.

    Raises:
        TypeError: If text is not str or max_length is not int.
        ValueError: If max_length is less than 3.

    Example:
        >>> truncate_text("Modular programming makes code reusable.", 20)
        'Modular programm...'
        >>> truncate_text("Short text", 20)
        'Short text'
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if isinstance(max_length, bool) or not isinstance(max_length, int):
        raise TypeError("max_length must be an integer.")
    if max_length < 3:
        raise ValueError("max_length must be at least 3 to fit the ellipsis ('...').")

    if len(text) <= max_length:
        return text

    return text[: max_length - 3] + "..."


# =============================================================================
# SECTION 3: CALCULATION UTILITIES
# =============================================================================

def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculates the arithmetic mean of a sequence of numbers.

    Parameters:
        numbers (list[int | float]): A non-empty list of integers or floats.

    Returns:
        float: The calculated average value.

    Raises:
        ValueError: If the numbers list is empty.
        TypeError: If the collection contains non-numeric elements or is not a list/tuple.

    Example:
        >>> calculate_average([10, 20, 30, 40])
        25.0
    """
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Numbers must be provided as a list or tuple.")

    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty collection.")

    for item in numbers:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            raise TypeError(f"Invalid non-numeric element found: {item!r}")

    return float(sum(numbers) / len(numbers))


def calculate_percentage(part: Union[int, float], whole: Union[int, float]) -> float:
    """
    Calculates what percentage 'part' represents out of 'whole'.

    Parameters:
        part (int | float): The portion value.
        whole (int | float): The total/reference value (cannot be zero).

    Returns:
        float: The resulting percentage value.

    Raises:
        ValueError: If whole is zero (division by zero).
        TypeError: If either part or whole is non-numeric.

    Example:
        >>> calculate_percentage(25, 200)
        12.5
    """
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) for x in (part, whole)):
        raise TypeError("Both 'part' and 'whole' must be numeric.")

    if whole == 0:
        raise ValueError("Cannot calculate percentage: 'whole' denominator cannot be zero.")

    return float((part / whole) * 100.0)


def calculate_simple_interest(
    principal: Union[int, float],
    rate: Union[int, float],
    time: Union[int, float]
) -> float:
    """
    Calculates Simple Interest using the formula: (Principal * Rate * Time) / 100.

    Parameters:
        principal (int | float): Starting loan or deposit amount.
        rate (int | float): Annual interest rate percentage (e.g., 7.5 for 7.5%).
        time (int | float): Duration in years.

    Returns:
        float: The simple interest earned or owed.

    Raises:
        ValueError: If principal, rate, or time is negative.
        TypeError: If any parameter is not numeric.

    Example:
        >>> calculate_simple_interest(10000, 5, 2)
        1000.0
    """
    args = (principal, rate, time)
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) for x in args):
        raise TypeError("Principal, rate, and time must all be integers or floats.")

    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative values.")

    return float((principal * rate * time) / 100.0)


def celsius_to_fahrenheit(c: Union[int, float]) -> float:
    """
    Converts temperature from Celsius to Fahrenheit using: (C * 9/5) + 32.

    Parameters:
        c (int | float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.

    Raises:
        TypeError: If c is not numeric.

    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    if isinstance(c, bool) or not isinstance(c, (int, float)):
        raise TypeError("Celsius temperature must be an integer or float.")

    return float((c * 9.0 / 5.0) + 32.0)


def fahrenheit_to_celsius(f: Union[int, float]) -> float:
    """
    Converts temperature from Fahrenheit to Celsius using: (F - 32) * 5/9.

    Parameters:
        f (int | float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.

    Raises:
        TypeError: If f is not numeric.

    Example:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
    """
    if isinstance(f, bool) or not isinstance(f, (int, float)):
        raise TypeError("Fahrenheit temperature must be an integer or float.")

    return float((f - 32.0) * 5.0 / 9.0)


def is_prime(n: int) -> bool:
    """
    Determines whether an integer is a prime number (greater than 1, with no
    divisors other than 1 and itself).

    Parameters:
        n (int): The integer to test.

    Returns:
        bool: True if n is prime, False otherwise.

    Raises:
        TypeError: If n is not an integer.

    Example:
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
        >>> is_prime(1)
        False
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Prime check requires an integer input.")

    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisors up to square root of n using 6k +/- 1 optimization
    limit = int(math.isqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer n (n! = n * (n-1) * ... * 1).

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The factorial value (0! = 1).

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.

    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Factorial requires an integer input.")

    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    if n in (0, 1):
        return 1

    # Iterative calculation for clarity and avoiding recursion limits
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


# =============================================================================
# SECTION 4: FILE UTILITIES
# =============================================================================

def read_file(path: Union[str, Path]) -> str:
    """
    Reads and returns the complete text content of a file using UTF-8 encoding.

    Parameters:
        path (str | Path): File path to read.

    Returns:
        str: Text content of the file.

    Raises:
        FileNotFoundError: If the target file does not exist.
        IsADirectoryError: If the target path points to a directory.

    Example:
        >>> content = read_file("sample_data.txt")
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found at: {file_path}")
    if file_path.is_dir():
        raise IsADirectoryError(f"Expected a file but found directory: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(path: Union[str, Path], content: str) -> None:
    """
    Writes text content to a file, completely overwriting any existing content.
    Automatically creates parent directories if they do not exist.

    Parameters:
        path (str | Path): Target destination path.
        content (str): Text data to write.

    Raises:
        TypeError: If content is not a string.

    Example:
        >>> write_file("notes.txt", "Hello from Python!")
    """
    if not isinstance(content, str):
        raise TypeError("Content to write must be a string.")

    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def append_to_file(path: Union[str, Path], content: str) -> None:
    """
    Appends text content to the end of an existing or new file.
    Creates parent directories if necessary.

    Parameters:
        path (str | Path): Target file path.
        content (str): Text data to append.

    Raises:
        TypeError: If content is not a string.

    Example:
        >>> append_to_file("log.txt", "New entry\\n")
    """
    if not isinstance(content, str):
        raise TypeError("Content to append must be a string.")

    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content)


def file_exists(path: Union[str, Path]) -> bool:
    """
    Checks whether a file exists at the given path and is a regular file.

    Parameters:
        path (str | Path): File path to check.

    Returns:
        bool: True if path exists and is a regular file, False otherwise.

    Example:
        >>> file_exists("sample_data.txt")
        True
    """
    try:
        return Path(path).is_file()
    except (TypeError, ValueError):
        return False


def count_lines(path: Union[str, Path]) -> int:
    """
    Counts the total number of lines in a text file.

    Parameters:
        path (str | Path): Path to the target text file.

    Returns:
        int: Number of lines found in the file.

    Raises:
        FileNotFoundError: If the target file does not exist.

    Example:
        >>> count_lines("sample_data.txt")
        7
    """
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    count = 0
    with open(file_path, "r", encoding="utf-8") as file:
        for _ in file:
            count += 1
    return count


def get_file_extension(path: Union[str, Path]) -> str:
    """
    Extracts and returns the lowercase file extension including the leading dot.

    Parameters:
        path (str | Path): Path or file name.

    Returns:
        str: Lowercase extension (e.g., '.txt', '.py') or '' if no extension.

    Example:
        >>> get_file_extension("document.PDF")
        '.pdf'
        >>> get_file_extension("archive.tar.gz")
        '.gz'
    """
    return Path(path).suffix.lower()


# =============================================================================
# SELF-TEST BLOCK
# =============================================================================

if __name__ == "__main__":
    if sys.platform.startswith("win"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    print("=" * 65)
    print("           RUNNING UTILS.PY INTERNAL SELF-TEST SUITE            ")
    print("=" * 65)

    passed_tests = 0
    total_tests = 0

    def test(condition: bool, description: str) -> None:
        global passed_tests, total_tests
        total_tests += 1
        if condition:
            passed_tests += 1
            print(f" [PASS] {description}")
        else:
            print(f" [FAIL] {description}")

    # 1. Validation Tests
    print("\n--- 1. Validation Tests ---")
    test(is_valid_email("intern@example.com") is True, "Valid email format")
    test(is_valid_email("user.name+tag@sub.domain.co") is True, "Complex valid email")
    test(is_valid_email("bad-email@") is False, "Invalid email missing domain")
    test(is_valid_email("no_at_sign.com") is False, "Invalid email missing @")

    test(is_valid_phone("9876543210") is True, "Standard 10-digit Indian phone")
    test(is_valid_phone("+91 98765-43210") is True, "Indian phone with +91 prefix and hyphens")
    test(is_valid_phone("08123456789") is True, "Indian phone with 0 prefix")
    test(is_valid_phone("5123456789") is False, "Invalid Indian phone starting with 5")
    test(is_valid_phone("98765") is False, "Too short phone number")

    test(is_positive_number(10) is True, "Positive integer")
    test(is_positive_number(0.01) is True, "Positive float")
    test(is_positive_number(0) is False, "Zero is not positive")
    test(is_positive_number(-7) is False, "Negative number is not positive")
    test(is_positive_number(True) is False, "Boolean True is not treated as number")

    test(is_non_empty_string("Antigravity") is True, "Standard non-empty string")
    test(is_non_empty_string("   ") is False, "Whitespace-only string is considered empty")
    test(is_non_empty_string("") is False, "Empty string")

    test(is_in_range(15, 10, 20) is True, "Value in range")
    test(is_in_range(10, 10, 20) is True, "Value at lower boundary")
    test(is_in_range(20, 10, 20) is True, "Value at upper boundary")
    test(is_in_range(25, 10, 20) is False, "Value out of range")
    try:
        is_in_range(10, 50, 20)
        test(False, "is_in_range raised ValueError when low > high")
    except ValueError:
        test(True, "is_in_range raised ValueError when low > high")

    # 2. Formatting Tests
    print("\n--- 2. Formatting Tests ---")
    test(format_currency(1234567.89) == "₹1,234,567.89", "Format Indian Rupee currency")
    test(format_currency(-500.5, symbol="$") == "-$500.50", "Format negative USD currency")
    test(format_percentage(75.256) == "75.26%", "Format percentage to 2 decimals")
    test(format_percentage(50, decimals=0) == "50%", "Format percentage to 0 decimals")
    test(to_title_case("hello world of python") == "Hello World Of Python", "Title case conversion")
    test(format_date(date(2026, 10, 25)) == "25-10-2026", "Format date to default DD-MM-YYYY")
    test(truncate_text("Hello World", 8) == "Hello...", "Truncate text with ellipsis")
    test(truncate_text("Short", 10) == "Short", "Truncate text without modification if short")

    # 3. Calculation Tests
    print("\n--- 3. Calculation Tests ---")
    test(calculate_average([10, 20, 30, 40]) == 25.0, "Calculate average of list")
    test(calculate_percentage(25, 200) == 12.5, "Calculate percentage")
    test(calculate_simple_interest(10000, 5, 2) == 1000.0, "Calculate simple interest")
    test(celsius_to_fahrenheit(0) == 32.0, "Celsius 0 to Fahrenheit 32")
    test(celsius_to_fahrenheit(100) == 212.0, "Celsius 100 to Fahrenheit 212")
    test(fahrenheit_to_celsius(32) == 0.0, "Fahrenheit 32 to Celsius 0")
    test(fahrenheit_to_celsius(212) == 100.0, "Fahrenheit 212 to Celsius 100")
    test(is_prime(2) is True, "2 is prime")
    test(is_prime(17) is True, "17 is prime")
    test(is_prime(4) is False, "4 is not prime")
    test(is_prime(1) is False, "1 is not prime")
    test(is_prime(-7) is False, "Negative number is not prime")
    test(factorial(0) == 1, "0! is 1")
    test(factorial(5) == 120, "5! is 120")

    # Calculation Edge Cases
    try:
        calculate_average([])
        test(False, "calculate_average raised ValueError on empty list")
    except ValueError:
        test(True, "calculate_average raised ValueError on empty list")

    try:
        calculate_percentage(50, 0)
        test(False, "calculate_percentage raised ValueError on division by zero")
    except ValueError:
        test(True, "calculate_percentage raised ValueError on division by zero")

    try:
        factorial(-3)
        test(False, "factorial raised ValueError on negative number")
    except ValueError:
        test(True, "factorial raised ValueError on negative number")

    # 4. File Utility Tests
    print("\n--- 4. File Utility Tests ---")
    test_file = Path("temp_test_file.txt")
    try:
        write_file(test_file, "Line 1: Hello\nLine 2: World\n")
        test(file_exists(test_file) is True, "File exists after write")
        test(count_lines(test_file) == 2, "Count lines returns 2")
        test(read_file(test_file) == "Line 1: Hello\nLine 2: World\n", "Read file matches content")
        append_to_file(test_file, "Line 3: Appended\n")
        test(count_lines(test_file) == 3, "Count lines returns 3 after append")
        test(get_file_extension(test_file) == ".txt", "Get file extension returns .txt")
    finally:
        if test_file.exists():
            test_file.unlink()

    print("\n" + "=" * 65)
    print(f"SELF-TEST RESULTS: {passed_tests} / {total_tests} PASSED")
    print("=" * 65)
