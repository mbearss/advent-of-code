import numpy as np
from collections import defaultdict

RENDER = False

direction_map = {
    0: (0, 1),  # East
    1: (1, 0),  # South
    2: (0, -1), # West
    3: (-1, 0)  # North
}

if __name__ == '__main__':
    grid = []
    with open('input.txt') as f:
        for line in f:
            grid.append(list(line.strip()))

    start, end = None, None
    for i, line in enumerate(grid):
        if 'S' in line:
            start = (i, line.index('S'))
        if 'E' in line:
            end = (i, line.index('E'))

    wall = np.array([['#' in item for item in row] for row in grid])

    unvisited = np.zeros((wall.shape[0], wall.shape[1], 4))
    distance = np.full_like(unvisited, np.inf, dtype=float)
    parent = defaultdict(list)
    distance[start[0], start[1], 0] = 0

    while True:
        x = distance + unvisited
        cur = np.unravel_index(np.argmin(x, axis=None), x.shape)
        if distance[cur] == np.inf:
            break

        dx, dy = direction_map[cur[2]]

        x, y = cur[0] + dx, cur[1] + dy
        if not wall[x, y]:
            new_dist = distance[cur] + 1
            if new_dist < distance[x, y, cur[2]]:
                distance[x, y, cur[2]] = new_dist
                parent[(x, y, cur[2])] = [cur]
            elif new_dist == distance[x, y, cur[2]]:
                parent[(x, y, cur[2])].append(cur)

        new_dist = distance[cur[0], cur[1], cur[2]] + 1000
        next_dir = (cur[2] + 1) % 4
        if new_dist < distance[cur[0], cur[1], next_dir]:
            distance[cur[0], cur[1], next_dir] = new_dist
            parent[(cur[0], cur[1], next_dir)] = [cur]
        elif new_dist == distance[cur[0], cur[1], next_dir]:
            parent[(cur[0], cur[1], next_dir)].append(cur)

        prev_dir = (cur[2] - 1) % 4
        if new_dist < distance[cur[0], cur[1], prev_dir]:
            distance[cur[0], cur[1], prev_dir] = new_dist
            parent[(cur[0], cur[1], prev_dir)] = [cur]
        elif new_dist == distance[cur[0], cur[1], prev_dir]:
            parent[(cur[0], cur[1], prev_dir)].append(cur)

        unvisited[cur] = np.inf

    end_direction = np.argmin(distance[end[0], end[1], :])

    all_path_nodes = set()
    stack = [(end[0], end[1], end_direction)]
    while stack:
        cur = stack.pop()
        if cur not in all_path_nodes:
            all_path_nodes.add((cur[0], cur[1]))
            stack.extend(parent[cur])

    if RENDER:
        for i in range(len(wall)):
            for j in range(len(wall[i])):
                if wall[i, j]:
                    print('#', end='')
                elif (i, j) in all_path_nodes:
                    print('O', end='')
                else:
                    print('.', end='')
            print()

    print('1:', int(distance[end[0], end[1], end_direction]))
    print('2:', len(all_path_nodes))
