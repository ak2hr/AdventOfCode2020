
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
        for tile2 in tiles:
            if(tile1 != tile2):
                if(compareTiles(tile1, tile2)):
                    
    
    


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
    

if __name__ == '__main__':
    main()