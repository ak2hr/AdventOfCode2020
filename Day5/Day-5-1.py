def main():
    file = open("Day5/input.txt", "r")
    curMax = 0
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
        if(seatId > curMax):
            curMax = seatId
    print(curMax)




if __name__ == '__main__':
    main()