with open('day-1/input.txt', 'r') as f:
    arr = []
    for line in f:
        arr.append(int(line.rstrip('\n')))


# PART-1

def part_one(arr):
    countDepth = 0
    first = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > first:
            countDepth += 1
        first = arr[i]
    
    return countDepth

print(part_one(arr))


# PART-2

def part_two(arr):
    for i in range(len(arr)-2):
        arr[i] = arr[i] + arr[i+1] + arr[i+2]

    return part_one(arr[:-2])

print(part_two(arr))
