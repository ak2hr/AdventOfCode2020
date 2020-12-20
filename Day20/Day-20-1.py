
tiles = {}


def main():
    file = open("Day20/input.txt", "r")
    tileNumber = 0
    rows = []
    for line in file:
        if(line.startswith("Tile")):
            tileNumber = int(line.strip()[line.find(' ') + 1:line.find(':')])
        elif(line == '\n'):
            tiles[tileNumber] = rows
            rows = []
        else:
            rows.append(list(line.strip()))
    tiles[tileNumber] = rows

    corners = []
    for tile1 in tiles:
        numMatched = 0
        for tile2 in tiles:
            if(tile1 != tile2):
                if(compareTiles(tile1, tile2)):
                    numMatched += 1
        if(numMatched == 2):
            corners.append(tile1)
    
    print(corners[0] * corners[1] * corners[2] * corners[3])


def getTop(tile):
    return tiles[tile][0]

def getBottom(tile):
    return tiles[tile][9]

def getLeft(tile):
    ret = []
    for row in tiles[tile]:
        ret.append(row[0])
    return ret

def getRight(tile):
    ret = []
    for row in tiles[tile]:
        ret.append(row[9])
    return ret

def compareTiles(tile1, tile2):
    tile1Sides = [getTop(tile1), getBottom(tile1), getLeft(tile1), getRight(tile1)]
    tile1SidesRev = [getTop(tile1)[::-1], getBottom(tile1)[::-1], getLeft(tile1)[::-1], getRight(tile1)[::-1]]
    tile2Sides = [getTop(tile2), getBottom(tile2), getLeft(tile2), getRight(tile2)]
    for side in tile1Sides:
        if(side in tile2Sides):
            return True
    for side in tile1SidesRev:
        if(side in tile2Sides):
            return True

if __name__ == '__main__':
    main()