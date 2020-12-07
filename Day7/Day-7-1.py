import re

def main():
    file = open("Day7/input.txt", "r")
    global bags 
    bags = dict()
    for line in file:
        line1 = line.strip().split(' contain ')
        line2 = line1[1].replace('.', '').split(', ')
        line1Fixed = line1[0][:-1]
        if(line1Fixed not in bags):
            bags[line1Fixed] = []
        for x in line2:
            if(x[-1] == 's'):
                x = x[:-1]
            if(x[:2] != "no"):
                x = x[2:]
            bags[line1Fixed].append(x)
    # for bag in bags:
    #     print(bag, ", ", bags[bag])
    goldBag = "shiny gold bag"
    global bagSet 
    bagSet = set()
    checkBags(goldBag)
    print(len(bagSet))

def checkBags(insideBag):
    for outer in bags:
        for y in bags[outer]:
            if(y == insideBag and outer not in bagSet):
                bagSet.add(outer)
                checkBags(outer)

if __name__ == '__main__':
    main()