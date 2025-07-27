from typing import List
import random

# hinting that the input will be a list and the output will be a float
def average(data: list) -> float: 
    avg = sum(data) / len(data)
    return round(avg, 2)

lst = [random.randint(1, 100) for _ in range(26)]
print("Data:", lst)
print("Average:", average(lst))