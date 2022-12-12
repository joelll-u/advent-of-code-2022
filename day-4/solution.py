import re

f = open("input.txt", 'r')

#part 1

def read_line(l):
    bounds =  re.findall("(\d+)", l)
    return [int(a) for a in bounds]

def has_containing(bounds):
    l1, u1 = bounds[0], bounds[1]
    l2, u2 = bounds[2], bounds[3]
    return (l1 >= l2 and u1 <= u2) or (l2 >= l1 and u2 <= u1)

containing = 0 
for line in f:
    if has_containing(read_line(line)):
        containing += 1
print(containing)

#part 2
f.seek(0)

def find_overlap(bounds):
    l1, u1 = bounds[0], bounds[1]
    l2, u2 = bounds[2], bounds[3]
    max_l = max(l1, l2)
    min_u = min(u1, u2)
    if max_l > min_u:
        return False
    else:
        return True

overlaps = 0
for line in f:
    if find_overlap(read_line(line)):
        overlaps += 1
print(overlaps)
f.close()