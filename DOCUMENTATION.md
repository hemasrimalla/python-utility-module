# `utils.py` Module Documentation

Welcome to the comprehensive reference documentation for the **`utils.py`** reusable utility library. This module was developed as part of **Day 25: Create a Python Utility Module** in the Level 1 Python Internship.

---

## Table of Contents
1. [Overview](#overview)
2. [Quick Reference Summary Table](#quick-reference-summary-table)
3. [1. Validation Utilities](#1-validation-utilities)
   - [`is_valid_email`](#is_valid_email)
   - [`is_valid_phone`](#is_valid_phone)
   - [`is_positive_number`](#is_positive_number)
   - [`is_non_empty_string`](#is_non_empty_string)
   - [`is_in_range`](#is_in_range)
4. [2. Formatting Utilities](#2-formatting-utilities)
   - [`format_currency`](#format_currency)
   - [`format_percentage`](#format_percentage)
   - [`to_title_case`](#to_title_case)
   - [`format_date`](#format_date)
   - [`truncate_text`](#truncate_text)
5. [3. Calculation Utilities](#3-calculation-utilities)
   - [`calculate_average`](#calculate_average)
   - [`calculate_percentage`](#calculate_percentage)
   - [`calculate_simple_interest`](#calculate_simple_interest)
   - [`celsius_to_fahrenheit`](#celsius_to_fahrenheit)
   - [`fahrenheit_to_celsius`](#fahrenheit_to_celsius)
   - [`is_prime`](#is_prime)
   - [`factorial`](#factorial)
6. [4. File Utilities](#4-file-utilities)
   - [`read_file`](#read_file)
   - [`write_file`](#write_file)
   - [`append_to_file`](#append_to_file)
   - [`file_exists`](#file_exists)
   - [`count_lines`](#count_lines)
   - [`get_file_extension`](#get_file_extension)

---

## Overview

The `utils.py` module adheres to clean architecture principles:
- **Zero External Dependencies**: Implemented strictly using the Python Standard Library (`re`, `math`, `datetime`, `pathlib`, `typing`).
- **Single Responsibility Principle (SRP)**: Each function performs exactly one clear task.
- **Strict Typing**: All functions include PEP 484 type annotations for IDE autocompletion and static type analysis.
- **Defensive Programming**: Functions validate edge cases (such as zero division, empty collections, negative dimensions) and raise descriptive built-in exceptions (`ValueError`, `TypeError`, `FileNotFoundError`).

---

## Quick Reference Summary Table

| Category | Function | Signature | Return Type | Brief Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Validation** | `is_valid_email` | `(email: str)` | `bool` | Checks if email syntax is valid |
| **Validation** | `is_valid_phone` | `(phone: str)` | `bool` | Validates 10-digit Indian mobile number |
| **Validation** | `is_positive_number` | `(value: int \| float)` | `bool` | Checks if number is strictly > 0 |
| **Validation** | `is_non_empty_string` | `(text: str)` | `bool` | Checks if string has non-whitespace text |
| **Validation** | `is_in_range` | `(value, low, high)` | `bool` | Checks if `low <= value <= high` |
| **Formatting** | `format_currency` | `(amount, symbol="₹")` | `str` | Formats currency with commas and 2 decimals |
| **Formatting** | `format_percentage` | `(value, decimals=2)` | `str` | Formats number with `%` and precision |
| **Formatting** | `to_title_case` | `(text: str)` | `str` | Capitalizes first letter of every word |
| **Formatting** | `format_date` | `(date_obj, fmt="%d-%m-%Y")` | `str` | Formats `date` or `datetime` to string |
| **Formatting** | `truncate_text` | `(text, max_length)` | `str` | Truncates text and appends `...` if exceeded |
| **Calculations** | `calculate_average` | `(numbers: list)` | `float` | Calculates arithmetic mean of a sequence |
| **Calculations** | `calculate_percentage` | `(part, whole)` | `float` | Returns what percentage part is of whole |
| **Calculations** | `calculate_simple_interest` | `(principal, rate, time)` | `float` | Calculates `(P * R * T) / 100` |
| **Calculations** | `celsius_to_fahrenheit` | `(c: int \| float)` | `float` | Converts Celsius to Fahrenheit |
| **Calculations** | `fahrenheit_to_celsius` | `(f: int \| float)` | `float` | Converts Fahrenheit to Celsius |
| **Calculations** | `is_prime` | `(n: int)` | `bool` | Tests if an integer is prime |
| **Calculations** | `factorial` | `(n: int)` | `int` | Computes factorial `n!` |
| **File Utilities** | `read_file` | `(path: str \| Path)` | `str` | Reads entire UTF-8 file content |
| **File Utilities** | `write_file` | `(path, content: str)` | `None` | Writes text to file, overwriting existing |
| **File Utilities** | `append_to_file` | `(path, content: str)` | `None` | Appends text to end of file |
| **File Utilities** | `file_exists` | `(path: str \| Path)` | `bool` | Verifies regular file presence |
| **File Utilities** | `count_lines` | `(path: str \| Path)` | `int` | Counts total lines in text file |
| **File Utilities** | `get_file_extension` | `(path: str \| Path)` | `str` | Returns lowercase extension (e.g. `.txt`) |

---

## 1. Validation Utilities

### `is_valid_email`
- **Purpose**: Validates whether a string matches a standard email pattern (`local-part@domain.extension`).
- **Parameters**:
  - `email` (*str*): The string candidate to validate.
- **Return Value**:
  - *bool*: `True` if valid; `False` otherwise.
- **Possible Exceptions**: None. Non-string inputs safely return `False`.
- **Example Usage**:
  ```python
  import utils

  print(utils.is_valid_email("intern@example.com"))  # Output: True
  print(utils.is_valid_email("not-an-email@"))        # Output: False
  ```

---

### `is_valid_phone`
- **Purpose**: Validates if a string is a 10-digit Indian mobile number. Supports optional leading `+91`, `91`, or `0`, and optional spaces/hyphens. The 10 core digits must start with 6, 7, 8, or 9.
- **Parameters**:
  - `phone` (*str*): The phone number string to validate.
- **Return Value**:
  - *bool*: `True` if valid; `False` otherwise.
- **Possible Exceptions**: None. Non-string inputs safely return `False`.
- **Example Usage**:
  ```python
  import utils

  print(utils.is_valid_phone("9876543210"))        # Output: True
  print(utils.is_valid_phone("+91 98765-43210"))   # Output: True
  print(utils.is_valid_phone("08123456789"))       # Output: True
  print(utils.is_valid_phone("5123456789"))        # Output: False
  ```

---

### `is_positive_number`
- **Purpose**: Checks whether a numeric value is strictly greater than zero (`> 0`). Excludes boolean types (`True`/`False`).
- **Parameters**:
  - `value` (*int | float*): Number to inspect.
- **Return Value**:
  - *bool*: `True` if numeric and `value > 0`; `False` otherwise.
- **Possible Exceptions**: None. Non-numeric types return `False`.
- **Example Usage**:
  ```python
  import utils

  print(utils.is_positive_number(42))     # Output: True
  print(utils.is_positive_number(0))      # Output: False
  print(utils.is_positive_number(-3.5))   # Output: False
  ```

---

### `is_non_empty_string`
- **Purpose**: Determines if an input is a string that contains visible, non-whitespace characters.
- **Parameters**:
  - `text` (*str*): Input string to evaluate.
- **Return Value**:
  - *bool*: `True` if string length after `strip()` is > 0; `False` otherwise.
- **Possible Exceptions**: None. Non-string types return `False`.
- **Example Usage**:
  ```python
  import utils

  print(utils.is_non_empty_string("Antigravity"))  # Output: True
  print(utils.is_non_empty_string("   "))          # Output: False
  print(utils.is_non_empty_string(""))             # Output: False
  ```

---

### `is_in_range`
- **Purpose**: Checks if a numeric value falls inclusively within the range `[low, high]`.
- **Parameters**:
  - `value` (*int | float*): Number to check.
  - `low` (*int | float*): Lower bound of the range.
  - `high` (*int | float*): Upper bound of the range.
- **Return Value**:
  - *bool*: `True` if `low <= value <= high`; `False` otherwise.
- **Possible Exceptions**:
  - `ValueError`: Raised if `low > high`.
  - `TypeError`: Raised if any input is non-numeric or a boolean.
- **Example Usage**:
  ```python
  import utils

  print(utils.is_in_range(15, 10, 20))  # Output: True
  print(utils.is_in_range(25, 10, 20))  # Output: False

  try:
      utils.is_in_range(10, 50, 20)
  except ValueError as err:
      print(f"Error caught: {err}")
  ```

---

## 2. Formatting Utilities

### `format_currency`
- **Purpose**: Formats a numeric amount into a currency string with two decimal places and standard comma grouping.
- **Parameters**:
  - `amount` (*int | float*): The monetary value.
  - `symbol` (*str*, default: `"₹"`): The prefix currency symbol.
- **Return Value**:
  - *str*: Formatted string (e.g., `"₹1,234,567.89"` or `"-$50.00"`).
- **Possible Exceptions**:
  - `TypeError`: Raised if `amount` is not numeric or `symbol` is not a string.
- **Example Usage**:
  ```python
  import utils

  print(utils.format_currency(2500000))                 # Output: '₹2,500,000.00'
  print(utils.format_currency(-450.75, symbol="$"))     # Output: '-$450.75'
  ```

---

### `format_percentage`
- **Purpose**: Formats a numeric value as a percentage with a configurable number of decimal places.
- **Parameters**:
  - `value` (*int | float*): The percentage number (e.g. `87.6543`).
  - `decimals` (*int*, default: `2`): Precision after decimal point.
- **Return Value**:
  - *str*: Formatted percentage string (e.g., `"87.65%"`).
- **Possible Exceptions**:
  - `TypeError`: Raised if `value` is non-numeric or `decimals` is not an `int`.
  - `ValueError`: Raised if `decimals < 0`.
- **Example Usage**:
  ```python
  import utils

  print(utils.format_percentage(87.6543))             # Output: '87.65%'
  print(utils.format_percentage(99.5, decimals=0))    # Output: '100%'
  ```

---

### `to_title_case`
- **Purpose**: Capitalizes the first letter of each word in a string while preserving word spacing.
- **Parameters**:
  - `text` (*str*): The text to format.
- **Return Value**:
  - *str*: The title-cased string.
- **Possible Exceptions**:
  - `TypeError`: Raised if `text` is not a string.
- **Example Usage**:
  ```python
  import utils

  print(utils.to_title_case("modular python programming"))
  # Output: 'Modular Python Programming'
  ```

---

### `format_date`
- **Purpose**: Formats a Python `datetime.date` or `datetime.datetime` object into a customized date string.
- **Parameters**:
  - `date_obj` (*date | datetime*): The date or datetime instance.
  - `fmt` (*str*, default: `"%d-%m-%Y"`): Standard `strftime` formatting directive.
- **Return Value**:
  - *str*: Formatted date string (e.g., `"25-10-2026"`).
- **Possible Exceptions**:
  - `TypeError`: Raised if `date_obj` is not a `date` or `datetime` object.
  - `ValueError`: Raised if the format string is malformed.
- **Example Usage**:
  ```python
  from datetime import date
  import utils

  d = date(2026, 10, 25)
  print(utils.format_date(d))                  # Output: '25-10-2026'
  print(utils.format_date(d, "%Y/%m/%d"))      # Output: '2026/10/25'
  ```

---

### `truncate_text`
- **Purpose**: Truncates text exceeding `max_length` and appends an ellipsis (`...`). If the text is shorter than `max_length`, it is returned unchanged.
- **Parameters**:
  - `text` (*str*): The input string to shorten.
  - `max_length` (*int*): Maximum allowed length including the 3-character ellipsis.
- **Return Value**:
  - *str*: Truncated string with `...` appended, or original string.
- **Possible Exceptions**:
  - `TypeError`: Raised if `text` is not a string or `max_length` is not an integer.
  - `ValueError`: Raised if `max_length < 3`.
- **Example Usage**:
  ```python
  import utils

  print(utils.truncate_text("Modular programming makes code reusable.", 20))
  # Output: 'Modular programm...'

  print(utils.truncate_text("Short text", 20))
  # Output: 'Short text'
  ```

---

## 3. Calculation Utilities

### `calculate_average`
- **Purpose**: Calculates the arithmetic mean of an iterable of numbers.
- **Parameters**:
  - `numbers` (*list[int | float]*): Sequence of numbers.
- **Return Value**:
  - *float*: The average value.
- **Possible Exceptions**:
  - `ValueError`: Raised if `numbers` is empty (`len == 0`).
  - `TypeError`: Raised if `numbers` is not a list/tuple or contains non-numeric items.
- **Example Usage**:
  ```python
  import utils

  print(utils.calculate_average([10, 20, 30, 40]))  # Output: 25.0

  try:
      utils.calculate_average([])
  except ValueError as err:
      print(f"Handled error: {err}")
  ```

---

### `calculate_percentage`
- **Purpose**: Calculates what percentage `part` is of `whole` using `(part / whole) * 100`.
- **Parameters**:
  - `part` (*int | float*): The portion amount.
  - `whole` (*int | float*): The total reference amount.
- **Return Value**:
  - *float*: The computed percentage.
- **Possible Exceptions**:
  - `ValueError`: Raised if `whole == 0` (division by zero guard).
  - `TypeError`: Raised if either parameter is non-numeric.
- **Example Usage**:
  ```python
  import utils

  print(utils.calculate_percentage(25, 200))  # Output: 12.5

  try:
      utils.calculate_percentage(50, 0)
  except ValueError as err:
      print(f"Handled zero division: {err}")
  ```

---

### `calculate_simple_interest`
- **Purpose**: Computes simple interest using the formula:
  $$\text{Interest} = \frac{\text{Principal} \times \text{Rate} \times \text{Time}}{100}$$
- **Parameters**:
  - `principal` (*int | float*): Initial deposit/loan amount.
  - `rate` (*int | float*): Annual interest rate percentage.
  - `time` (*int | float*): Duration in years.
- **Return Value**:
  - *float*: The total simple interest.
- **Possible Exceptions**:
  - `ValueError`: Raised if `principal`, `rate`, or `time` is negative (`< 0`).
  - `TypeError`: Raised if any argument is non-numeric.
- **Example Usage**:
  ```python
  import utils

  interest = utils.calculate_simple_interest(10000, 5, 2)
  print(interest)  # Output: 1000.0
  ```

---

### `celsius_to_fahrenheit`
- **Purpose**: Converts temperature from degrees Celsius to degrees Fahrenheit using $(C \times 9/5) + 32$.
- **Parameters**:
  - `c` (*int | float*): Temperature in Celsius.
- **Return Value**:
  - *float*: Temperature in Fahrenheit.
- **Possible Exceptions**:
  - `TypeError`: Raised if input is non-numeric.
- **Example Usage**:
  ```python
  import utils

  print(utils.celsius_to_fahrenheit(0))    # Output: 32.0
  print(utils.celsius_to_fahrenheit(100))  # Output: 212.0
  ```

---

### `fahrenheit_to_celsius`
- **Purpose**: Converts temperature from degrees Fahrenheit to degrees Celsius using $(F - 32) \times 5/9$.
- **Parameters**:
  - `f` (*int | float*): Temperature in Fahrenheit.
- **Return Value**:
  - *float*: Temperature in Celsius.
- **Possible Exceptions**:
  - `TypeError`: Raised if input is non-numeric.
- **Example Usage**:
  ```python
  import utils

  print(utils.fahrenheit_to_celsius(32))   # Output: 0.0
  print(utils.fahrenheit_to_celsius(212))  # Output: 100.0
  ```

---

### `is_prime`
- **Purpose**: Checks whether an integer $n > 1$ is prime (has no divisors other than 1 and itself). Uses $6k \pm 1$ square root optimization.
- **Parameters**:
  - `n` (*int*): The integer to test.
- **Return Value**:
  - *bool*: `True` if $n$ is prime; `False` otherwise.
- **Possible Exceptions**:
  - `TypeError`: Raised if $n$ is not an integer.
- **Example Usage**:
  ```python
  import utils

  print(utils.is_prime(2))    # Output: True
  print(utils.is_prime(17))   # Output: True
  print(utils.is_prime(4))    # Output: False
  print(utils.is_prime(1))    # Output: False
  ```

---

### `factorial`
- **Purpose**: Computes $n! = n \times (n-1) \times \dots \times 1$ iteratively for non-negative integers.
- **Parameters**:
  - `n` (*int*): Non-negative integer ($0! = 1$).
- **Return Value**:
  - *int*: The computed factorial value.
- **Possible Exceptions**:
  - `ValueError`: Raised if $n < 0$.
  - `TypeError`: Raised if $n$ is not an integer.
- **Example Usage**:
  ```python
  import utils

  print(utils.factorial(0))  # Output: 1
  print(utils.factorial(5))  # Output: 120

  try:
      utils.factorial(-3)
  except ValueError as err:
      print(f"Handled error: {err}")
  ```

---

## 4. File Utilities

### `read_file`
- **Purpose**: Safely opens and reads an entire text file using UTF-8 encoding.
- **Parameters**:
  - `path` (*str | Path*): Path to the target file.
- **Return Value**:
  - *str*: Complete string contents of the file.
- **Possible Exceptions**:
  - `FileNotFoundError`: Raised if the file does not exist.
  - `IsADirectoryError`: Raised if `path` is a directory instead of a file.
- **Example Usage**:
  ```python
  import utils

  content = utils.read_file("sample_data.txt")
  print(content)
  ```

---

### `write_file`
- **Purpose**: Writes text content to a file using UTF-8 encoding, overwriting any previous content. Automatically creates any missing parent directories.
- **Parameters**:
  - `path` (*str | Path*): Destination path.
  - `content` (*str*): Text to write.
- **Return Value**:
  - *None*
- **Possible Exceptions**:
  - `TypeError`: Raised if `content` is not a string.
- **Example Usage**:
  ```python
  import utils

  utils.write_file("output.txt", "Initial file content.\n")
  ```

---

### `append_to_file`
- **Purpose**: Appends text content to the end of a file in UTF-8 mode. Creates the file and parent folders if they do not yet exist.
- **Parameters**:
  - `path` (*str | Path*): Destination path.
  - `content` (*str*): Text to append.
- **Return Value**:
  - *None*
- **Possible Exceptions**:
  - `TypeError`: Raised if `content` is not a string.
- **Example Usage**:
  ```python
  import utils

  utils.append_to_file("output.txt", "Appended line.\n")
  ```

---

### `file_exists`
- **Purpose**: Checks whether a path exists on the filesystem and is a regular file.
- **Parameters**:
  - `path` (*str | Path*): Target path.
- **Return Value**:
  - *bool*: `True` if it exists and is a file; `False` otherwise.
- **Possible Exceptions**: None. Invalid path types safely return `False`.
- **Example Usage**:
  ```python
  import utils

  if utils.file_exists("sample_data.txt"):
      print("File is ready for processing!")
  ```

---

### `count_lines`
- **Purpose**: Streams through a text file line-by-line using UTF-8 encoding and counts total lines. Memory-efficient for files of any size.
- **Parameters**:
  - `path` (*str | Path*): File path.
- **Return Value**:
  - *int*: Number of lines in the file.
- **Possible Exceptions**:
  - `FileNotFoundError`: Raised if target file does not exist.
- **Example Usage**:
  ```python
  import utils

  lines = utils.count_lines("sample_data.txt")
  print(f"Total lines: {lines}")
  ```

---

### `get_file_extension`
- **Purpose**: Extracts and returns the lowercase file extension including the leading dot.
- **Parameters**:
  - `path` (*str | Path*): File name or path.
- **Return Value**:
  - *str*: Lowercase extension (e.g., `".txt"`, `".py"`), or `""` if none exists.
- **Possible Exceptions**: None.
- **Example Usage**:
  ```python
  import utils

  print(utils.get_file_extension("archive.tar.GZ"))  # Output: '.gz'
  print(utils.get_file_extension("document.PDF"))     # Output: '.pdf'
  print(utils.get_file_extension("Makefile"))         # Output: ''
  ```

---

## Summary

The `utils.py` module demonstrates how writing modular, single-responsibility functions with strong docstrings, type annotations, and exception handling creates reliable software foundations that simplify application development in `main.py`.
