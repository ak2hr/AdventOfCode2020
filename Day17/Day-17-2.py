import copy, itertools

active = set()
nextActive = set()

def main():
    global active
    global nextActive
    file = open("Day17/input.txt", "r")
    y = 0
    for line in file:
        for unit in range(len(line)):
            if(line[unit] == '#'):
                active.add((unit, y, 0, 0))
        y += 1
    
    for x in range(6):
        nextActive = set()
        allCubes = set()
        for cube in active:
            for neighbor in getNeighbors(cube):
                allCubes.add(neighbor)
            allCubes.add(cube)
        for cube in allCubes:
            activeNeighbors = 0
            for neighbor in getNeighbors(cube):
                if(neighbor in active):
                    activeNeighbors += 1
            if(cube in active and (activeNeighbors == 2 or activeNeighbors == 3)):
                nextActive.add(cube)
            elif(cube not in active and activeNeighbors == 3):
                nextActive.add(cube)
        active = copy.copy(nextActive)
    
    print(len(active))

        
def getNeighbors(cube):
    neighbors = []
    a = cube[0] - 1
    for x in range(a, a+3):
        b = cube[1] - 1
        for y in range(b, b+3):
            c = cube[2] - 1
            for z in range(c, c+3):
                d = cube[3] - 1
                for w in range(d, d+3):
                    neighbors.append((x, y, z, w))
    neighbors.remove(cube)
    return neighbors


if __name__ == '__main__':
    main()