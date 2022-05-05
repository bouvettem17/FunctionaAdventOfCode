
with open('q6.txt', 'r') as f:
  entry = f.readline()
  fishes = [int(fish) for fish in entry.split(',')]

fishAges = {0: 0, 1: 0, 2: 0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for fish in fishes:
  fishAges[fish] += 1

print(f'Original: {fishAges}')

def updateFishAges(numberOfDays):
  for i in range(0, numberOfDays):
    fishAgesTemp = fishAges.copy()
    for age in range(0, len(fishAges)-1):
      if age == 0:
        fishAges[age] = fishAgesTemp[age + 1]
        fishAges[6] = fishAgesTemp[0]
        fishAges[8] = fishAgesTemp[0]
      elif age == 6:
        fishAges[6] = fishAges[6] + fishAgesTemp[age + 1]
      else:
        fishAges[age] = fishAgesTemp[age + 1]
        
    print(f'day {i + 1}: {fishAges}')
  
  return fishAges


result = updateFishAges(256)

print(sum(result.values()))