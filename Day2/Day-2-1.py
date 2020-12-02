file = open("Day2/input.txt", "r")
mins = []
maxes = []
letters = []
passwords = []
for line in file:
    parts = line.split()
    ranges = parts[0].split('-')
    mins.append(int(ranges[0]))
    maxes.append(int(ranges[1]))
    letters.append(parts[1][:1])
    passwords.append(parts[2])
valids = 0
for x in range(0, len(mins)):
    if(passwords[x].count(letters[x]) >= mins[x] and passwords[x].count(letters[x]) <= maxes[x]):
        valids += 1
print(valids)