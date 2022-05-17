from collections import deque

with open("q10.txt", "r") as f:
    navLines = [line.strip() for line in f.readlines()]

charComplements = {"]": "[", ")": "(", ">": "<", "}": "{"}
corruptScore = {")": 3, "]": 57, "}": 1197, ">": 25137}
incompleteScore = {"(": 1, "[": 2, "{": 3, "<": 4}

returnChars = []
incompleteLines = []


def checkLine(line):
    chunkQueue = deque()
    for char in line:
        if char in charComplements.values():
            chunkQueue.append(char)
        else:
            if len(chunkQueue) == 0:
                return False
            else:
                currentOpen = chunkQueue.pop()
                if charComplements[char] != currentOpen:
                    return char
    completeLineCost(chunkQueue)


def completeLineCost(chunkQueue):
    chunkQueue.reverse()
    sumForIncomplete = 0
    for char in chunkQueue:
        sumForIncomplete = sumForIncomplete * 5 + incompleteScore[char]
    incompleteLines.append(sumForIncomplete)


for line in navLines:
    result = checkLine(line)
    if result != None:
        returnChars.append(result)

result = sum(map(lambda char: corruptScore[char], returnChars))
print(f"Total Syntax Error Score: {result}")

incompleteLines.sort()
result = incompleteLines[len(incompleteLines) // 2]
print(f"Middle Incomplete Score: {result}")
