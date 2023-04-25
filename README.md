# **Calculator**

A simple calculator package that can perform basic arithmetic operations.

## **Installation**

You can install the package using pip:

```
pip install -i https://test.pypi.org/simple/ my_calculator1


```

## **Usage**

```
from my_calculator1 import Calculator

# Create a new calculator
calc = Calculator()

# Add two numbers
result = calc.add(2, 3)
print(result)  # Output: 5

# Add a single number to the calculator's memory
result = calc.add(2)
print(result)  # Output: 7

```

### **`Calculator()`**

The constructor for the `Calculator` class. Initializes the calculator with a memory of 0.

### **`add(num1: Optional[float], num2: Optional[float] = None) -> float`**

Adds two numbers or a single number to the calculator's memory and returns the result.

### **`subtract(num1: Optional[float], num2: Optiona[float] = None) -> float`**

Subtracts two numbers or a single number from the calculator's memory and returns the result.

### **`multiply(num1: Optional[float], num2: Optional[float] = None) -> float`**

Multiplies two numbers or a single number with the calculator's memory and returns the result.

### **`divide(num1: Optional[float], num2: Optional[float] = None) -> float`**

Divides the calculator's memory by a number or divides two numbers and returns the result.

### **`nth_root(root: int, num1: Optional[float] = None, num2: Optional[float] = None) -> float`**

Takes the nth root of a number and stores the result in the calculator's memory or takes the nth root of two numbers.

### **`reset() -> float`**

Resets the calculator's memory to 0.
