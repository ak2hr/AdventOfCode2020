
curCup = 0
cups = {}
size = 0

def main():
    global curCup
    global cups
    global size
    file = open("Day23/input.txt", "r") 
    starting = [int(x) for x in list(file.readline().strip())]
    for x in range(len(starting)):
        if(x == len(starting) - 1):
            cups[starting[x]] = 10
        else:
            cups[starting[x]] = starting[x+1]
    for x in range(10, 1000000):
        cups[x] = x + 1
    cups[1000000] = starting[0]
    curCup = starting[0]
    size = len(cups)

    for x in range(10000000):
        oneMove() 
    first = cups[1]
    second = cups[first]
    print(first * second)
    

    # oneInd = cups.index(1)
    # result = ""
    # for x in range(1,9):
    #     result += str(cups[(oneInd + x) % 9])
    # print(result) 

    # oneInd = cups.index(1)
    # print(cups[oneInd + 1] * cups[oneInd + 2])
    

def oneMove():
    global curCup
    global cups
    global size
    pickedUp = pickUpThree(curCup)
    dest = (curCup - 1) % size
    while(dest == 0 or dest in pickedUp):
        dest = (dest-1) % (size + 1)
    placeThree(dest, pickedUp)
    curCup = cups[curCup]
    
    
def pickUpThree(start):
    global cups
    ret = []
    ret.append(cups[start])
    ret.append(cups[ret[0]])
    ret.append(cups[ret[1]])
    cups[start] = cups[ret[2]]
    return ret

def placeThree(start, pickedUp):
    global cups
    cups[pickedUp[0]] = pickedUp[1]
    cups[pickedUp[1]] = pickedUp[2]
    cups[pickedUp[2]] = cups[start]
    cups[start] = pickedUp[0]

def printCups():
    global cups
    current = cups[curCup]
    while(current != curCup):
        print(cups[current], end=' ')
        current = cups[current]
    print(cups[curCup], end=' ')
    print()

    
if __name__ == '__main__':
    main()