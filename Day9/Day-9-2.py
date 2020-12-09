
from collections import deque

invalid = 36845998

def main():
    file = open("Day9/input.txt", "r")
    numbers = []
    for line in file:
        numbers.append(int(line))
    print(len(numbers))
    for x in range(len(numbers)):
        curSum = numbers[x]
        for y in range(x+1, len(numbers)):
            curSum += numbers[y]
            if(curSum == invalid): 
                print(min(numbers[x:y+1]) + max(numbers[x:y+1]))
            elif(curSum > invalid):
                break



if __name__ == '__main__':
    main()