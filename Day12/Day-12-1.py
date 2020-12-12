
actions = []
values = []

def main():
    file = open("Day12/input.txt", "r")
    for line in file:
        actions.append(line[0])
        values.append(int(line[1:]))
    direction = 90
    x = 0
    y = 0
    for cur in range(len(actions)):
        action = actions[cur]
        value = values[cur]
        if(action == 'N'):
            y += value
        elif(action == 'S'):
            y -= value
        elif(action == 'E'):
            x += value
        elif(action == 'W'):
            x -= value
        elif(action == 'L'):
            direction = (direction - value) % 360
        elif(action == 'R'):
            direction = (direction + value) % 360
        elif(action == 'F'):
            if(direction == 0):
                y += value
            elif(direction == 90):
                x += value
            elif(direction == 180):
                y -= value
            elif(direction == 270):
                x -= value
    print(abs(x) + abs(y))

if __name__ == '__main__':
    main()