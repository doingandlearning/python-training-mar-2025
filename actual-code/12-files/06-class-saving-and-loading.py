import csv
from experiment_result import ExperimentResult

experiment1 = ExperimentResult("EXP001", 12.5, "mg/L", "2025-03-10 14:30:00")
experiment2 = ExperimentResult("EXP002", 7.8, "ppm", "2025-03-11 10:15:00")
experiment3 = ExperimentResult("EXP003", 22.1, "mm", "2025-03-11 15:30:00")

results = [experiment1, experiment2, experiment3]

# Serializing

# with open("results.csv", "w") as file:
#     writer = csv.writer(file)
#     for result in results:
#         # writer.writerow([result.experiment_id, result.measurement, result.unit, result.timestamp])
#         writer.writerow(result.to_list())

# with open("results.csv", "w") as file:
#     writer = csv.DictWriter(file, fieldnames=["experiment_id", "measurement", "unit", "timestamp"])
#     writer.writeheader()
#     for result in results:
#         writer.writerow(result.to_dict())

# Deserializing

def load_experiment_results(filename="results.csv"):
    results = []
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            next(reader)  # only necessary if you have a header row!
            for row in reader:
                experiment = ExperimentResult(row[0], row[1], row[2], row[3])
                results.append(experiment)
    except FileNotFoundError:
        print("Whoops! That file doesn't exist!")
    return results

def load_experiment_results_dict(filename="results.csv"):
    results = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file, fieldnames=["experiment_id", "measurement", "unit", "timestamp"])
            next(reader)
            for row in reader:
                # experiment = ExperimentResult(row["experiment_id"], row["measurement"], row["unit"], row["timestamp"])
                experiment = ExperimentResult(**row)
                results.append(experiment)
    except FileNotFoundError:
        print("Whoops! That file doesn't exist!")
    return results

print(results)
print(load_experiment_results())
print(load_experiment_results_dict())