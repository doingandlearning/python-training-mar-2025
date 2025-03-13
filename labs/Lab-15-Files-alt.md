# **Lab: Working with Files in Python**

### **Objective**
In this lab, you will:
✅ Read data from a **CSV file**  
✅ Store the data in **class instances**  
✅ Handle **missing or malformed data**  
✅ Use **Python's built-in CSV module**  

---

## **📌 Steps to Complete**
1. **Create `loader.py`**
2. **Create the data file (`data.csv`)**
3. **Prompt the user for a filename**
4. **Load the data from the file**
5. **Invoke the `load_data()` function**
6. **Display the loaded data**

---

## **1️⃣ Step 1: Create `loader.py`**
- Create a **new Python file** called `loader.py`.
- Import the **CSV module**.
- Define a **class `TemperatureReading`**. You can use this one or your own versions:

```python
class TemperatureReading:
    """Class representing temperature info"""

    def __init__(self, temp, date, location, scale="Celsius"):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale

    def __str__(self):
        return f"TemperatureReading[{self.scale}]({self.temp} on {self.date} at {self.location})"

    def __repr__(self):
        return f"TemperatureReading({self.temp}, {self.date}, {self.location}, {self.scale})"
```

---

## **2️⃣ Step 2: Create the Data File (`data.csv`)**
- Create a **CSV file** called `data.csv` in the same directory as `loader.py`.
- Add **temperature readings** in the format:
  ```
  13.5,Celsius,01/05/20,London
  12.6,Celsius,02/05/20,London
  15.3,Celsius,03/05/20,London
  ```

📌 **Your Task:**
- Add at least **7 readings** to simulate real data.

---

## **3️⃣ Step 3: Prompt the User for a Filename**
- Modify `loader.py` to prompt the user for a **filename to load**.
- If the user enters nothing, **default to `"data.csv"`**.

📌 **Your Task:**
- Use `input()` to prompt the user.
- Use `.strip()` to handle accidental spaces in input.
- If the user provides **no input**, set a **default filename**.

---

## **4️⃣ Step 4: Load the Data from the File**
- Write a **function** `load_data(filename)` that:
  - **Opens the file** in **read mode**.
  - Uses the **CSV module** to **read the data**.
  - **Iterates over the rows** and creates `TemperatureReading` instances.
  - **Skips malformed rows** (missing columns, invalid values).

📌 **Your Task:**
- Use `with open()` to open the file.
- Use `csv.reader()` to process the file.
- Convert the **temperature value to a float**.
- Handle **invalid rows** by printing `"Skipping malformed row: ..."`.
- Return a **list of `TemperatureReading` objects**.

---

## **5️⃣ Step 5: Invoke the `load_data()` Function**
- Call `load_data(filename)` and store the result in `temperatures`.
- Display the **number of readings loaded**.

📌 **Your Task:**
- Print `"Loaded X temperature readings"`, where `X` is the count of readings.

---

## **6️⃣ Step 6: Display the Loaded Data**
- Iterate through the **list of `TemperatureReading` objects**.
- Print each reading **using the `__str__()` method**.

📌 **Your Task:**
- Use a **for loop** to print each reading.

---

## **🚀 Final Deliverables**
✔ `loader.py` (Python script to read and process temperature data)  
✔ `data.csv` (Sample temperature dataset)  
✔ Handled missing or malformed data  
✔ Displayed temperature readings correctly  

---

## **🔹 Possible extensions**
Would you like to:
1. **Filter temperature readings** (e.g., only show values above 15°C)?
2. **Save processed readings back to a CSV file**?
3. **Convert Celsius to Fahrenheit dynamically**?
