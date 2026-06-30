*Developed as part of the 42 Python curriculum by rosvela.*

# Python Fundamentals: Growing Code 🪴

This repository contains the solutions for the **Growing Code** project. The focus is on mastering Python's fundamental syntax, data types, and control flow through a community garden data lens, while maintaining a professional DevOps workflow.

## 🛠️ DevOps Pipeline: `check.sh`

To ensure code quality and compliance with **42** standards and **Flake8** (PEP 8) rules, I have implemented a local CI (Continuous Integration) script named `check.sh`.

### Key Features

1.  **Environment Cleanup**: Automatically removes `__pycache__` directories and temporary files to ensure a clean testing state.
2.  **Linting (Style Validation)**: Runs `flake8` across the entire project. It enforces PEP 8 compliance (indentation, line length, blank lines, and docstrings).
3.  **Ephemeral Environment Management**: Creates **Symbolic Links (symlinks)** for all exercise files (`ex0/` through `ex7/`) in the root directory. This allows the `main.py` helper to access all functions without duplicating or moving source files.
4.  **Automated Testing**: Once the style check passes, it automatically launches the `main.py` test suite to verify logic.

### How to Use

Run the pipeline from the root of the repository:

```bash
# Grant execution permissions (first time only)
chmod +x check.sh

# Run the quality and test pipeline
./check.sh

```
## Project Structure

. ex0/ to ex7/: Individual directories for each exercise as per the subject requirements.

. check.sh: Automation script for quality assurance and environment setup.

. main.py: Official 42 helper resource for logic validation.

## Technical Highlights

. Type Annotations: Implemented in Exercise 7 to ensure robust data handling, similar to TypeScript standards.

. Recursion vs Iteration: Exercise 5 explores different algorithmic approaches to data processing.

. Clean Code: Strict adherence to PEP 8 using automated linting.

