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

# part 2
f.seek(0)

def find_triple_overlap(str1, str2, str3):
    str1s = set(str1)
    str2s = set(str2)
    for i in str3:
        if i in str1s and i in str2s:
            return i
    print(str1, str2, str3)

curr_group = []
badge_sum = 0

for line in f:
    curr_group.append(line.rstrip())
    if len(curr_group) == 3:
        o = find_triple_overlap(curr_group[0], curr_group[1], curr_group[2])
        badge_sum += get_priority(o)
        curr_group = []

print(badge_sum)