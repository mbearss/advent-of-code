import numpy as np
from heapq import heappush, heappop


def a_star(grid, start, goal):
    rows, cols = grid.shape

    def is_valid_position(pos):
        r, c = pos
        return 0 <= r < rows and 0 <= c < cols and grid[r, c] == 0

    def heuristic(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    open_set = []
    heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse the path

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            neighbor = (current[0] + dr, current[1] + dc)
            if is_valid_position(neighbor):
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    if neighbor not in [item[1] for item in open_set]:
                        heappush(open_set, (f_score[neighbor], neighbor))

    return []


if __name__ == "__main__":
    grid_size = (71, 71)
    goal = (grid_size[0] - 1, grid_size[1] - 1)
    bytes = []
    with open('input.txt') as f:
        for line in f:
            bytes.append(tuple(map(int, line.strip().split(','))))

    grid = np.zeros(grid_size, dtype=bool)

    for i in range(1024):
        grid[bytes[i]] = True

    path = a_star(grid, (0, 0), goal)
    print('1:', len(path) - 1)

    i += 1
    while i < len(bytes):
        grid[bytes[i]] = True
        if not a_star(grid, (0, 0), goal):
            break
        i += 1

    print(f"2: {bytes[i][0]},{bytes[i][1]}")
