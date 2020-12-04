def main():
    global passports
    passports = []
    validPassVals = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    ]
    file = open("Day4/input04.txt", "r")
    curPassport = {}
    for line in file:
        if(len(line) > 1):
            for x in line.strip().split():
                curPassport[x.split(':')[0]] = x.split(':')[1]
        else:
            passports.append(curPassport)
            curPassport = {}
    passports.append(curPassport)
    numInValid = 0
    for x in passports:
        for y in validPassVals:
            if(y not in x.keys()):
                numInValid += 1
                break
    print(len(passports) - numInValid)
            

if __name__ == '__main__':
    main()