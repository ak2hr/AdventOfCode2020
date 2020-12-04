import re

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
    file = open("Day4/input.txt", "r")
    curPassport = {}
    for line in file:
        if(len(line) > 1):
            for x in line.strip().split():
                curPassport[x.split(':')[0]] = x.split(':')[1]
        else:
            passports.append(curPassport)
            curPassport = {}
    passports.append(curPassport)
    numValid = 0
    for x in passports:
        valid = True
        allKeys = True
        for y in validPassVals:
            if(y not in x.keys()):
                allKeys = False
        if(not allKeys):
            valid = False
            continue
        if(int(x["byr"]) < 1920 or int(x["byr"]) > 2002):
            print(x["byr"])
            valid = False
        if(int(x["iyr"]) < 2010 or int(x["iyr"]) > 2020):
            valid = False
        if(int(x["eyr"]) < 2020 or int(x["eyr"]) > 2030):
            valid = False
        hgt = False
        if(x["hgt"][-2:] == "cm" or x["hgt"][-2:] == "in"):
            if(x["hgt"][-2:] == "cm"):
                if(int(x["hgt"][:-2]) >= 150 and int(x["hgt"][:-2]) <= 193):
                    hgt = True
            else:
                if(int(x["hgt"][:-2]) >= 59 and int(x["hgt"][:-2]) <= 76):
                    hgt = True
        if(not hgt):
            valid = False
        if(not re.search('[^0-9a-f]', x["hcl"]) or len(x["hcl"]) != 7):
            valid = False
        if(x["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            valid  = False
        if(len(x["pid"]) != 9 and not re.search('[^0-9]', x["pid"])):
            print(x["pid"])
            valid = False
        if(valid):
            numValid += 1
    print(numValid)
            

if __name__ == '__main__':
    main()