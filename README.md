*Developed as part of the 42 Python curriculum by rosvela.*

# Garden Management System

This project is a series of exercises designed to progressively teach **object-oriented programming (OOP) concepts** in Python, applied to a garden management context. Each exercise builds on the previous, introducing new concepts and techniques.

---

## Exercises Overview

### Exercise 0: Basic Plant Information
- Introduces variables to store plant data (`name`, `height`, `age`).
- Displays information using `print`.
- No classes are used in this stage.

### Exercise 1: Plant Class and Object Instantiation
- Introduces the `Plant` class.
- Implements methods to display plant information.
- Demonstrates creating multiple objects and storing them in a list.

### Exercise 2: Plant Growth and Aging
- Adds methods to modify plant attributes: `grow()` and `age()`.
- Demonstrates mutability and state changes of objects over time.

### Exercise 3: Plant Factory
- Implements a factory function to create multiple plants efficiently.
- Streamlines plant creation and initialization.
- Demonstrates using tuples and iteration to generate multiple objects dynamically.

### Exercise 4: SecurePlant – Encapsulation
- Introduces `SecurePlant` with protected attributes (`_height`, `_age`).
- Provides safe getter and setter methods with validation.
- Demonstrates encapsulation and error handling for invalid data.

### Exercise 5: Specialized Plant Types
- Implements inheritance: `Plant` → `Flower`, `Tree`, `Vegetable`.
- Each subclass adds unique attributes and behaviors.
- Demonstrates **polymorphism** with the `act()` method.

### Exercise 6: Garden Analytics
- Implements `GardenManager` to handle multiple gardens.
- Includes a nested `GardenStats` class for statistics.
- Demonstrates use of instance, class, and static methods.
- Tracks plant growth, counts plant types, and validates heights.
- Combines inheritance, polymorphism, and system-wide analytics.

---

## Key Concepts Learned
- **Classes and Objects**: Creating reusable object structures.
- **Inheritance**: Extending base classes for specialized behaviors.
- **Encapsulation**: Protecting sensitive data with getter/setter methods.
- **Polymorphism**: Using the same interface (`act()`) for different behaviors.
- **Class and Static Methods**: Performing operations at the class level or as utilities.
- **System Design**: Organizing complex programs using nested classes and multiple interacting components.

---

## Running the Programs

Each exercise has its own Python script:

```bash
python3 ex0.py
python3 ex1.py
python3 ex2.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py