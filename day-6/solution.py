f = open("input.txt", "r")

line = f.read().rstrip()

#part 1
seen = set()
left = 0
right = 0
while right < len(line):
    if not line[right] in seen:
        if right - left == 3:
            print(right + 1)
            break
        seen.add(line[right])
        right += 1
    else:
        while line[left] != line[right]:
            seen.remove(line[left])
            left += 1
        left += 1
        right += 1