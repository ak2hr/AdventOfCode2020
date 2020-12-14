
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
            binaryVal = bin(val)[2:].zfill(36)
            result = ""
            for x in range(len(mask)):
                if(mask[x] == 'X'):
                    result += binaryVal[x]
                else:
                    result += mask[x]
            memory[memVal] = int(result, 2)
    total = 0
    for x in memory:
        if(memory[x] != 0):
            total += memory[x]
    print(total)



        



if __name__ == '__main__':
    main()