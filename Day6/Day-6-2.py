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
        groupList = []
        for passen in group:
            curSet = set()
            for question in list(passen):
                curSet.add(question)
            groupList.append(curSet)
        totalAns += len(set.intersection(*groupList))
    print(totalAns)

    

if __name__ == '__main__':
    main()