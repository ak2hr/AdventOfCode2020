
curCup = 0
size = 0

def main():
    global curCup
    global size
    file = open("Day23/input.txt", "r")
    cups = []
    for line in file:
        cups = [int(x) for x in list(line)]
    for x in range(10,101):
        cups.append(x)
    curCup = cups[0]
    size = len(cups)

    for x in range(10000000):
        print(x)
        cups = oneMove(cups)  

    oneInd = cups.index(1)
    result = ""
    for x in range(1,9):
        result += str(cups[(oneInd + x) % 9])
    print(result) 

    # oneInd = cups.index(1)
    # print(cups[oneInd + 1] * cups[oneInd + 2])
    

def oneMove(cups):
    global curCup
    global size
    pickedUp = []
    for x in range(1,4):
        ind = cups.index(curCup) + x
        pickedUp.append(cups[ind % size])
    for x in pickedUp:
        cups.remove(x)
    destCup = (curCup - 1) % size
    while(destCup in pickedUp or destCup == 0):
        destCup = (destCup - 1) % (size + 1)
    destInd = cups.index(destCup)
    cups = cups[:destInd + 1] + pickedUp + cups[destInd + 1:]
    curCup = cups[(cups.index(curCup) + 1) % size]
    return cups

    
if __name__ == '__main__':
    main()