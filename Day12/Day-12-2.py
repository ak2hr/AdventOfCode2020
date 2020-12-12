import copy

actions = []
values = []

def main():
    file = open("Day12/input.txt", "r")
    for line in file:
        actions.append(line[0])
        values.append(int(line[1:]))
    x = 0
    y = 0
    wayX = 10
    wayY = 1
    for cur in range(len(actions)):
        tempX = copy.copy(wayX)
        tempY = copy.copy(wayY)
        action = actions[cur]
        value = values[cur]
        if(action == 'N'):
            wayY += value
        elif(action == 'S'):
            wayY -= value
        elif(action == 'E'):
            wayX += value
        elif(action == 'W'):
            wayX -= value
        elif(action == 'L'):
            if(value % 360 == 90):
                wayY = tempX
                wayX = (tempY * -1)
            elif(value % 360 == 180):
                wayX = tempX * -1
                wayY = tempY * -1
            elif(value % 360 == 270):
                wayY = (tempX * -1)
                wayX = tempY
        elif(action == 'R'):
            if(value % 360 == 90):
                wayY = (tempX * -1)
                wayX = tempY
            elif(value % 360 == 180):
                wayX = tempX * -1
                wayY = tempY * -1
            elif(value % 360 == 270):
                wayY = tempX
                wayX = (tempY * -1)
        elif(action == 'F'):
            x += (value * wayX)
            y += (value * wayY)
    print(abs(x) + abs(y))

if __name__ == '__main__':
    main()