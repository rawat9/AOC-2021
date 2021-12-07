from math import floor
from statistics import median, mean


with open("day-07/input.txt", "r") as file:
    positions = list(map(int, file.read().rstrip("\n").split(",")))

# PART-1
def least_fuel():
    pos = int(median(positions))
    return sum(map(lambda x: abs(x - pos), positions))


# PART-2
def least_fuel2():
    pos = floor(mean(positions))
    cost = lambda n: n * (n + 1) // 2
    return sum(map(lambda x: cost(abs(x - pos)), positions))


print(least_fuel(), least_fuel2())
