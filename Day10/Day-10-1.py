def main():
    file = open("Day10/input.txt", "r")
    adaptors = []
    for line in file:
        adaptors.append(int(line))
    adaptors.sort()
    adaptors.insert(0,0)
    adaptors.append(max(adaptors) + 3)
    num1 = 0
    num3 = 0
    for x in range(1,len(adaptors)):
        if(adaptors[x] - adaptors[x-1] == 1):
            num1 += 1
        elif(adaptors[x] - adaptors[x-1] == 3):
            num3 += 1
    print(num1, num3)
    print(num1 * num3)
    


if __name__ == '__main__':
    main()