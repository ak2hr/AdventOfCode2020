
tileDirs = []

def main():
    global tileDirs
    file = open("Day24/input.txt", "r")
    for line in file:
        line = list(line.strip())
        curDir = []
        prev = ''
        for x in line:
            if(x == 'e' or x == 'w'):
                if(prev == 'n' or prev == 's'):
                    curDir.append(prev + x)
                else:
                    curDir.append(x)
                prev = ''
            else:
                prev = x
        tileDirs.append(curDir)
    
    black = []
    for dirs in tileDirs:
        tile = followDirs(dirs)
        if(tile in black):
            black.remove(tile)
        else:
            black.append(tile)
    print(len(black))


def followDirs(dirs):
    cur = [0,0]
    for x in dirs:
        if(x == "e"):
            cur[0] += 2
        elif(x == "w"):
            cur[0] -= 2
        elif(x == "nw"):
            cur[0] -= 1
            cur[1] -= 1
        elif(x == "ne"):
            cur[0] += 1
            cur[1] -= 1
        elif(x == "sw"):
            cur[0] -= 1
            cur[1] += 1
        elif(x == "se"):
            cur[0] += 1
            cur[1] += 1
    return cur

if __name__ == '__main__':
    main()