

combos = {}
adaptors = []

def main():
    global combos
    global adaptors
    file = open("Day10/input.txt", "r")
    for line in file:
        adaptors.append(int(line))
    adaptors.sort()
    print(findCombos(max(adaptors)))


def findCombos(num):
    global combos
    if(num in combos):
        return combos[num]
    else:
        runTotal = 0
        if(num - 1 in adaptors):
            runTotal += findCombos(num - 1)
        if(num - 2 in adaptors):
            runTotal += findCombos(num - 2)
        if(num - 3 in adaptors):
            runTotal += findCombos(num - 3)
        if(num in [1,2,3]):
            runTotal += 1
        combos[num] = runTotal
        return runTotal

if __name__ == '__main__':
    main()