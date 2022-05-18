import numpy as np

with open("q11.txt", "r") as f:
    octupus = [[int(num) for num in num.strip()] for num in f.readlines()]


def octupusFlash(j, i, trackOctupusFlash):
    if (
        j < 0
        or i < 0
        or j > len(octupus) - 1
        or i > len(octupus[0]) - 1
        or trackOctupusFlash[j][i] == 1
    ):
        return

    trackOctupusFlash[j][i] = 1

    if j != 0:
        if i != 0:
            octupus[j - 1][i - 1] += 1
            if octupus[j - 1][i - 1] == 10:
                octupusFlash(j - 1, i - 1, trackOctupusFlash)
        if i != len(octupus[0]) - 1:
            octupus[j - 1][i + 1] += 1
            if octupus[j - 1][i + 1] == 10:
                octupusFlash(j - 1, i + 1, trackOctupusFlash)
        octupus[j - 1][i] += 1
        if octupus[j - 1][i] == 10:
            octupusFlash(j - 1, i, trackOctupusFlash)
    if j != len(octupus) - 1:
        if i != 0:
            octupus[j + 1][i - 1] += 1
            if octupus[j + 1][i - 1] == 10:
                octupusFlash(j + 1, i - 1, trackOctupusFlash)
        if i != len(octupus[0]) - 1:
            octupus[j + 1][i + 1] += 1
            if octupus[j + 1][i + 1] == 10:
                octupusFlash(j + 1, i + 1, trackOctupusFlash)
        octupus[j + 1][i] += 1
        if octupus[j + 1][i] == 10:
            octupusFlash(j + 1, i, trackOctupusFlash)
    if i != 0:
        octupus[j][i - 1] += 1
        if octupus[j][i - 1] == 10:
            octupusFlash(j, i - 1, trackOctupusFlash)
    if i != len(octupus[0]) - 1:
        octupus[j][i + 1] += 1
        if octupus[j][i + 1] == 10:
            octupusFlash(j, i + 1, trackOctupusFlash)


def resetFlashPoints(trackOctupusFlash, numberOfFlashes, allFlashed):
    allFlashed = True
    for j in range(0, len(trackOctupusFlash)):
        for i in range(0, len(trackOctupusFlash[0])):
            if trackOctupusFlash[j][i] == 1:
                octupus[j][i] = 0
                numberOfFlashes += 1
            else:
                allFlashed = False

    return numberOfFlashes, allFlashed


numberOfFlashes = 0
allFlashed = False
step = 0

# Change to for k in range(0, 100) for the first part
while allFlashed == False:
    trackOctupusFlash = np.zeros((len(octupus), len(octupus[0])))
    for j in range(0, len(octupus)):
        for i in range(0, len(octupus[0])):
            octupus[j][i] += 1
            if octupus[j][i] == 10:
                octupusFlash(j, i, trackOctupusFlash)

    numberOfFlashes, allFlashed = resetFlashPoints(
        trackOctupusFlash, numberOfFlashes, allFlashed
    )

    step += 1

print(np.asarray(octupus))
print(f"The number of flashes that happen is: {numberOfFlashes}")
print(f"All Octupi Flash at step: {step}")
