f = open("input.txt", "r")

# part 1

def find_overlap(str1, str2):
    str1s = set(str1)
    for i in str2:
        if i in str1s:
            return i

def get_priority(chr):
    base = ord(chr.lower()) - ord('a') + 1
    if chr.isupper():
        return base + 26
    return base

priority_sum = 0

for line in f:
    c1 = line[:len(line) // 2]
    c2 = line[len(line) // 2:-1]
    priority_sum += get_priority(find_overlap(c1, c2))

print(priority_sum)