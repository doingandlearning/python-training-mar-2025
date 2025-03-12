### **Lab: Enhancing Error Handling in Scientific Data Processing**

#### **Objective**
In this lab, you'll work with a **faulty data processing function** and enhance it by:
1. **Adding try-except blocks** to catch errors.
2. **Handling multiple exceptions appropriately.**
3. **Using an `else` clause for successful execution.**
4. **Implementing a `finally` block to ensure cleanup.**
5. **Creating a custom exception for invalid data.**

---

## **🚀 Starter Code (Faulty Version)**
This function processes a list of scientific measurements but currently has **no error handling**.

```python
def process_measurements(measurements):
    """
    Processes a list of scientific measurements.
    
    :param measurements: List of (experiment_id, value) tuples.
    :return: Processed data summary.
    """
    total = 0
    count = 0

    for experiment_id, value in measurements:
        total += value  # Potential TypeError if value is not a number
        count += 1
    
    average = total / count  # Potential ZeroDivisionError if count is zero
    return f"Processed {count} measurements. Average value: {average:.2f}"

# Test Cases (Some have issues)
data_samples = [
    ("EXP001", 23.4),
    ("EXP002", "invalid"),  # This will cause a TypeError
    ("EXP003", 18.7),
]

print(process_measurements(data_samples))  # Run this and see what happens!
```

🔴 **Problem:** The function will crash if:
- A value is **not a number** (`TypeError`).
- The list is **empty** (`ZeroDivisionError`).

---

## **🛠 Task 1: Add Basic Exception Handling**
Modify `process_measurements()` to:
1. Use a `try-except` block to catch errors.
2. Print an error message instead of crashing.

---

## **🛠 Task 2: Handle Multiple Exceptions**
Enhance the function to:
1. Catch **TypeError** (invalid data values).
2. Catch **ZeroDivisionError** (no valid measurements).
3. Use `else:` to execute only when no errors occur.
4. Use `finally:` to indicate that processing is complete.

---

## **🛠 Task 3: Define a Custom Exception**
Define a **`InvalidMeasurementError`** exception and raise it if:
- A measurement **value is negative** (we assume all values must be positive).

---

## **💡 Example Usage & Expected Output**
Once your error handling is in place, your function should:
- **Handle invalid values gracefully.**
- **Still process valid data.**
- **Always print a "Processing complete" message.**

```python
data_samples = [
    ("EXP001", 23.4),
    ("EXP002", "invalid"),  # Should trigger a TypeError
    ("EXP003", -5.0),       # Should trigger InvalidMeasurementError
    ("EXP004", 18.7),
]

print(process_measurements(data_samples))
```

🔹 Expected output:
```
Error: Invalid value 'invalid' in experiment EXP002.
Error: Negative measurement value -5.0 in experiment EXP003.
Processed 2 valid measurements. Average value: 21.05
Processing complete.
```

---

## **Final Deliverables**
✅ **Updated `process_measurements()` function with exception handling**  
✅ **A custom exception for invalid measurements**  
✅ **At least two test cases that trigger errors**


