from collections import Counter

with open('day-05/input.txt', 'r') as file:
    coords = file.read().splitlines()


def get_coords(points):
    for coord in coords:
        l = coord.split(' -> ')
        left, right = list(map(int, l[0].split(','))), list(map(int, l[1].split(',')))
        x1, y1 = left[0], left[1]
        x2, y2 = right[0], right[1]

        if y1 == y2:
            if x2 > x1:
                for x in range(x1, x2+1):
                    points.append((x, y2))
            else:
                for x in range(x1, x2-1, -1):
                    points.append((x, y2))
        elif x1 == x2:
            if y2 > y1:
                for y in range(y1, y2+1):
                    points.append((x1, y))
            else:
                for y in range(y1, y2-1, -1):
                    points.append((x1, y))
    return points


def get_coords2(points):
    for coord in coords:
        l = coord.split(' -> ')
        left, right = list(map(int, l[0].split(','))), list(map(int, l[1].split(',')))
        x1, y1 = left[0], left[1]
        x2, y2 = right[0], right[1]

        if y1 == y2:
            if x2 > x1:
                for x in range(x1, x2+1):
                    points.append((x, y2))
            else:
                for x in range(x1, x2-1, -1):
                    points.append((x, y2))
        elif x1 == x2:
            if y2 > y1:
                for y in range(y1, y2+1):
                    points.append((x1, y))
            else:
                for y in range(y1, y2-1, -1):
                    points.append((x1, y))

        # diagonal
        elif abs(x2 - x1) == abs(y2 - y1):
            for i in range(abs(x2 - x1) + 1):
                if x1 + y1 == x2 + y2:
                    points.append((min(x1, x2) + i, max(y1, y2) - i))
                else:
                    points.append((min(x1, x2) + i, min(y1, y2) + i))
    return points



answer1 = get_coords([])
answer2 = get_coords2([])
c1, c2 = Counter(answer1), Counter(answer2)

ans1 = len([v for _,v in c1.items() if v > 1])
ans2 = len([v for _,v in c2.items() if v > 1])
print(ans1, ans2)
