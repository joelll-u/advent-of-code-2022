# Part 1

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

# Part 2
f.seek(0)
top3 = [0, 0, 0]

def add_to_top3(num):
    for i in range(3):
        if num > top3[i]:
            top3.insert(i, num)
            top3.pop()
            break

curr_sum = 0
for line in f:
    if line == "\n":
        add_to_top3(curr_sum)
        curr_sum = 0
    else:
        curr_sum += int(line.rstrip())
print(sum(top3))
f.close()