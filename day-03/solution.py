g_rate = ""  # gamma_rate
e_rate = ""  # epsilon_rate

with open("day-03/input.txt", "r") as file:
    report = file.read().split()
    bitLength = len(report[0])

# PART-1

i = 0

while i < bitLength:
    bits = [f[i] for f in report]
    if bits.count("0") > bits.count("1"):
        g_rate += "0"
    else:
        g_rate += "1"
    i += 1

# Flip bits

for bit in g_rate:
    if bit == "0":
        e_rate += "1"
    else:
        e_rate += "0"

print(int(g_rate, 2) * int(e_rate, 2))


# PART-2

elements = len(report[0])


def oxy():
    source = report.copy()
    for i in range(elements):
        if len(source) == 1:
            break
        line1 = []
        line0 = []
        for line in source:
            if line[i] == "1":
                line1.append(line)
            else:
                line0.append(line)

        if len(line1) >= len(line0):
            source = line1.copy()
        else:
            source = line0.copy()

    return source[0]


def co2():
    source = report.copy()
    for i in range(elements):
        if len(source) == 1:
            break
        line1 = []
        line0 = []
        for line in source:
            if line[i] == "1":
                line1.append(line)
            else:
                line0.append(line)

        if len(line1) < len(line0):
            source = line1.copy()
        else:
            source = line0.copy()

    return source[0]


print(int(oxy(), 2) * int(co2(), 2))
