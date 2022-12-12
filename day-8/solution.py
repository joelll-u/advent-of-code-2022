f = open("input.txt", "r")
forest = f.readlines()
f.close()

# part 1

height = len(forest)
width = len(forest[0]) - 1
visibility_matrix = [[True] * (width - 2) for i in range(height - 2)]

for i in range(1, height - 1):
    max_left = forest[i][0]
    max_right = forest[i][width - 1]

    for ptr in range(1, width - 1):
        # from left
        if forest[i][ptr] > max_left:
            max_left = forest[i][ptr]
            visibility_matrix[i - 1][ptr - 1] = False
        
        # from right
        if forest[i][width - ptr - 1] > max_right:
            max_right = forest[i][width - ptr - 1]
            visibility_matrix[i - 1][width - ptr - 2] = False

for i in range(1, width - 1):
    max_upper = forest[0][i]
    max_lower = forest[height - 1][i]

    for ptr in range(1, height - 1):
        # from upper
        if forest[ptr][i] > max_upper:
            max_upper = forest[ptr][i]
            visibility_matrix[ptr - 1][i - 1] = False
        
        #from lower
        if forest[height - ptr - 1][i] > max_lower:
            max_lower = forest[height - ptr - 1][i]
            visibility_matrix[height - ptr - 2][i - 1] = False

sum_ = 0
for i in visibility_matrix:
    sum_ += sum(i)
print((width * height) - sum_)

scale_array = [[1] * (width - 2) for i in range(height - 2)]

def get_most_recent(val, recent, dist):
    most = max(recent[val:])
    return dist - most

for i in range(1, height - 1):
    recent_left = [0] * 10
    recent_right = [0] * 10

    for ptr in range(1, width - 1):
        # from left
        tree_l = int(forest[i][ptr])
        scale_array[i - 1][ptr - 1] *= get_most_recent(tree_l, recent_left, ptr)
        recent_left[tree_l] = ptr

        tree_r = int(forest[i][width - ptr - 1])
        scale_array[i - 1][width - ptr - 2] *= get_most_recent(tree_r, recent_right, ptr)
        recent_right[tree_r]  = ptr

for i in range(1, width - 1):
    recent_upper = [0] * 10
    recent_lower = [0] * 10

    for ptr in range(1, height - 1):
        # from left
        tree_u = int(forest[ptr][i])
        scale_array[ptr - 1][i - 1] *= get_most_recent(tree_u, recent_upper, ptr)
        recent_upper[tree_u] = ptr

        tree_l = int(forest[height - ptr - 1][i])
        scale_array[height - ptr - 2][i - 1] *= get_most_recent(tree_l, recent_lower, ptr)
        recent_lower[tree_l] = ptr

print(max([max(a) for a in scale_array]))