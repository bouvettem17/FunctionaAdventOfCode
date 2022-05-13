import numpy as np

with open("q9.txt", "r") as f:
    heightmap = f.readlines()
    entries = [row.strip() for row in heightmap]

debugArray = np.zeros((len(entries), len(entries[0])))

lowPoints = 0
for j in range(0, len(entries)):
    for i in range(0, len(entries[j])):
        if j == 0:
            if i == 0:
                if (
                    entries[j + 1][i] > entries[j][i]
                    and entries[j][i + 1] > entries[j][i]
                ):
                    lowPoints += 1 + int(entries[j][i])
                    debugArray[j][i] = 1
            if i == len(entries[j]) - 1:
                if (
                    entries[j][i - 1] > entries[j][i]
                    and entries[j + 1][i] > entries[j][i]
                ):
                    lowPoints += 1 + int(entries[j][i])
                    debugArray[j][i] = 1
            else:
                if (
                    entries[j][i - 1] > entries[j][i]
                    and entries[j + 1][i] > entries[j][i]
                    and entries[j][i + 1] > entries[j][i]
                ):
                    lowPoints += 1 + int(entries[j][i])
                    debugArray[j][i] = 1
        elif j == len(entries) - 1:
            if i == 0:
                if (
                    entries[j - 1][i] > entries[j][i]
                    and entries[j][i + 1] > entries[j][i]
                ):
                    lowPoints += 1 + int(entries[j][i])
                    debugArray[j][i] = 1
            if i == len(entries[j]) - 1:
                if (
                    entries[j - 1][i] > entries[j][i]
                    and entries[j][i - 1] > entries[j][i]
                ):
                    lowPoints += 1 + int(entries[j][i])
                    debugArray[j][i] = 1
            else:
                if (
                    entries[j][i - 1] > entries[j][i]
                    and entries[j - 1][i] > entries[j][i]
                    and entries[j][i + 1] > entries[j][i]
                ):
                    lowPoints += 1 + int(entries[j][i])
                    debugArray[j][i] = 1
        elif i == 0:
            if (
                entries[j - 1][i] > entries[j][i]
                and entries[j][i + 1] > entries[j][i]
                and entries[j + 1][i] > entries[j][i]
            ):
                lowPoints += 1 + int(entries[j][i])
                debugArray[j][i] = 1
        elif i == len(entries[j]) - 1:
            if (
                entries[j - 1][i] > entries[j][i]
                and entries[j][i - 1] > entries[j][i]
                and entries[j + 1][i] > entries[j][i]
            ):
                lowPoints += 1 + int(entries[j][i])
                debugArray[j][i] = 1
        else:
            if (
                entries[j - 1][i] > entries[j][i]
                and entries[j][i - 1] > entries[j][i]
                and entries[j][i + 1] > entries[j][i]
                and entries[j + 1][i] > entries[j][i]
            ):
                lowPoints += 1 + int(entries[j][i])
                debugArray[j][i] = 1


def read_file(filename):
    with open(filename, "r") as file:
        return [
            list(map(int, list(line.strip())))
            for line in file.read().strip().split("\n")
        ]


heightmap = read_file("q9.txt")


def check_basin(matrix, x, y, visited_nodes, r_len, c_len):
    if (
        x < 0
        or y < 0
        or x > r_len
        or y > c_len
        or matrix[x][y] == 9
        or (x, y) in visited_nodes
    ):
        return

    visited_nodes.append((x, y))

    check_basin(matrix, x, y + 1, visited_nodes, r_len, c_len)
    check_basin(matrix, x, y - 1, visited_nodes, r_len, c_len)
    check_basin(matrix, x - 1, y, visited_nodes, r_len, c_len)
    check_basin(matrix, x + 1, y, visited_nodes, r_len, c_len)


height_sum = []
for j in range(0, len(debugArray)):
    for i in range(0, len(debugArray[0])):
        if debugArray[j][i] == 1:
            height_sum.append((j, i, int(entries[j][i])))

basins = []
for heights in height_sum:
    i, j, z = heights
    visited = []
    check_basin(heightmap, i, j, visited, len(heightmap) - 1, len(heightmap[0]) - 1)
    basins.append(len(visited))

basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
