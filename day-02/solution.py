horizontal = 0
depth = 0

# PART-1

with open('day-2/input.txt', 'r') as file:
    for line in file:
        command, unit = line.split()

        if command == 'forward':
            horizontal += int(unit)
        elif command == 'down':
            depth += int(unit)
        else:
            depth -= int(unit)

print(horizontal * depth)


# PART-2

horizontal = 0
depth = 0
aim = 0

with open('day-2/input.txt', 'r') as file:
    for line in file:
        command, unit = line.split()

        if command == 'forward':
            horizontal += int(unit)
            depth += (aim * int(unit))
        elif command == 'down':
            aim += int(unit)
        else:
            aim -= int(unit)

print(horizontal * depth)

