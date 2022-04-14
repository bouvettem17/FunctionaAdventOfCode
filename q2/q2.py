file = open('q2.txt', 'r')
content = file.read()
inputs = list(map(str, content.splitlines()))
xPos = 0
yPos = 0
aim = 0

for input in inputs:
  inputSplit = input.split()
  command = inputSplit[0]
  distance = int(inputSplit[1])
  
  if command == 'forward':
    xPos += distance
    yPos += distance * aim
  elif command == 'up':
    # yPos -= distance
    aim -= distance
  elif command == 'down':
    # yPos += distance
    aim += distance

print(xPos * yPos)


