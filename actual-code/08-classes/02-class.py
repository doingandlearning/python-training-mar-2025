class ExperimentResult:
    # methods -> function inside a class
    def __init__(self, date, value, experiment, unit="mm"):  # __init__ -> dunder init
        self.date = date
        self.value = value
        self.experiment = experiment
        self.unit = unit

    def __str__(self):
        return f"Experiment at {self.experiment} on {self.date} with value {self.value}{self.unit}."

    def __repr__(self):  # this
        return f"ExperimentResult({self.date}, {self.value}, {self.experiment}, {self.unit})"

    def value_in_unit(self, new_unit):
        # m, mm, cm
        if new_unit == self.unit:
            return self.value

        conversion_factors = {
            "mm": 1,
            "cm": 0.1,
            "m": 0.001
        }

        value_in_mm = self.value / conversion_factors[self.unit]
        return value_in_mm * conversion_factors[new_unit]



result1 = ExperimentResult("2025-03-10", 10, "LPC", "mm")
result2 = ExperimentResult(date="2025-03-11", value=12, experiment="LPC", unit="m")
result3 = ExperimentResult(date="2025-03-09", value=14, experiment="LHC", unit="mm")

experiment_results = [result1, result2, result3]

print([result for result in experiment_results if result.unit == "mm"])
print([result.value_in_unit("mm") for result in experiment_results])

print(list(filter(lambda r: r.experiment == "LHC", experiment_results)))



#
# print(abs(result1.value_in_unit("mm") - result2.value_in_unit("mm")))
#
# result3 = {
#     "date": "2025-03-11",
#     "value": 13,
#     "experiment": "LHC",
#     "unit": "cm"
# }
#
# # protocols ...
# print(result1)  # __str__  __repr__
# print(result2)
#
# print([result1, result2])