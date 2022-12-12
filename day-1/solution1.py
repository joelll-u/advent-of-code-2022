f = open("input1.txt", "r")
curr_max = 0
curr_sum = 0
for line in f:
    if line == "\n":
        if curr_sum > curr_max:
            curr_max = curr_sum
        curr_sum = 0
    else:
        curr_sum += int(line.rstrip())
print(curr_max)