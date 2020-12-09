
from collections import deque

preamble = 25

def main():
    file = open("Day9/input.txt", "r")
    q = deque()
    for i, line in enumerate(file):
        curNum = int(line)
        if(i < preamble):
            q.append(curNum)
        elif(i >= preamble):
            curSet = set()
            for x in range(preamble):
                for y in range(x+1, preamble):
                    curSet.add(q[x] + q[y])
            if(curNum in curSet):
                q.append(curNum)
                q.popleft()
            else:
                print(curNum)
                break



if __name__ == '__main__':
    main()