def is_adjacent(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x2 - x1) < 2 and abs(y2 - y1) < 2

def new_tail_pos(cur_pos, head_pos):
    if not is_adjacent(cur_pos, head_pos):
        x, y = cur_pos
        xh, yh = head_pos
        if abs(x - xh) == 2 and abs(y - yh) == 2:
            if x > xh and y > yh:
                return (x - 1, y - 1)
            elif x > xh:
                return (x - 1, y + 1)
            elif y > yh:
                return (x + 1, y - 1)
            else:
                return (x + 1, y + 1)

        elif abs(x - xh) == 2:
            if x > xh:
                return (x - 1, yh)
            else:
                return (x + 1, yh)
        else:
            if y > yh:
                return (xh, y - 1)
            else:
                return (xh, y + 1)
    else:
        return cur_pos

def update_head(head_x, head_y, dir):
    if dir == 'U':
        head_y += 1
    elif dir == 'D':
        head_y -= 1
    elif dir == 'L':
        head_x -= 1
    else:
        head_x += 1
    return (head_x, head_y)

file = open("input.txt", "r")
instructions = file.readlines()
file.close()

# part 1
head_x, head_y = (0,0)
tail_pos = (0,0)
tail_visited = set()

for i in instructions:
    dir, n = tuple(i.split())
    for _ in range(int(n)):
        head_x, head_y = update_head(head_x, head_y, dir)
        tail_pos = new_tail_pos(tail_pos, (head_x, head_y))
        tail_visited.add(tail_pos)

print(len(tail_visited))

head_x, head_y = 0, 0
rope_pos = [(0, 0) for i in range(9)]
tail_visited = set()
for i in instructions:
    dir, n = tuple(i.split())
    for _ in range(int(n)):
        head_x, head_y = update_head(head_x, head_y, dir)
        part_ahead = (head_x, head_y)
        for part in range(9):
            rope_pos[part] = new_tail_pos(rope_pos[part], part_ahead)
            part_ahead = rope_pos[part]
        tail_visited.add(rope_pos[-1])

print(len(tail_visited))
