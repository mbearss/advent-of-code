import math

from tile import Tile

monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]
monster = [[1 if c == '#' else 0 for c in m] for m in monster]


def assemble1(corner_tiles, tiles, size):
    r = 0
    for c in corner_tiles:
        r += assemble2(c, tiles, size)
        c.rotate()
        r += assemble2(c, tiles, size)
        c.rotate()
        r += assemble2(c, tiles, size)
        c.rotate()
        r += assemble2(c, tiles, size)
        c.rotate()
        c.flip_h()
        r += assemble2(c, tiles, size)
        c.rotate()
        r += assemble2(c, tiles, size)
        c.rotate()
        r += assemble2(c, tiles, size)
        c.rotate()
        r += assemble2(c, tiles, size)
        c.rotate()

        if r != 0:
            return r


def assemble2(corner_tile, tiles, size):
    grid = [[None for _ in range(size)] for _ in range(size)]
    used = []

    grid[0][0] = corner_tile
    used.append(corner_tile)
    return assemble3(tiles, grid, used, size)


def assemble3(tiles, grid, used, size):
    if len(tiles) == len(used):
        return find_monster(grid)

    n = len(used)
    col = n % size
    row = n // size

    check_left = True if col > 0 else False
    check_above = True if row > 0 else False

    for curr in tiles:
        if curr in used:
            continue

        if check_above and check_left:
            res = grid[row - 1][col].tile_fits_below(curr) and grid[row][col - 1].tile_fits_right(curr)
            if res:
                grid[row][col] = curr
                used2 = used + [curr]
                return assemble3(tiles, grid, used2, size)
        elif check_above:
            res = grid[row - 1][col].tile_fits_below(curr)
            if res:
                grid[row][col] = curr
                used2 = used + [curr]
                return assemble3(tiles, grid, used2, size)
        elif check_left:
            res = grid[row][col - 1].tile_fits_right(curr)
            if res:
                grid[row][col] = curr
                used2 = used + [curr]
                return assemble3(tiles, grid, used2, size)
    return 0


def find_monster(grid):
    dim = len(grid)
    size = 8 * dim
    image = [[8 for _ in range(size)] for _ in range(size)]
    for r in range(dim):
        for c in range(dim):
            t = grid[r][c]
            for i in range(8):
                for j in range(8):
                    v = int(t.data[10 * (i + 1) + (j + 1)])
                    image[r * 8 + i][c * 8 + j] = v

    total = sum(sum(i) for i in image)
    need = sum(sum(k) for k in monster)
    found = 0
    for x in range(len(image) - len(monster)):
        for y in range(len(image[0]) - len(monster[0])):
            count = sum([1 for i in range(len(monster)) for j in range(len(monster[0])) if
                         image[x + i][y + j] == 1 and monster[i][j] == 1])
            if count == need:
                found += 1
                total -= need

    if found > 0:
        return total
    return 0


if __name__ == '__main__':
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.append(line.strip())

        tiles, tile = [], None
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith('Tile'):
                tile = Tile()
                tile.data = []
                tile.id = int(line.split()[1][:-1])
                for j in range(10):
                    i += 1
                    line = lines[i]
                    tile.data += [x for x in line.replace('.', '0').replace('#', '1')]
                tiles.append(tile)
            i += 1

    all_edge_values = {}
    for t in tiles:
        edge_values = t.all_edge_values()
        for e in edge_values:
            if e in all_edge_values:
                all_edge_values[e] += 1
            else:
                all_edge_values[e] = 1

    sides = {x for x in all_edge_values if all_edge_values[x] == 1}

    result = 1
    for t in tiles:
        if sum([True if s in sides else False for s in t.edge_values()]) == 2:
            result *= t.id

    print('1:', result)

    all_edge_values = {}
    for t in tiles:
        edge_values = t.all_edge_values()
        for e in edge_values:
            if e in all_edge_values:
                all_edge_values[e] += 1
            else:
                all_edge_values[e] = 1

    sides = {x for x in all_edge_values if all_edge_values[x] == 1}

    corners = []
    for t in tiles:
        if sum([True if s in sides else False for s in t.edge_values()]) == 2:
            corners.append(t)

    result = assemble1(corners, tiles, int(math.sqrt(len(tiles) + 1)))
    print('2:', result)
