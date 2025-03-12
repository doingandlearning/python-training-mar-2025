class InvalidMeasurementError(Exception):
    def __init__(self, experiment_id, value):
        super().__init__(f"Invalid measurement in experiment {experiment_id}: {value}")
        self.experiment_id = experiment_id
        self.value = value

def process_measurements(measurements):
    """
    Processes a list of scientific measurements.

    :param measurements: List of (experiment_id, value) tuples.
    :return: Processed data summary.
    """
    total = 0
    count = 0

    for experiment_id, value in measurements:
        try:
            if not isinstance(value, (int, float)):
                raise TypeError(f'Invalid value "{value}" in experiment {experiment_id}. Must be a number.')
            if value < 0:
                raise InvalidMeasurementError(experiment_id, value)
            total += value  # Potential TypeError if value is not a number
            count += 1
        except TypeError as e:
            print(f"Error: {e}")
        except InvalidMeasurementError as e:
            print(f"Error: {e}")

    try:
        average = total / count  # Potential ZeroDivisionError if count is zero
    except ZeroDivisionError:
        print("Error: No valid measurements to process.")
        return None
    else:
        return f"Processed {count} measurements. Average value: {average:.2f}"
    finally:
        print("Processing complete.")

# Test Cases (Some have issues)
data_samples = [
    ("EXP001", 23.4),
    ("EXP002", "invalid"),  # This will cause a TypeError
    ("EXP003", 18.7),
    ("EXP004", -10)
]

print(process_measurements(data_samples))  # Run this and see what happens!
print(process_measurements([]))