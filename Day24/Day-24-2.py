import copy

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
    
    for x in range(100):
        white = []
        for tile in black:
            #e
            if(getE(tile) not in white and getE(tile) not in black):
                white.append(getE(tile))
            #w
            if(getW(tile) not in white and getW(tile) not in black):
                white.append(getW(tile))
            #ne
            if(getNE(tile) not in white and getNE(tile) not in black):
                white.append(getNE(tile))
            #nw
            if(getNW(tile) not in white and getNW(tile) not in black):
                white.append(getNW(tile))
            #se
            if(getSE(tile) not in white and getSE(tile) not in black):
                white.append(getSE(tile))
            #sw
            if(getSW(tile) not in white and getSW(tile) not in black):
                white.append(getSW(tile))

        newBlack = []
        for tile in black:
            countBlack = 0
            if(getE(tile) in black):
                countBlack += 1
            if(getW(tile) in black):
                countBlack += 1
            if(getNE(tile) in black):
                countBlack += 1
            if(getNW(tile) in black):
                countBlack += 1
            if(getSE(tile) in black):
                countBlack += 1
            if(getSW(tile) in black):
                countBlack += 1
            if(countBlack == 1 or countBlack == 2):
                newBlack.append(tile)

        for tile in white:
            countBlack = 0
            if(getE(tile) in black):
                countBlack += 1
            if(getW(tile) in black):
                countBlack += 1
            if(getNE(tile) in black):
                countBlack += 1
            if(getNW(tile) in black):
                countBlack += 1
            if(getSE(tile) in black):
                countBlack += 1
            if(getSW(tile) in black):
                countBlack += 1
            if(countBlack == 2):
                newBlack.append(tile)

        black = copy.copy(newBlack)
    print(len(black))
            
def getE(tile):
    return [tile[0]+2, tile[1]]

def getW(tile):
    return [tile[0]-2, tile[1]]

def getNE(tile):
    return [tile[0]+1, tile[1]-1]

def getNW(tile):
    return [tile[0]-1, tile[1]-1]

def getSE(tile):
    return [tile[0]+1, tile[1]+1]

def getSW(tile):
    return [tile[0]-1, tile[1]+1]

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