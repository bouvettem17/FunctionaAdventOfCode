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
