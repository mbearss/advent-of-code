import numpy as np

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs_region(array, start, visited, region_value):
    stack = [start]
    region = set()

    while stack:
        row, col = stack.pop()

        if visited[row, col]:
            continue

        visited[row, col] = True
        region.add((row, col))

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < array.shape[0] and 0 <= c < array.shape[1]:
                if not visited[r, c] and array[r, c] == region_value:
                    stack.append((r, c))

    return region

if __name__ == '__main__':
    grid = []
    with open('input.txt') as f:
        for line in f:
            grid.append([ord(x) for x in list(line.strip())])

    grid = np.array(grid)

    visited = np.zeros_like(grid, dtype=bool)
    regions = []
    for idx in np.ndindex(grid.shape):
        if visited[idx]:
            continue
        regions.append(dfs_region(grid, idx, visited, grid[idx]))

    part1, part2 = 0, 0
    for region in regions:
        perimeter, corners = 0, 0
        seen = set()

        for row, col in region:
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r, c) not in region:
                    perimeter += 1

            for dx, dy in [
                (-0.5, -0.5),
                (0.5, -0.5),
                (0.5, 0.5),
                (-0.5, 0.5),
            ]:
                corner = (row + dx, col + dy)
                if corner in seen:
                    continue
                seen.add(corner)

                adjacent = sum(
                    (corner[0] + r, corner[1] + c) in region
                    for r, c in [
                        (-0.5, -0.5),
                        (0.5, -0.5),
                        (0.5, 0.5),
                        (-0.5, 0.5),
                    ]
                )

                if adjacent == 1 or adjacent == 3:
                    corners += 1
                elif adjacent == 2:
                    pattern = [
                        (corner[0] - 0.5, corner[1] - 0.5) in region,
                        (corner[0] + 0.5, corner[1] + 0.5) in region,
                    ]
                    if pattern == [True, True] or pattern == [False, False]:
                        corners += 2

        part1 += perimeter * len(region)
        part2 += corners * len(region)

    print('1:', part1)
    print('2:', part2)
