
validNumbers = set()

def main():
    global validNumbers
    file = open("Day16/input.txt", "r")

    #Get all the rules
    while(True):
        line = file.readline().strip()
        if(line == ''):
            break
        ranges = line[line.find(':') + 2:].replace(' ', '').split("or")
        for curRange in ranges:
            indiv = curRange.split('-')
            for x in range(int(indiv[0]), int(indiv[1]) + 1):
                validNumbers.add(x)

    #Get my ticket
    while(True):
        line = file.readline().strip()
        if(line == ''):
            break

    errorRate = 0
    #Get all other tickets
    file.readline()
    while(True):
        line = file.readline().strip()
        if(line == ''):
            break
        ticketNums = line.split(',')
        for x in ticketNums:
            if(int(x) not in validNumbers):
                errorRate += int(x)
    print(errorRate)


if __name__ == '__main__':
    main()