import copy

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
    instructions.append("end")
    values.append(0)
    for x in range(len(instructions)):
        curInstructions = copy.copy(instructions)
        accumulator = 0
        curIndex = 0
        if(instructions[x] == "jmp"):
            curInstructions[x] = "nop"
        elif(instructions[x] == "nop"):
            curInstructions[x] = "jmp"
        if(runCode(curInstructions, values)):
            break
    print(accumulator)


def runCode(progInstructions, progValues):
    global accumulator
    global curIndex
    visitedIntructions = set()
    while(True):
        curCommand = progInstructions[curIndex]
        curValue = values[curIndex]
        if(curCommand == "end"):
            return True
        elif(curIndex in visitedIntructions):
            return False
        else:
            visitedIntructions.add(curIndex)
        if(curCommand == "acc"):
            accumulator += curValue
        elif(curCommand == "jmp"):
            curIndex += curValue - 1
        curIndex += 1


if __name__ == '__main__':
    main()