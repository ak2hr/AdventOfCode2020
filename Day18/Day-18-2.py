import copy

def main():
    file = open("Day18/input.txt", "r")
    sum = 0
    for line in file:
        sum += solveEquation(list(line.replace(' ', '').strip()))
    print(sum)
    

def solveEquation(equation):
    openParens = 0
    reducedEquation = []
    first = -1
    for x in range(len(equation)):
        if(equation[x] == '('):
            openParens += 1
            if(first == -1):
                first = x
        elif(equation[x] == ')'):
            openParens -= 1
            if(openParens == 0):
                reducedEquation.append(solveEquation(equation[first + 1:x]))
                first = -1
        elif(openParens == 0):
            reducedEquation.append(equation[x])

    while(reducedEquation.count('+') > 0):
        nextEquation = []
        currentX = 0
        for x in range(len(reducedEquation) - 1):
            if(reducedEquation[x + 1] == '+'):
                nextEquation.append(int(reducedEquation[x]) + int(reducedEquation[x+2]))
                currentX = x + 3
                break
            elif(reducedEquation[x + 1] == '*' or reducedEquation[x-1] == '*' or reducedEquation[x] == '*'):
                nextEquation.append(reducedEquation[x])
        for x in range(currentX, len(reducedEquation)):
            nextEquation.append(reducedEquation[x])
        reducedEquation = copy.copy(nextEquation)
        
    ans = int(reducedEquation[0])
    for x in range(1,len(reducedEquation)):
        if(reducedEquation[x] != '*'):
            ans *= int(reducedEquation[x])

    return ans


if __name__ == '__main__':
    main()