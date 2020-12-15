
numbers = []
last = {}

def main():
    file = open("Day15/input.txt", "r")
    for x in file.readline().strip().split(','):
        numbers.append(int(x))
    for x in range(len(numbers) - 1):
        last[numbers[x]] = x
    for x in range(len(numbers) - 1,30000000):
        if(numbers[x] not in last):
            numbers.append(0)
        else:
            numbers.append(x - last[numbers[x]])
        last[numbers[x]] = x
        if(x % 100000 == 0):
            print(x)
    print(numbers[30000000 - 1])


if __name__ == '__main__':
    main()