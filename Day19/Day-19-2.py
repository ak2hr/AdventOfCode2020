from itertools import product

rules = {}

def main():
    file = open("Day19/input.txt", "r")
    for line in file:
        if(line == '\n'):
            break
        num = int(line[:line.find(':')])
        rule = line[line.find(':') + 1:].strip().replace('"', '').split('|')
        rules[num] = []
        for x in rule:
            rules[num].append(x.strip().split(' '))
    valids = solveRule(0)
    validCount = 0
    for line in file:
        if(line.strip() in valids):
            validCount += 1
    print(validCount)


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