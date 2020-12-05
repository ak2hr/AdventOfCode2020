def main():
    file = open("Day5/input.txt", "r")
    seats = []
    for line in file:
        interval = 64
        row = 0
        for x in line[:7]:
            if(x == 'B'):
                row += interval
            interval /= 2
        interval = 4
        column = 0
        for x in line[7:]:
            if(x == 'R'):
                column += interval
            interval /= 2
        seatId = (8*row) + column
        seats.append(int(seatId))
    seats.sort()
    for x in range(11,851):
        if(x not in seats):
            print(x)



if __name__ == '__main__':
    main()