file = open('q1.txt', 'r')
content = file.read()
numbers = list(map(int, content.splitlines()))

numbersLess = numbers[1::]
count = 0

def greaterThan(a, b):
  if(a > b) :
    return 1
  else: 
    return 0

result = sum(list(map(greaterThan, numbersLess, numbers)))
print(result)


# Part 2
slidingSums = []

for i in range(2, len(numbers)):
  slidingSums.append(numbers[i] + numbers[i-1] + numbers[i-2])

slidingSumsLess = slidingSums[1::]
result = sum(list(map(greaterThan, slidingSumsLess, slidingSums)))
print(result)
