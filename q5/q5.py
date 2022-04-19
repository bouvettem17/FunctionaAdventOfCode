from numpy import true_divide


with open('q5.txt', 'r') as f:
    lines = [entry.strip() for entry in f.readlines()]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        return '({0}, {1})'.format(self.x, self.y)

    def is_equal(x, y):
        if x.x == y.x and x.y == y.y:
            return True
        else:
            return False


coordinates = []

for entry in lines:
    currentCoordinates = entry.split(' -> ')
    splitCoordinates = list(
        map(lambda coordinate: coordinate.split(','), currentCoordinates))
    coordinates.append(list(map(lambda coordinate: Point(
        int(coordinate[0]), int(coordinate[1])), splitCoordinates)))

linesOfVents = []

for coordinateRow in coordinates:
    if(coordinateRow[0].x == coordinateRow[1].x):
        if(coordinateRow[0].y < coordinateRow[1].y):
            i = coordinateRow[0].y
            while coordinateRow[1].y >= i:
                linesOfVents.append(f'{coordinateRow[0].x}, {i}')
                i += 1
        else:
            i = coordinateRow[1].y
            while coordinateRow[0].y >= i:
                linesOfVents.append(f'{coordinateRow[0].x}, {i}')
                i += 1
    elif (coordinateRow[0].y == coordinateRow[1].y):
        if(coordinateRow[0].x < coordinateRow[1].x):
            i = coordinateRow[0].x
            while coordinateRow[1].x >= i:
                linesOfVents.append(f'{i}, {coordinateRow[0].y}')
                i += 1
        else:
            i = coordinateRow[1].x
            while coordinateRow[0].x >= i:
                linesOfVents.append(f'{i}, {coordinateRow[0].y}')
                i += 1
    else:
        if (coordinateRow[0].x < coordinateRow[1].x):
            i = coordinateRow[0].x
            if(coordinateRow[0].y < coordinateRow[1].y):
              j = coordinateRow[0].y
              while i != coordinateRow[1].x + 1 and j != coordinateRow[1].y + 1:
                linesOfVents.append(f'{i}, {j}')
                i += 1
                j += 1
            elif(coordinateRow[0].y > coordinateRow[1].y):
              j = coordinateRow[0].y
              while i != coordinateRow[1].x + 1 and j != coordinateRow[1].y - 1:
                linesOfVents.append(f'{i}, {j}')
                i += 1
                j -= 1
        elif (coordinateRow[0].x > coordinateRow[1].x):
          i = coordinateRow[0].x
          if(coordinateRow[0].y < coordinateRow[1].y):
            j = coordinateRow[0].y
            while i != coordinateRow[1].x - 1 and j != coordinateRow[1].y + 1:
              linesOfVents.append(f'{i}, {j}')
              i -= 1
              j += 1
          if(coordinateRow[0].y > coordinateRow[1].y):
            j = coordinateRow[0].y
            while i != coordinateRow[1].x - 1 and j != coordinateRow[1].y -1:
              linesOfVents.append(f'{i}, {j}')
              i -= 1
              j -= 1


locations = dict()
for loc in linesOfVents:
    if loc in locations.keys():
        locations[loc] += 1
    else:
        locations[loc] = 1

count = 0
for loc in locations:
    if locations[loc] > 1:
        count += 1

print(count)
