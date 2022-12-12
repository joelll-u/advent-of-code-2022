f = open("input.txt", "r")

line = f.read().rstrip()

#part 1
def find_distinct_char(line, n):
    seen = set()
    left = 0
    right = 0
    while right < len(line):
        if not line[right] in seen:
            if right - left == (n - 1):
                return right + 1
            seen.add(line[right])
            right += 1
        else:
            while line[left] != line[right]:
                seen.remove(line[left])
                left += 1
            left += 1
            right += 1

print(find_distinct_char(line, 4))
print(find_distinct_char(line, 14))