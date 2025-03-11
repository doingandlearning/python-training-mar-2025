# **Lab: Working with Higher-Order Functions in Temperature and Number Processing**

## **Objective**
The focus of this lab is to explore **higher-order functions** like `map()`, `filter()`, and lambda functions to process a list of temperatures and numbers.

You will:
1. **Convert temperatures** from Celsius to Fahrenheit using `map()`, both with a function and a lambda.
2. **Filter temperatures** above a given threshold using `filter()`.
3. **Combine `map()` and `filter()`** to transform and filter data in a single operation.
4. **Use `filter()`** to extract even numbers from a list, using both a lambda function and a named function.

---

## **Tasks**
### **1. Temperature Conversion Using `map()`**
- Given a list of temperatures in Celsius, use `map()` to convert them to Fahrenheit.
- Implement this in **two ways**:
  1. Using a **named function**.
  2. Using a **lambda function**.

📌 **Hint**: The formula for Celsius to Fahrenheit is:
   \[
   F = (C \times 9/5) + 32
   \]

---

### **2. Filtering Temperatures**
- Using `filter()`, remove all temperatures **below 18°C** from the list.
- Store the filtered temperatures in a new list.

---

### **3. Combining `map()` and `filter()`**
- First, **filter** temperatures that are **above 14°C**.
- Then, **convert** these filtered values to Fahrenheit using `map()`.
- Store the result in a new list.

---

### **4. Filtering Even Numbers**
- Given a list of numbers, use `filter()` to keep only **even numbers**.
- Implement this in **two ways**:
  1. Using a **lambda function**.
  2. Using a **named function**.

---

## **Example Input and Expected Output**
Assume the input lists:

```python
temperatures = [12.5, 18.1, 15.6, 17.8, 20.1, 22.6, 18.9]
data = [1, 3, 5, 2, 7, 4, 10]
```

Expected output:
```text
[54.5, 64.58, 60.08, 64.04, 68.18, 72.68, 66.02]  # Converted Fahrenheit temps
[18.1, 20.1, 22.6, 18.9]  # Temps above threshold
[60.08, 64.04, 68.18, 72.68, 66.02]  # Filtered and converted temps
[2, 4, 10]  # Even numbers from data
```

---

## **Additional Requirements**
- **Use list comprehensions** to display results in a structured way.
- **Add docstrings** to your functions following reStructuredText format.

🔹 **Example of docstring format**:
```python
def is_even(n):
    """
    Check if a number is even.

    :param n: The number to check.
    :type n: int
    :return: True if even, False otherwise.
    :rtype: bool
    """
```


