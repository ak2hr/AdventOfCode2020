def main():
    file = open("Day6/input.txt", "r")
    passengers = []
    passenger = []
    for line in file:
        if(line != '\n'):
            passenger.append(line.strip())
        else:
            passengers.append(passenger)
            passenger = []
    passengers.append(passenger)
    totalAns = 0
    for group in passengers:
        curSet = set()
        for passen in group:
            for question in list(passen):
                curSet.add(question)
        totalAns += len(curSet)
    print(totalAns)

    

if __name__ == '__main__':
    main()