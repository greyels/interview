def make_bricks(small, big, goal):
    if small == goal or big * 5 == goal:
        return True
    x = goal // 5
    y = goal % 5
    if big >= x and small >= y:
        return True
    elif big < x and small >= (goal - big * 5):
        return True
    return False


print(make_bricks(2, 1000000, 100003))
