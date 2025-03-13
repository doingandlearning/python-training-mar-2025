class ExperimentResult:
    def __init__(self, experiment_id, measurement, unit, timestamp):
        self.experiment_id = experiment_id
        self.measurement = measurement
        self.unit = unit
        self.timestamp = timestamp

    def __str__(self):
        return f"Experiment {self.experiment_id}: {self.measurement} {self.unit} at {self.timestamp}"

    def __repr__(self):
        return f"ExperimentResult({self.experiment_id}, {self.measurement}, {self.unit}, {self.timestamp})"

    def to_list(self):
        return [self.experiment_id, self.measurement, self.unit, self.timestamp]

    def to_dict(self):
        return {
            "class_name_1": {
                "experiment_id": self.experiment_id,
                "measurement": self.measurement,
                "unit": self.unit,
                "timestamp": self.timestamp},
            "class_name_2": {

            }
            }

    def to_standard_format(self):
        return ""