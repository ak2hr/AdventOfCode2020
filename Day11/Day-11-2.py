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

                #topLeft
                vert = y - 1
                horz = x - 1
                while(vert >= 0 and horz >= 0):
                    if(seats[vert][horz] == '#'):
                        around[0] = True
                        break
                    elif(seats[vert][horz] == 'L'):
                        break
                    vert -= 1
                    horz -= 1

                #top
                vert = y - 1
                horz = x
                while(vert >= 0):
                    if(seats[vert][horz] == '#'):
                        around[1] = True
                        break
                    elif(seats[vert][horz] == 'L'):
                        break
                    vert -= 1

                #topRight
                vert = y - 1
                horz = x + 1
                while(vert >= 0 and horz < len(seats[0])):
                    if(seats[vert][horz] == '#'):
                        around[2] = True
                        break
                    elif(seats[vert][horz] == 'L'):
                        break
                    vert -= 1
                    horz += 1

                #left
                vert = y
                horz = x - 1
                while(horz >= 0):
                    if(seats[vert][horz] == '#'):
                        around[3] = True
                        break
                    elif(seats[vert][horz] == 'L'):
                        break
                    horz -= 1

                #right
                vert = y
                horz = x + 1
                while(horz < len(seats[0])):
                    if(seats[vert][horz] == '#'):
                        around[4] = True
                        break
                    elif(seats[vert][horz] == 'L'):
                        break
                    horz += 1

                #botLeft
                vert = y + 1
                horz = x - 1
                while(vert < len(seats) and horz >= 0):
                    if(seats[vert][horz] == '#'):
                        around[5] = True
                        break
                    elif(seats[vert][horz] == 'L'):
                        break
                    vert += 1
                    horz -= 1

                #bot
                vert = y + 1
                horz = x
                while(vert < len(seats)):
                    if(seats[vert][horz] == '#'):
                        around[6] = True
                        break
                    elif(seats[vert][horz] == 'L'):
                        break
                    vert += 1

                #botRight
                vert = y + 1
                horz = x + 1
                while(vert < len(seats) and horz < len(seats[0])):
                    if(seats[vert][horz] == '#'):
                        around[7] = True
                        break
                    elif(seats[vert][horz] == 'L'):
                        break
                    vert += 1
                    horz += 1

            if(val == 'L' and around.count(True) == 0):
                otherSeats[y][x] = '#'
            elif(val == '#' and around.count(True) >= 5):
                otherSeats[y][x] = 'L'
            else:
                otherSeats[y][x] = val


if __name__ == '__main__':
    main()