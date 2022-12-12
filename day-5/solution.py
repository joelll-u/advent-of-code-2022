f = open("input.txt", "r")
import re

#part 1 

def read_stack(stack_setup):
    stacks = dict()
    base = stack_setup[-1]
    nums = re.findall(r"(\d+)", base)
    stack_n = int(nums[-1])
    for i_str in nums:
        i = int(i_str)
        stacks[i] = []
        for j in stack_setup[-2::-1]:
            crate = j[(4 * i) - 3]
            if crate == ' ':
                break
            else:
                stacks[i].append(crate)
    return (stack_n, stacks)

stack_text = []
for line in f:
    if line == '\n':
        stack_n, stacks = read_stack(stack_text)
        break
    else:
        stack_text.append(line)

def read_instruction(line):
    return tuple(int(a) for a in re.findall("(\d+)", line))

for line in f:
    quantity, src, dest = read_instruction(line)
    for _ in range(quantity):
        stacks[dest].append(stacks[src].pop())

print(''.join([stacks[i + 1][-1] for i in range(stack_n)]))