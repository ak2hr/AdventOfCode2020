from itertools import product

rules = {}
valid = set()

def main():
    file = open("Day19/test1.txt", "r")
    for line in file:
        if(line == '\n'):
            break
        num = int(line[:line.find(':')])
        rule = line[line.find(':') + 1:].strip().replace('"', '').split('|')
        rules[num] = []
        for x in rule:
            rules[num].append(x.strip().split(' '))
    print(rules)
    print(solveRule(0))


def solveRule(rule):
    print('here')
    
    


if __name__ == '__main__':
    main()