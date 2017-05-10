__author__ = "Maximilian Rasch"

def calc_latency(latency):
    sum = 0
    i = 0
    for item in latency:
        sum = sum + item
        i += 1
    return round(sum / i, 6)