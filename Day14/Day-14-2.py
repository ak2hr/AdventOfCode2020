import itertools

memory = {}
mask = []

def main():
    global memory
    global mask
    file = open("Day14/input.txt", "r")
    for line in file:
        if(line[:4] == "mask"):
            mask = line[7:].strip()
        else:
            memVal = line[line.find('[')+1:line.find(']')]
            val = int(line[line.find("= ")+1:])
            binaryMem = bin(int(memVal))[2:].zfill(36)
            
            for combo in itertools.product(['0','1'], repeat = mask.count('X')):
                result = ""
                comboList = list(combo)
                for x in range(len(mask)):
                    if(mask[x] == 'X'):
                        result += comboList.pop(0)
                    elif(mask[x] == '1'):
                        result += '1'
                    else:
                        result += binaryMem[x]
                memory[int(result, 2)] = val
    total = 0
    for x in memory:
        if(memory[x] != 0):
            total += memory[x]
    print(total)



        



if __name__ == '__main__':
    main()