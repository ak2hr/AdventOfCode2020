import copy

buses = []

def main():
    file = open("Day13/input2.txt", "r")
    for x in file.readline().strip().split(','):
        buses.append(x)
    onlyNumbers = []
    for x in range(len(buses)):
        if(buses[x] != 'x'):
            buses[x] = int(buses[x])
            onlyNumbers.append(int(buses[x]))
    indexes = []
    for x in onlyNumbers:
        indexes.append(buses.index(x) - buses.index(max(onlyNumbers)))
        origNumbers = copy.copy(onlyNumbers)
    onlyNumbers.sort()
    first = onlyNumbers[-1]
    second = onlyNumbers[-2]
    third = onlyNumbers[-3]
    fourth = onlyNumbers[-4]
    diffSecond = buses.index(second) - buses.index(first)
    diffThird = buses.index(third) - buses.index(first)
    diffFourth = buses.index(fourth) - buses.index(first)
    
    #find first instance of top three being in correct position
    current = copy.copy(first)
    while(True):
        if((current + diffSecond) % second  == 0 and (current  + diffThird) % third  == 0 and (current  + diffFourth) % fourth  == 0):
            break
        current += first
    start = current
    step = first * second * third * fourth

    #Use step to look for full pattern
    current = start
    found = False
    while(True):
        found = True
        for x in range(len(origNumbers)):
            if((current + indexes[x]) % origNumbers[x] != 0):
                found = False
        if(found):
            break
        current += step
        print(current)
    print(current - buses.index(max(onlyNumbers)))
        

if __name__ == '__main__':
    main()