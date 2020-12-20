import numpy as np
import math

tiles = {}
placedTiles = {}
sideLen = 0

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

    sideLen = int(math.sqrt(len(tiles)))

    placedTiles[tileNumber] = (0,0)
    placeTile(tileNumber)

    minX = 100
    minY = 100
    maxX = -100
    maxY = -100

    for tile in placedTiles:
        minX = placedTiles[tile][0] if placedTiles[tile][0] < minX else minX
        minY = placedTiles[tile][1] if placedTiles[tile][1] < minY else minY
        maxX = placedTiles[tile][0] if placedTiles[tile][0] > maxX else maxX
        maxY = placedTiles[tile][1] if placedTiles[tile][1] > maxY else maxY

    orderedTiles = []
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            for tile in placedTiles:
                if(placedTiles[tile] == (x, y)):
                    orderedTiles.append(tile)

    for x in orderedTiles:
        stripTile(x)

    organized = np.array_split(orderedTiles, sideLen)

    assembled = []
    for section in organized:
        for row in range(8):
            curRow = []
            for tile in list(section):
                for col in range(8):
                    curRow.append(tiles[tile][row][col])
            assembled.append(curRow)

    numHash = 0
    for row in assembled:
        for col in row:
            if(col == '#'):
                numHash += 1

    for x in range(2):
        for y in range(4):
            numSeaMonsters = searchOcean(assembled)
            if(numSeaMonsters != 0):
                print(numHash - numSeaMonsters)
            assembled = rotateAssem(assembled)
        flipAssem(assembled)

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

def rotate(tile):
    newTile = []
    for x in range(10):
        newRow = []
        for row in reversed(tiles[tile]):
            newRow.append(row[x])
        newTile.append(newRow)
    tiles[tile] = newTile
        
def flip(tile):
    for row in tiles[tile]:
        row.reverse()

def stripTile(tile):
    newTile = []
    for x in range(1, 9):
        newRow = []
        for y in range(1, 9):
            newRow.append(tiles[tile][x][y])
        newTile.append(newRow)
    tiles[tile] = newTile

def placeTile(placed):
    curX = placedTiles[placed][0]
    curY = placedTiles[placed][1]
    newPlaced = []
    for tile in tiles:
        if(tile not in placedTiles):
            if(matchTop(placed, tile)):
                placedTiles[tile] = (curX, curY - 1)
                newPlaced.append(tile)
            elif(matchBot(placed, tile)):
                placedTiles[tile] = (curX, curY + 1)
                newPlaced.append(tile)
            elif(matchLeft(placed, tile)):
                placedTiles[tile] = (curX - 1, curY)
                newPlaced.append(tile)
            elif(matchRight(placed, tile)):
                placedTiles[tile] = (curX + 1, curY)
                newPlaced.append(tile)
    for tile in newPlaced:
        placeTile(tile)

def matchTop(placed, notPlaced):
    for x in range(2):
        for y in range(4):
            if(getTop(placed) == getBottom(notPlaced)):
                return True
            rotate(notPlaced)
        flip(notPlaced)
    return False

def matchBot(placed, notPlaced):
    for x in range(2):
        for y in range(4):
            if(getBottom(placed) == getTop(notPlaced)):
                return True
            rotate(notPlaced)
        flip(notPlaced)
    return False

def matchLeft(placed, notPlaced):
    for x in range(2):
        for y in range(4):
            if(getLeft(placed) == getRight(notPlaced)):
                return True
            rotate(notPlaced)
        flip(notPlaced)
    return False

def matchRight(placed, notPlaced):
    for x in range(2):
        for y in range(4):
            if(getRight(placed) == getLeft(notPlaced)):
                return True
            rotate(notPlaced)
        flip(notPlaced)
    return False

def flipAssem(assembled):
    for row in assembled:
        row.reverse()

def rotateAssem(assembled):
    newAssem = []
    for x in range(len(assembled[0])):
        newRow = []
        for row in reversed(assembled):
            newRow.append(row[x])
        newAssem.append(newRow)
    return newAssem

def searchOcean(assembled):
    seaMonsters = set()
    for y in range(len(assembled)):
        for x in range(len(assembled[0])):
            seaMonster = False
            try:
                seaMonster = (assembled[y-1][x+18] == '#' and
                            assembled[y][x+5] == '#' and
                            assembled[y][x+6] == '#' and
                            assembled[y][x+11] == '#' and
                            assembled[y][x+12] == '#' and
                            assembled[y][x+17] == '#' and
                            assembled[y][x+18] == '#' and
                            assembled[y][x+19] == '#' and
                            assembled[y+1][x+1] == '#' and
                            assembled[y+1][x+4] == '#' and
                            assembled[y+1][x+7] == '#' and
                            assembled[y+1][x+10] == '#' and
                            assembled[y+1][x+13] == '#' and
                            assembled[y+1][x+16] == '#')
                if(seaMonster):
                    seaMonsters.add((y,x))
                    seaMonsters.add((y-1,x+18))
                    seaMonsters.add((y,x+5))
                    seaMonsters.add((y,x+6))
                    seaMonsters.add((y,x+11))
                    seaMonsters.add((y,x+12))
                    seaMonsters.add((y,x+17))
                    seaMonsters.add((y,x+18))
                    seaMonsters.add((y,x+19))
                    seaMonsters.add((y,x+18))
                    seaMonsters.add((y+1,x+1))
                    seaMonsters.add((y+1,x+4))
                    seaMonsters.add((y+1,x+7))
                    seaMonsters.add((y+1,x+10))
                    seaMonsters.add((y+1,x+13))
                    seaMonsters.add((y+1,x+16))
            except:
                continue
    return len(seaMonsters)

if __name__ == '__main__':
    main()