with open('day-08/input.txt', 'r') as file:
    signals = file.readlines()

def find(patterns):
    one = (next(p for p in patterns if len(p) == 2))
    seven = (next(p for p in patterns if len(p) == 3))
    four = (next(p for p in patterns if len(p) == 4))
    eight = (next(p for p in patterns if len(p) == 7))
    nine = (next(p for p in patterns if len(p) == 6 and all(x in p for x in four)))
    zero = (next(p for p in patterns if len(p) == 6 and p != nine and all(x in p for x in one)))
    six = (next(p for p in patterns if len(p) == 6 and p != zero and p != nine))
    three = (next(p for p in patterns if len(p) == 5 and all(x in p for x in one)))
    five = (next(p for p in patterns if len(p) == 5 and p != three and all(x in nine for x in p)))
    two = (next(p for p in patterns if len(p) == 5 and p != five and p != three))
    
    return [zero, one, two, three, four, five, six, seven, eight, nine]


answer1, answer2 = 0, 0
sort = lambda x: "".join(sorted(x))

for signal in signals:
    patterns = signal.rstrip('\n').split(' ')[:10]
    output = signal.rstrip('\n').split(' ')[11:]

    patterns = list(map(sort, patterns))
    output = list(map(sort, output))
    patterns = find(patterns)
    
    answer1 += sum(1 for val in output if val in [patterns[i] for i in [1,4,7,8]])
    answer2 += int("".join([str(patterns.index(o)) for o in output]))

print(answer1, answer2)
