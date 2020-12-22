import copy

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
    
    winner = gameOfCombat(player1, player2)
    player1Final = winner[1]
    player2Final = winner[2]
    score = 0
    if(len(player1Final) > 0):
        player1Final.reverse()
        for x in range(len(player1Final)):
            score += (x + 1) * player1Final[x]
    else:
        player2Final.reverse()
        for x in range(len(player2Final)):
            score += (x + 1) * player2Final[x]
    print(score)


#return = (True, player1Deck, player2Deck) if player1 won, False if otherwise
def gameOfCombat(player1Deck, player2Deck):
    playedRounds = []
    while(len(player1Deck) > 0 and len(player2Deck) > 0):
        thisRound = [copy.copy(player1Deck), copy.copy(player2Deck)]
        if(thisRound in playedRounds):
            return (True, player1Deck, player2Deck)
        else:
            playedRounds.append(thisRound)
            oneCard = player1Deck.pop(0)
            twoCard = player2Deck.pop(0)
            winner = oneCard > twoCard
            if(len(player1Deck) >= oneCard and len(player2Deck) >= twoCard):
                winner = gameOfCombat(player1Deck[:oneCard], player2Deck[:twoCard])[0]
            if(winner):
                player1Deck.append(oneCard)
                player1Deck.append(twoCard)
            else:
                player2Deck.append(twoCard)
                player2Deck.append(oneCard)
    if(len(player1Deck) == 0):
        return (False, player1Deck, player2Deck)
    else:
        return (True, player1Deck, player2Deck)
            
        


if __name__ == '__main__':
    main()