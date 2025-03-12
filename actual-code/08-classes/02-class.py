class ExperimentResult:
    def __init__(self, date, value, experiment, unit):  # __init__ -> dunder init
        self.date = date
        self.value = value
        self.experiment = experiment
        self.unit = unit

result1 = ExperimentResult("2025-03-10", 10, "LPC", "mm")

print(result1)
print(result1.date)
print(result1.experiment)
print(result1.value)
print(result1.unit)

