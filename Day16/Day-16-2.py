import copy

validNumbers = set()
tickets = []
validTickets = []
myTicket = []
rules = {}
unsolvedRules = []

def main():
    global validNumbers
    global tickets
    global myTicket
    global validTickets
    global rules
    global unsolvedRules
    file = open("Day16/input.txt", "r")

    #Get all the rules
    while(True):
        line = file.readline().strip()
        if(line == ''):
            break
        ranges = line[line.find(':') + 2:].replace(' ', '').split("or")
        rule = line.split(':')[0]
        unsolvedRules.append(rule)
        rules[rule] = []
        for curRange in ranges:
            indiv = curRange.split('-')
            for x in range(int(indiv[0]), int(indiv[1]) + 1):
                validNumbers.add(x)
                rules[rule].append(x)

    #Get my ticket
    line = file.readline()
    while(True):
        line = file.readline().strip()
        if(line == ''):
            break
        myTicket = line.split(',')

    #Get all other tickets
    file.readline()
    while(True):
        line = file.readline().strip()
        if(line == ''):
            break
        tickets.append(line.split(','))
    
    #remove invalid tickets
    for ticket in tickets:
        valid = True
        for x in ticket:
            if(int(x) not in validNumbers):
                print(x)
                valid = False
        if(valid):
            validTickets.append(ticket)
    
    #identify fields
    unsolvedFields = list(range(len(validTickets[0])))
    print(unsolvedFields)
    potentialRules = {}
    for x in unsolvedFields:
        potentialRules[x] = copy.copy(unsolvedRules)


    while(len(unsolvedFields) > 0):
        fieldsToRemove = []
        rulesToRemove = []
        for x in unsolvedFields:
            curRules = potentialRules[x]
            potentialRulesToRemove = set()
            for ticket in validTickets:
                for rule in curRules:
                    if(int(ticket[x]) not in rules[rule]):
                        potentialRulesToRemove.add(rule)
            for rule in potentialRulesToRemove:
                potentialRules[x].remove(rule)
            if(len(potentialRules[x]) == 1):
                print(x, potentialRules[x][0])
                fieldsToRemove.append(x)
                rulesToRemove.append(potentialRules[x][0])
        for field in fieldsToRemove:
            unsolvedFields.remove(field)
        for rule in rulesToRemove:
            for entry in potentialRules:
                if(rule in potentialRules[entry]):
                    potentialRules[entry].remove(rule)

    print(int(myTicket[0]) * int(myTicket[7]) * int(myTicket[4]) * int(myTicket[17]) * int(myTicket[10]) * int(myTicket[16]))
        
                

            
    



if __name__ == '__main__':
    main()