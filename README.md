# Python Utility Module (`python-utility-module`)

> **Level 1 Python Internship — Day 25: Create a Python Utility Module**  
> *A modular, beginner-friendly Python utility library demonstrating code reuse, clean architecture, and defensive programming.*

---

## 🎯 Learning Objectives

The primary goal of this project is to master **modular programming** and **code reuse** in Python using exclusively the Python Standard Library:
- **Separation of Concerns**: Organizing reusable functions into a standalone library module (`utils.py`) separate from client/driver code (`main.py`).
- **Single Responsibility Principle (SRP)**: Ensuring each function performs a single, well-defined task.
- **Defensive Programming & Error Handling**: Gracefully managing edge cases (e.g., division by zero, empty collections, missing files, negative inputs) via explicit exceptions (`ValueError`, `TypeError`, `FileNotFoundError`).
- **Self-Testing Modules**: Embedding executable unit/regression checks within `utils.py` using `if __name__ == "__main__":` blocks.
- **Type Annotations & PEP 8 Compliance**: Using type hints and clear docstrings to make the library accessible and maintainable.

---

## 📂 Project Structure

```text
python-utility-module/
├── utils.py          # The reusable utility module (23 functions across 4 sections)
├── main.py           # Example driver program with interactive menu & automated demo
├── sample_data.txt   # Sample data file used by file utilities demonstrations
├── DOCUMENTATION.md  # Exhaustive reference documentation for every function
├── README.md         # Project overview, installation, how-to-run, and sample output
└── .gitignore        # Ignores byte-compiled artifacts and temporary test files
```

---

## 🛠️ Function Categories

The module is divided into 4 clearly commented sections:

### 1. Validation Utilities
- `is_valid_email(email)`: Validates email address format (`name@domain.ext`).
- `is_valid_phone(phone)`: Validates 10-digit Indian mobile numbers (starts with 6–9, supports `+91` / `0` prefixes).
- `is_positive_number(value)`: Checks if a numeric value is strictly greater than 0 (excludes booleans).
- `is_non_empty_string(text)`: Checks if a string contains visible non-whitespace characters.
- `is_in_range(value, low, high)`: Checks if `low <= value <= high` (raises `ValueError` if `low > high`).

### 2. Formatting Utilities
- `format_currency(amount, symbol="₹")`: Formats numbers into currency strings with commas and 2 decimals.
- `format_percentage(value, decimals=2)`: Formats numbers into percentage strings with custom precision.
- `to_title_case(text)`: Capitalizes the first letter of each word in a string.
- `format_date(date_obj, fmt="%d-%m-%Y")`: Converts `date` or `datetime` objects to formatted strings.
- `truncate_text(text, max_length)`: Shortens strings exceeding `max_length` and appends `...`.

### 3. Calculation Utilities
- `calculate_average(numbers)`: Calculates arithmetic mean; raises `ValueError` on empty sequences.
- `calculate_percentage(part, whole)`: Returns what percentage `part` is of `whole`; raises `ValueError` on zero denominator.
- `calculate_simple_interest(principal, rate, time)`: Calculates `(P * R * T) / 100`; raises `ValueError` on negative values.
- `celsius_to_fahrenheit(c)`: Converts temperature from Celsius to Fahrenheit.
- `fahrenheit_to_celsius(f)`: Converts temperature from Fahrenheit to Celsius.
- `is_prime(n)`: Determines if an integer `n > 1` is prime using $6k \pm 1$ optimization.
- `factorial(n)`: Computes factorial `n!`; raises `ValueError` if $n < 0$.

### 4. File Utilities
- `read_file(path)`: Reads and returns text content using UTF-8 and `with` statements; handles missing files.
- `write_file(path, content)`: Overwrites file with string content; auto-creates parent folders.
- `append_to_file(path, content)`: Appends string content to a file.
- `file_exists(path)`: Returns `True` if path points to an existing regular file.
- `count_lines(path)`: Streams file to count total lines safely and efficiently.
- `get_file_extension(path)`: Extracts lowercase extension (e.g., `.txt`, `.py`).

> For full signatures, parameters, return types, and exceptions, see **[DOCUMENTATION.md](DOCUMENTATION.md)**.

---

## 🚀 How to Run

### Requirements
- **Python 3.8+**
- No third-party packages required (Standard Library only).

