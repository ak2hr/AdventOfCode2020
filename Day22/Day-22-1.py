
player1 = []
player2 = []

def main():
    file = open("Day22/input.txt", "r")
    file.readline()
    for line in file:
        if(line == '\n'):
            break
        else:
            player1.append(int(line.strip()))
    file.readline()
    for line in file:
        player2.append(int(line.strip()))
    
    while(len(player1) > 0 and len(player2) > 0):
        oneCard = player1.pop(0)
        twoCard = player2.pop(0)
        if(oneCard > twoCard):
            player1.append(oneCard)
            player1.append(twoCard)
        else:
            player2.append(twoCard)
            player2.append(oneCard)
    score = 0
    if(len(player1) > 0):
        player1.reverse()
        for x in range(len(player1)):
            score += (x + 1) * player1[x]
    else:
        player2.reverse()
        for x in range(len(player2)):
            score += (x + 1) * player2[x]
    print(score)


if __name__ == '__main__':
    main()