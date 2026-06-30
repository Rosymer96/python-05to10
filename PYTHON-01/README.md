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

### Exercise 2: Plant Growth and Aging (`ex2/ft_plant_growth.py`)
- Adds behavioral methods to modify object state: grow() and age().
- Simulates state changes over a period of time (a week of growth).

### Exercise 3: Plant Factory (`ex3/ft_plant_factory.py`)
- Focuses on streamlining object creation using the __init__ constructor.
- Enables initializing multiple plants with specific data (name, height, age) at the moment of instantiation.

### Exercise 4: SecurePlant – Encapsulation (`ex4/ft_garden_security.py`)
- Introduces Encapsulation using protected attributes (_height, _age).
- Implements safe Getters and Setters with data validation to prevent negative values .

### Exercise 5: Specialized Plant Types (`ex5/ft_plant_types.py`)
- Implements inheritance: `Plant` → `Flower`, `Tree`, `Vegetable`.
- Each subclass adds unique attributes and behaviors.
- Demonstrates Method Overriding using super() to extend base functionality (e.g., adding color to flowers or trunk diameter to trees)


### Exercise 6: Garden Analytics (`ex6/ft_garden_analytics.py`)
- Implements Nested Classes: A Stats class inside Plant to track calls to grow, age, and show.
- Uses Static Methods (@staticmethod) for utility checks (e.g., is_older_than_year).
- Uses Class Methods (@classmethod) for factory patterns like creating anonymous plants.
- Extends the hierarchy with a Seed class inheriting from Flower.

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