### 1. Run the Interactive Main Program
Launches a menu-driven interface with user input handling:
```bash
python main.py
```

```text
=================================================================
             PYTHON UTILITY MODULE - MAIN MENU
=================================================================
  [1] Validation Utilities Demo
  [2] Formatting Utilities Demo
  [3] Calculation Utilities Demo
  [4] File Utilities Demo
  [5] Run All Demonstrations
  [6] Exit Program
=================================================================
Enter your choice (1-6):
```

### 2. Run All Demonstrations Automatically (Batch Mode)
Runs demonstrations for all 23 functions consecutively:
```bash
python main.py --all
```

### 3. Run the Built-in Self-Tests
Runs the comprehensive test suite embedded inside `utils.py`:
```bash
python utils.py
```

---

## 📋 Sample Terminal Output

### Output from `python utils.py`:
```text
=================================================================
           RUNNING UTILS.PY INTERNAL SELF-TEST SUITE            
=================================================================

--- 1. Validation Tests ---
 [PASS] Valid email format
 [PASS] Complex valid email
 [PASS] Invalid email missing domain
 [PASS] Invalid email missing @
 [PASS] Standard 10-digit Indian phone
 [PASS] Indian phone with +91 prefix and hyphens
 [PASS] Indian phone with 0 prefix
 [PASS] Invalid Indian phone starting with 5
 [PASS] Too short phone number
 [PASS] Positive integer
 [PASS] Positive float
 [PASS] Zero is not positive
 [PASS] Negative number is not positive
 [PASS] Boolean True is not treated as number
 [PASS] Standard non-empty string
 [PASS] Whitespace-only string is considered empty
 [PASS] Empty string
 [PASS] Value in range
 [PASS] Value at lower boundary
 [PASS] Value at upper boundary
 [PASS] Value out of range
 [PASS] is_in_range raised ValueError when low > high

--- 2. Formatting Tests ---
 [PASS] Format Indian Rupee currency
 [PASS] Format negative USD currency
 [PASS] Format percentage to 2 decimals
 [PASS] Format percentage to 0 decimals
 [PASS] Title case conversion
 [PASS] Format date to default DD-MM-YYYY
 [PASS] Truncate text with ellipsis
 [PASS] Truncate text without modification if short

--- 3. Calculation Tests ---
 [PASS] Calculate average of list
 [PASS] Calculate percentage
 [PASS] Calculate simple interest
 [PASS] Celsius 0 to Fahrenheit 32
 [PASS] Celsius 100 to Fahrenheit 212
 [PASS] Fahrenheit 32 to Celsius 0
 [PASS] Fahrenheit 212 to Celsius 100
 [PASS] 2 is prime
 [PASS] 17 is prime
 [PASS] 4 is not prime
 [PASS] 1 is not prime
 [PASS] Negative number is not prime
 [PASS] 0! is 1
 [PASS] 5! is 120
 [PASS] calculate_average raised ValueError on empty list
 [PASS] calculate_percentage raised ValueError on division by zero
 [PASS] factorial raised ValueError on negative number

--- 4. File Utility Tests ---
 [PASS] File exists after write
 [PASS] Count lines returns 2
 [PASS] Read file matches content
 [PASS] Count lines returns 3 after append
 [PASS] Get file extension returns .txt

=================================================================
SELF-TEST RESULTS: 52 / 52 PASSED
=================================================================
```

---

## 🐙 Git & GitHub Commands

Follow these step-by-step commands in your terminal to initialize the Git repository and push your project to GitHub:

### Step 1: Navigate to the project directory
```bash
cd "C:\Users\HEMA\.gemini\antigravity-ide\scratch\python-utility-module"
```

### Step 2: Initialize Git
```bash
git init
```

### Step 3: Stage and commit all project files
```bash
git add .
git commit -m "feat: complete Day 25 python utility module project"
```

### Step 4: Rename default branch to `main`
```bash
git branch -M main
```

### Step 5: Link your remote GitHub repository
Create a new public repository on GitHub named `python-utility-module` (leave "Initialize with README" unchecked), then connect it:
```bash
# Replace YOUR_GITHUB_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/python-utility-module.git
```

### Step 6: Push to GitHub
```bash
git push -u origin main
```

---

## 📜 License
Created for Level 1 Python Internship educational purposes. Free to use and distribute under the MIT License.
