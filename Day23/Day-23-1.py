
cups = []
curCup = 0

def main():
    global cups
    global curCup
    file = open("Day23/input.txt", "r")
    for line in file:
        cups = [int(x) for x in list(line)]
    curCup = cups[0]

    for x in range(100):
        oneMove()   

    oneInd = cups.index(1)
    result = ""
    for x in range(1,9):
        result += str(cups[(oneInd + x) % 9])
    print(result)
    

def oneMove():
    global cups
    global curCup
    pickedUp = []
    for x in range(1,4):
        ind = cups.index(curCup) + x
        pickedUp.append(cups[ind % 9])
    for x in pickedUp:
        cups.remove(x)
    destCup = (curCup - 1) % 9
    while(destCup not in cups):
        destCup = (destCup - 1) % 10
    destInd = cups.index(destCup)
    for x in range(3):
        cups.insert(destInd + 1 + x, pickedUp[x])
    curCup = cups[(cups.index(curCup) + 1) % 9]

    
if __name__ == '__main__':
    main()