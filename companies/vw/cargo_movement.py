import re


def parse_input():
    with open('input_data/input.txt', 'r') as file:
        # parse input
        is_first_iter = True
        for line in file:
            if is_first_iter:
                num_stacks = (len(line) + 1) // 4
                input = [[] for i in range(num_stacks)]
                is_first_iter = False
            counter = 0
            for i in range(1, len(line), 4):
                if line[i] != ' ' and not line[i].isnumeric():
                    input[counter].append(line[i])
                counter += 1
            if line == "\n":
                break
        plan = []
        for line in file:
            plan.append(re.findall(r'\d+', line))
        return input, plan


def move_cargo():
    input, plan = parse_input()
    for move in plan:
        containers_num, stack_from, stack_to = int(move[0]), int(move[1]) - 1, int(move[2]) - 1
        for _ in range(containers_num):
            container = input[stack_from].pop(0)
            input[stack_to].insert(0, container)
    output = []
    for stack in input:
        output.append(stack[0])
    return output


assert move_cargo(), ['G', 'R', 'T', 'S', 'W', 'N', 'J', 'H', 'H']
print("OK")
