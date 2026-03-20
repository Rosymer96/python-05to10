# Garden Management System
*Developed as part of the 42 Python curriculum by rosvela.*

This project is a series of exercises designed to progressively teach **object-oriented programming (OOP) concepts** in Python, applied to a garden management context. Each exercise builds on the previous, introducing new concepts and techniques.

---

## Exercises Overview

### Exercise 0: Basic Plant Information (`ex0/ft_garden_intro.py`)
- Introduces variables to store plant data (`name`, `height`, `age`).
- Displays information using `print`. No classes are used in this stage.

### Exercise 1: Plant Class and Object Instantiation (`ex1/ft_garden_data.py`)
- Introduces the `Plant` class.
- Implements methods to display plant information.
- Demonstrates creating multiple objects and storing them in a list.

### Exercise 2: Plant Growth and Aging (`ex2/ft_plant_growth.py`)
- Adds methods to modify plant attributes: `grow()` and `age()`.
- Demonstrates mutability and state changes of objects over time.

### Exercise 3: Plant Factory (`ex3/ft_plant_factory.py`)
- Implements a factory function to create multiple plants efficiently.
- Demonstrates using tuples and iteration to generate objects dynamically.

### Exercise 4: SecurePlant – Encapsulation (`ex4/ft_garden_security.py`)
- Introduces protected attributes (`_height`, `_age`).
- Provides safe getter and setter methods with validation.
- Demonstrates encapsulation and error handling for invalid data.

### Exercise 5: Specialized Plant Types (`ex5/ft_plant_types.py`)
- Implements inheritance: `Plant` → `Flower`, `Tree`, `Vegetable`.
- Each subclass adds unique attributes and behaviors.
- Demonstrates **polymorphism** with the `act()` method.

### Exercise 6: Garden Analytics (`ex6/ft_garden_analytics.py`)
- Implements `GardenManager` to handle multiple gardens (Alice, Bob, etc.).
- Includes `@classmethod` for global states and `@staticmethod` for utilities.
- Tracks growth, counts plant types, and validates system-wide data.

---

## Validation and Style

To ensure the code meets **42 standards** (PEP 8 and static typing), a custom validation script is included.

### Requirements
You must have `flake8` and `mypy` installed:
```bash
python3 -m pip install flake8 mypy
```
### Using the Validator
The `check.sh` script automatically verifies file naming, code style (PEP 8), and type integrity (Mypy) across all exercises to ensure they meet **42 standards**:

#### Give execution permissions
```bash
chmod +x check.sh
```
#### Run the validation suite
```bash
./check.sh
```

## Key Concepts Learned

- **Classes and Objects**: Defining blueprints for data structures and creating multiple independent instances.
- **Inheritance**: Creating a hierarchy where specialized classes (`Flower`, `Tree`) inherit and extend the attributes and methods of a base class (`Plant`).
- **Encapsulation**: Protecting internal object state by using protected attributes (`_height`) and providing controlled access through getter and setter methods with data validation.
- **Polymorphism**: Implementing a common interface (`act()`) across different classes, allowing the system to trigger specific behaviors (blooming, providing shade) through the same method call.
- **Class and Static Methods**: 
  - **Class Methods**: Managing data that belongs to the class


---

## Running the Programs

Each exercise can be executed individually from the root directory:

```bash
python3 ex0/ft_garden_intro.py
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py