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
            bags[line1Fixed].append(x.split(' ',1))
    # for bag in bags:
    #     print(bag, ", ", bags[bag])
    goldBag = "shiny gold bag"
    print(checkBags(goldBag, 1) - 1)
    

def checkBags(outsideBag, numBags):
    curCount = 0
    for outer in bags:
        if(outer == outsideBag):
            for x in bags[outer]:
                if(x[0] == "no"):
                    return int(numBags)
                else:
                    curCount += checkBags(x[1], x[0])
    return int(numBags) + (int(numBags)*curCount)
    

if __name__ == '__main__':
    main()