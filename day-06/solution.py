with open("day-06/input.txt", "r") as file:
    file = file.read().split("\n")

initial = list(map(int, file[0].split(",")))


def count_fishes(state, days):
    day = 0
    while day < days:
        state += [9] * state.count(0)
        state = list(map(lambda x: 6 if x == 0 else x - 1, state))
        day += 1

    return len(state)


memo = {}


def func(state):
    total = 0
    for state in initial:
        if state in memo:
            total += memo[state]
        else:
            result = count_fishes([state], 80)
            memo[state] = result
            total += memo[state]
    return total


print(func(set(initial)))
