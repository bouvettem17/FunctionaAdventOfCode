file = open('q3.txt', 'r')
content = file.read()
numbers = list(map(str, content.splitlines()))

gammaRate = ""
epsilonRate = ""

def calculateIndexCounts(binaryList):
  indexCounts = {}
  for number in binaryList:
    for i in range(len(number)):
      if i in indexCounts:
        if (int(number[i]) == 1):
          indexCounts[i] += 1
        else:
          indexCounts[i] -= 1
      else:
        if (int(number[i]) == 1):
          indexCounts[i] = 1
        else:
          indexCounts[i] = -1
    
  return indexCounts

partOneIndexCounts = calculateIndexCounts(numbers)

for index, value in partOneIndexCounts.items():
  if value > 0:
    gammaRate += '1'
    epsilonRate += '0'
  else:
    gammaRate += '0'
    epsilonRate += '1'

gammaRateConverted = int(gammaRate, 2)
epsilonRateConverted = int(epsilonRate, 2)

print(epsilonRateConverted * gammaRateConverted)

remainingForCarbon = numbers

def findOxygen(remainingForOxygen, currentIndex):
  if(len(remainingForOxygen) == 1):
    return remainingForOxygen[0]
  else:
    currentIndexCount = calculateIndexCounts(remainingForOxygen)
    if(currentIndexCount[currentIndex] < 0):
      for number in list(remainingForOxygen):
        if int(number[currentIndex]) != 0:
          remainingForOxygen.remove(number)
    else:
      for number in list(remainingForOxygen):
        if int(number[currentIndex]) != 1:
          remainingForOxygen.remove(number)
    
    currentIndex += 1
    return findOxygen(remainingForOxygen, currentIndex)

def findCarbon(remainingForCarbon, currentIndex):
  if(len(remainingForCarbon) == 1):
    return remainingForCarbon[0]
  else:
    currentIndexCount = calculateIndexCounts(remainingForCarbon)
    if(currentIndexCount[currentIndex] < 0):
      for number in list(remainingForCarbon):
        if int(number[currentIndex]) != 1:
          remainingForCarbon.remove(number)
    else:
      for number in list(remainingForCarbon):
        if int(number[currentIndex]) != 0:
          remainingForCarbon.remove(number)
    
    currentIndex += 1
    return findCarbon(remainingForCarbon, currentIndex)

answer = int(findOxygen(list(numbers), 0), 2)
answer2 = int(findCarbon(list(numbers), 0), 2)
print(answer * answer2)

