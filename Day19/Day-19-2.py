from itertools import product
import copy

rules = {}


def main():
    file = open("Day19/test2.txt", "r")
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
    print(thirtyOne)

    valids = []
    for line in file:
        valids.append(line.strip())

    #check if starts with a multiple of rule 42
    
    #check if continues with multiple of rule 31

    


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