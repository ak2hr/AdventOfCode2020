import copy

earliest = 0
buses = []

def main():
    file = open("Day13/input.txt", "r")
    earliest = int(file.readline())
    for x in file.readline().strip().split(','):
        if(x != 'x'):
            buses.append(int(x))
    current = copy.copy(earliest)
    found = False
    theBus = 0
    while(not found):
        for x in buses:
            if(current % x == 0):
                found = True
                theBus = x
        current += 1
    firstBus = current - 1
    print((firstBus - earliest) * theBus)


if __name__ == '__main__':
    main()