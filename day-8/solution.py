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



