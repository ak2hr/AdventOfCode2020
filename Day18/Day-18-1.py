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
    for x in range(0, len(equation)):
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
    ans = int(reducedEquation[0])
    currentOp = ""
    for x in range(1, len(reducedEquation)):
        if(reducedEquation[x] == '+'):
            currentOp = "plus"
        elif(reducedEquation[x] == '*'):
            currentOp = "times"
        else:
            if(currentOp == "plus"):
                ans += int(reducedEquation[x])
            elif(currentOp == "times"):
                ans *= int(reducedEquation[x])
    return ans


if __name__ == '__main__':
    main()