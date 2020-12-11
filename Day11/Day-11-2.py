import copy

seats = []
otherSeats = []

def main():
    global seats
    global otherSeats
    file = open("Day11/input.txt", "r")
    for line in file:
        seats.append(list(line.strip()))
    otherSeats = copy.deepcopy(seats)
    count = 0
    while(True):
        seats = copy.deepcopy(otherSeats)
        oneTick()
        if(seats == otherSeats):
            break
    count = 0
    for x in seats:
        for y in x:
            if y == '#':
                count += 1
    print(count)
    

#           0        1      2        3     4      5       6      7
# Order = [topLeft, top, topRight, left, right, botLeft, bot, botRight]

def oneTick():
    global seats
    global otherSeats
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            around = []
            for num in range(8):
                around.append(False)
            val = seats[y][x]
            if(val != '.'):
                if(x != 0 and y !=0):
                    around[0] = True if seats[y-1][x-1] == '#' else False
                if(y != 0):
                    around[1] = True if seats[y-1][x] == '#' else False
                if(x != len(seats[0]) - 1 and y != 0):
                    around[2] = True if seats[y-1][x+1] == '#' else False
                if(x != 0):
                    around[3] = True if seats[y][x-1] == '#' else False
                if(x != len(seats[0]) - 1):
                    around[4] = True if seats[y][x+1] == '#' else False
                if(x != 0 and y != len(seats) - 1):
                    around[5] = True if seats[y+1][x-1] == '#' else False
                if(y != len(seats) - 1):
                    around[6] = True if seats[y+1][x] == '#' else False
                if(x != len(seats[0]) - 1 and y != len(seats) - 1):
                    around[7] = True if seats[y+1][x+1] == '#' else False
            if(val == 'L' and around.count(True) == 0):
                otherSeats[y][x] = '#'
            elif(val == '#' and around.count(True) >= 4):
                otherSeats[y][x] = 'L'
            else:
                otherSeats[y][x] = val


if __name__ == '__main__':
    main()