file = open('q1.txt', 'r')
content = file.read()
numbers = list(map(int, content.splitlines()))

numbersLess = numbers[1::]
count = 0

def greaterThan(a, b):
  return 1 if a > b else 0

result = sum(list(map(greaterThan, numbersLess, numbers)))
print(result)
