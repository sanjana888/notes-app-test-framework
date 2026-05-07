import time
import csv
import os

def measure_execution_time(function):
    start = time.time()
    result = function()
    end = time.time()
    return result, round(end - start, 2)

def log_performance(metric_name, value):
    os.makedirs("reports", exist_ok=True)

    file_path = "reports/performance_trend.csv"
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Metric", "Value"])

        writer.writerow([metric_name, value])