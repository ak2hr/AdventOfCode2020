
numbers = []
last = {}

def main():
    file = open("Day15/input.txt", "r")
    for x in file.readline().strip().split(','):
        numbers.append(int(x))
    for x in range(len(numbers) - 1):
        last[numbers[x]] = x
    for x in range(len(numbers) - 1,2020):
        if(numbers[x] not in last):
            numbers.append(0)
        else:
            numbers.append(x - last[numbers[x]])
        last[numbers[x]] = x
    print(numbers[1990:2019])


if __name__ == '__main__':
    main()