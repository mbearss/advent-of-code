from functools import cache

pad1 = {val: (x % 3, x // 3) for x, val in enumerate("789456123.0A")}
pad2 = {val: (x % 3, x // 3) for x, val in enumerate(".^A<v>")}


@cache
def best_dirpad(x, y, dx, dy, robots, invalid):
    ret = None
    todo = [(x, y, "")]

    while len(todo) > 0:
        x, y, path = todo.pop(0)
        if (x, y) == (dx, dy):
            ret = min(filter(lambda x: x is not None, [ret, best_robot(path + "A", robots - 1)]), default=None)
        elif (x, y) != invalid:
            for ox, oy, val in ((-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v")):
                if (ox < 0 and dx < x or ox > 0 and dx > x) or (oy < 0 and dy < y or oy > 0 and dy > y):
                    todo.append((x + ox, y + oy, path + val))

    return ret


@cache
def best_robot(path, robots):
    if robots == 1:
        return len(path)

    ret = 0
    x, y = pad2["A"]

    for val in path:
        dx, dy = pad2[val]
        ret += best_dirpad(x, y, dx, dy, robots, pad2["."])
        x, y = dx, dy

    return ret


def find_path(x, y, dx, dy, robots, invalid):
    ret = None
    todo = [(x, y, "")]
    while len(todo) > 0:
        x, y, path = todo.pop(0)
        if (x, y) == (dx, dy):
            ret = min(filter(lambda x: x is not None, [ret, best_robot(path + "A", robots)]), default=None)
        elif (x, y) != invalid:
            for ox, oy, val in ((-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v")):
                if (ox < 0 and dx < x or ox > 0 and dx > x) or (oy < 0 and dy < y or oy > 0 and dy > y):
                    todo.append((x + ox, y + oy, path + val))
    return ret


if __name__ == '__main__':
    part1, part2 = 0, 0
    with open('input.txt') as f:
        for line in f:
            p1, p2 = 0, 0
            x, y = pad1["A"]
            for val in line.strip():
                dx, dy = pad1[val]
                p1 += find_path(x, y, dx, dy, 3, pad1["."])
                p2 += find_path(x, y, dx, dy, 26, pad1["."])
                x, y = dx, dy
            i = int(line.strip()[:-1].lstrip("0"))
            part1 += p1 * i
            part2 += p2 * i

    print('1:', part1)
    print('2:', part2)
