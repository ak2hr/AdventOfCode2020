from itertools import product
import copy

rules = {}


def main():
    file = open("Day19/input2.txt", "r")
    for line in file:
        if(line == '\n'):
            break
        num = int(line[:line.find(':')])
        rule = line[line.find(':') + 1:].strip().replace('"', '').split('|')
        rules[num] = []
        for x in rule:
            rules[num].append(x.strip().split(' '))
    fortyTwo = solveRule(42)
    thirtyOne = solveRule(31)
    length = len(fortyTwo[0])

    valids = []
    for line in file:
        valids.append(line.strip())
    
    numValids = 0
    for code in valids:
        
        found42 = 0
        while(True):
            if(code.startswith(tuple(fortyTwo))):
                code = copy.copy(code[length:])
                found42 += 1
            else:
                break
        
        if(found42 >= 2):
            found31 = 0
            while(True):
                if(code.startswith(tuple(thirtyOne))):
                    code = copy.copy(code[length:])
                    found31 += 1
                else:
                    break
            if(found31 > 0 and found31 < found42 and len(code) == 0):
                numValids += 1
    print(numValids)


def solveRule(rule):
    if(rules[rule][0][0] == 'a'):
        return 'a'
    elif(rules[rule][0][0] == 'b'):
        return 'b'
    else:
        potentials = []
        for x in rules[rule]:
            stringList = []
            for y in x:
                stringList.append(solveRule(int(y)))
            for y in list(product(*stringList)):
                potentials.append(''.join(y))
        return potentials
    
    


if __name__ == '__main__':
    main()