
curIndex = 0
accumulator = 0
instructions = []
values = []

def main():
    file = open("Day8/input.txt", "r")
    global curIndex
    global instructions
    global values
    global accumulator
    for line in file:
        instructions.append(line.split()[0])
        values.append(int(line.split()[1]))
    visitedIntructions = set()
    while(True):
        if(curIndex in visitedIntructions):
            break
        else:
            visitedIntructions.add(curIndex)
        curCommand = instructions[curIndex]
        curValue = values[curIndex]
        if(curCommand == "acc"):
            accumulator += curValue
        elif(curCommand == "jmp"):
            curIndex += curValue - 1
        curIndex += 1
    print(accumulator)



if __name__ == '__main__':
    main()