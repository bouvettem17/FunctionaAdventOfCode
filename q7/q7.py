import math

from numpy import diff

with open('q7.txt', 'r') as f:
  startingLocations = [int(num) for num in f.readline().split(',')]

minStartingPosition = min(startingLocations)
maxStartingPosition = max(startingLocations)
storeDistances = {}
minDistance = 0


for i in range(minStartingPosition, maxStartingPosition + 1):
  differenceArray = map(lambda x: int((abs(x - i)*(abs(x-i)+1)/2)), startingLocations)
  totalDifference = sum(list(differenceArray))
  if i == 0:
    minDistance = totalDifference
  elif totalDifference < minDistance:
    minDistance = totalDifference


print(minDistance)
