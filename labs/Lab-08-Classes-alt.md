# **Lab: Implementing and Working with Classes in Python - Scientific Dataset Analysis**

## **Objective**
This lab will reinforce **Object-Oriented Programming (OOP)** concepts by building a class that models **scientific dataset records**. You will:
1. Define a **class** with attributes and methods.
2. Create **instances** of the class.
3. Override the **`__str__`** and **`__repr__`** methods.
4. Modify attributes and observe assignment behavior.
5. Implement methods for **data analysis and manipulation**.

---

## **Scenario: Tracking Sensor Readings**
In many scientific experiments, data is collected from **sensors** at regular intervals. These readings need to be stored, processed, and analyzed.

You will implement a **`SensorReading`** class that models individual readings from an environmental sensor.

---

## **Task 1: Define the `SensorReading` Class**
1. Create a class named **`SensorReading`**.
2. Define the **`__init__`** method with:
   - `sensor_id` (string)
   - `timestamp` (string, e.g., `"2025-03-11 14:30:00"`)
   - `value` (float)
   - `units` (string, e.g., `"°C"` for temperature or `"ppm"` for gas concentration)

---

## **Task 2: Implement Instance Methods**
1. **Format the Output**  
   - Override `__str__` to return:  
     `"Sensor {{ sensor_id }} at {{ timestamp }}: {{ value }} {{ units }}"`

2. **Checking Threshold Violations**  
   - Implement `is_above_threshold(self, threshold: float) -> bool`  
     - Returns `True` if `value > threshold`, otherwise `False`.

---

## **Task 3: Modify and Analyze Data**
1. **Modify Sensor Readings**
   - Implement `adjust_reading(self, correction: float)` to add/subtract a correction factor to `value`.

2. **Tracking Assignments**
   - Show what happens when an object is assigned to another variable:
     ```python
     r1 = SensorReading("TEMP_001", "2025-03-11 14:30:00", 22.5, "°C")
     r2 = r1
     r2.value = 25.0
     ```
     - Print `r1` and `r2`. What happens? Why?

---

## **Task 4: Work with Multiple Sensor Readings**
1. Create a **list** of multiple `SensorReading` objects.
2. Use **list comprehensions** to:
   - Print all readings.
   - Filter readings **above a given threshold**.
   - Adjust all readings by a correction factor.
  
---

### **Expected Example Usage**
```python
r1 = SensorReading("TEMP_001", "2025-03-11 14:30:00", 22.5, "°C")
r2 = SensorReading("CO2_002", "2025-03-11 14:31:00", 450.0, "ppm")

print(r1)  # Output: Sensor TEMP_001 at 2025-03-11 14:30:00: 22.5 °C
print(r2.is_above_threshold(400))  # Output: True

r1.adjust_reading(-2.5)
print(r1)  # Output: Sensor TEMP_001 at 2025-03-11 14:30:00: 20.0 °C
```

---

### **Final Deliverables**
- **Your `SensorReading` class definition.**
- **A script that creates multiple sensor readings, processes them, and prints results.**
- **Reflections on object assignment and modification behavior.**

