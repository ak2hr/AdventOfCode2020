file = open("Day1/input.txt", "r")

nums = []
for line in file:
    nums.append(int(line))
for x in range(len(nums)):
    for y in range(x+1, len(nums)):
        for z in range(y+1, len(nums)):
            if(nums[x] + nums[y] + nums[z] == 2020):
                print(nums[x], ",", nums[y], ",", nums[z])
                print(nums[x] * nums[y] * nums[z])
