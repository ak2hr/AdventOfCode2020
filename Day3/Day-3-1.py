def main():
    global height
    global width
    global forest
    file = open("Day3/input.txt", "r")
    forest = []
    for line in file:
        forest.append(list(line.strip()))
    width = len(forest[0])
    height = len(forest)
    print(checkSlope(1,1)*checkSlope(3,1)*checkSlope(5,1)*checkSlope(7,1)*checkSlope(1,2))

def checkSlope(right, down):
    curX = 0
    curY = 0
    numTrees = 0
    while(curY < height - 1):
        curX = (curX + right) % width
        curY = curY + down
        #print(curX, curY, forest[curY][curX])
        if(forest[curY][curX] == '#'):
            numTrees += 1
    return numTrees


if __name__ == '__main__':
    main()