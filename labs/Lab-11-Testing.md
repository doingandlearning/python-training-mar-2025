# **Lab: Testing a Weather Data Processing Module with `pytest`**  

## **📌 Objective**
In this lab, you will:
1. **Write unit tests using `pytest`** for a weather data processing module.
2. **Use function-based testing without fixtures**.
3. **Write parameterized tests for multiple test cases**.
4. **Test for exceptions and edge cases**.
5. **Ignore tests that are under development**.

---

## **🔬 Scenario: Weather Data Processing**
Your team at **CERN** is working with **weather station data**. You need to test a module that:
- Converts **Celsius to Fahrenheit**.
- Calculates the **average temperature** from a dataset.
- Identifies **temperature anomalies**.

---

## **🛠 Task 1: Implement `weather.py` (Starter Code, No Tests Yet)**
Create a file called **`weather.py`** and add the following code:
```python
"""Weather data processing module."""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def average_temperature(temperatures):
    """Calculate the average temperature from a list."""
    if not temperatures:
        raise ValueError("Temperature list cannot be empty")
    return sum(temperatures) / len(temperatures)

def detect_anomalies(temperatures, threshold):
    """
    Identify temperature anomalies.
    Returns a list of temperatures that exceed the threshold.
    """
    return [temp for temp in temperatures if abs(temp) > threshold]
```

---

## **🛠 Task 2: Write Basic Tests for `weather.py`**
Create a separate test file **`test_weather.py`** in the same directory.

📌 **Basic Test Cases**
```python
import pytest
from weather import celsius_to_fahrenheit, average_temperature, detect_anomalies

def test_celsius_to_fahrenheit():
    pass

def test_average_temperature():
    pass

def test_average_temperature_empty_list():
    pass

```
✅ **Run the Tests**
```bash
pytest test_weather.py
```

---

## **🛠 Task 3: Parameterized Tests**
Instead of writing separate tests for each input, use `@pytest.mark.parametrize`.

📌 **Modify `test_weather.py`**
```python
def test_celsius_to_fahrenheit_param(celsius, expected):
  pass
```
✅ **Run the Tests**
```bash
pytest test_weather.py
```

---

## **🛠 Task 4: Test for Anomalies**
Now, test the `detect_anomalies()` function.

📌 **Add This to `test_weather.py`**
```python
def test_detect_anomalies():
    pass
```
✅ **Run the Tests**
```bash
pytest test_weather.py
```

---

## **🛠 Task 5: Ignore a Test**
While working on a **new function**, you may want to **skip its test**.

📌 **Modify `test_weather.py`**
```python
def test_future_feature():
    assert False  # Placeholder for future test
```
✅ **Run Tests and Observe Skipped Test**
```bash
pytest -v
```
🔹 **Expected Output**
```text
SKIPPED [1] test_weather.py::test_future_feature - Function not implemented yet
```

---

## **✅ Final Deliverables**
✔ `weather.py` (Temperature conversion, averaging, anomaly detection)  
✔ `test_weather.py` (Function-based testing with `pytest`)  
✔ **Parameterized tests**  
✔ **Exception handling tests**  
✔ **Skipped tests for work-in-progress features**  

---

## **🚀 Workshop Wrap-Up**
### **Key Takeaways**
- ✅ **Use `pytest` for function-based testing**.
- ✅ **Test multiple inputs with `@pytest.mark.parametrize`**.
- ✅ **Write tests that check for exceptions**.
- ✅ **Skip tests that are under development**.


