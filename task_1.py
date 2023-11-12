# TODO решите задачу
import json


def task() -> float:
    summ = 0
    filename = "input.json"
    key_score = "score"
    key_weight = "weight"
    with open(filename) as file:
        data = json.load(file)
    for pair in data:
        summ += pair[key_score] * pair[key_weight]
    return round(summ, 3)


print(task())
