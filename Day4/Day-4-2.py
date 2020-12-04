import re

def main():
    global passports
    passports = []
    validPassVals = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    }
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
        if(len(validPassVals.difference(x.keys())) != 0):
            continue
        if(int(x["byr"]) < 1920 or int(x["byr"]) > 2002):
            continue
        if(int(x["iyr"]) < 2010 or int(x["iyr"]) > 2020):
            continue
        if(int(x["eyr"]) < 2020 or int(x["eyr"]) > 2030):
            continue
        if(x["hgt"][-2:] != "cm" and x["hgt"][-2:] != "in"):
            continue
        if(x["hgt"][-2:] == "cm" and (int(x["hgt"][:-2]) < 150 or int(x["hgt"][:-2]) > 193)):
            continue
        if(x["hgt"][-2:] == "in" and (int(x["hgt"][:-2]) < 59 or int(x["hgt"][:-2]) > 76)):
            continue
        if(x["hcl"][0] != '#' or not re.search('[^0-9a-f]', x["hcl"]) or len(x["hcl"]) != 7):
            continue
        if(x["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            continue
        if(len(x["pid"]) != 9 or re.search('[^0-9]', x["pid"])):
            continue
        numValid += 1
    print(numValid)
            

if __name__ == '__main__':
    main()