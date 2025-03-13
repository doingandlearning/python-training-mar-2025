# JavaScript Object Notation
import json
from experiment_result import ExperimentResult

experiment1 = ExperimentResult("EXP001", 12.5, "mg/L", "2025-03-10 14:30:00")
experiment2 = ExperimentResult("EXP002", 7.8, "ppm", "2025-03-11 10:15:00")
experiment3 = ExperimentResult("EXP003", 22.1, "mm", "2025-03-11 15:30:00")

results = [experiment1, experiment2, experiment3]

print([result.to_dict() for result in results])


print(json.dumps([result.to_dict() for result in results]))

# with open("results.json", "w") as file:
#     file.write(json.dumps([result.to_dict() for result in results]))

with open("results.json") as file:
    result_dict = json.loads(file.read())
    print(result_dict)

    print([ExperimentResult(**result) for result in result_dict])  # concise way to unpack
    print([ExperimentResult(experiment_id=result["experiment_id"],
                            measurement=result["measurement"],
                            unit=result["unit"],
                            timestamp=result["timestamp"]) for result in result_dict])

def demo_of_kwargs(name, lives_in, experience):
    print(f"{name} lives in {lives_in} and has experience with {experience}")

test_dict = {"name": "Sally", "lives_in": "Geneva", "experience": ["Matlab", "Materials Eng"]}
demo_of_kwargs(**test_dict)
