def main():
    file = open("Day25/input.txt", "r")
    cardPublic = int(file.readline().strip())
    doorPublic = int(file.readline().strip())
    
    x = 0
    curVal = 1
    while(curVal != cardPublic):
        curVal *= 7
        curVal = curVal % 20201227
        x += 1
    print(x)

    curVal = 1
    for y in range(x):
        curVal *= doorPublic
        curVal = curVal % 20201227
    print(curVal)


if __name__ == '__main__':
    main()