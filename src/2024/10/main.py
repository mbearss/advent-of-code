import numpy as np
import networkx as nx

if __name__ == '__main__':
    grid = []
    with open('input.txt') as f:
        for line in f:
            grid.append([int(x) for x in list(line.strip())])

    G = nx.DiGraph()
    grid = np.array(grid)
    for index in np.ndindex(grid.shape):
        G.add_node(index, name=grid[index])

    for index in np.ndindex(grid.shape):
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xp, yp = index[0] + d[0], index[1] + d[1]
            if 0 <= xp < grid.shape[0] and 0 <= yp < grid.shape[1]:
                if grid[index] + 1 == grid[xp, yp]:
                    G.add_edge(index, (xp, yp))


    start_nodes = [node for node, data in G.nodes(data=True) if data['name'] == 0]
    end_nodes = [node for node, data in G.nodes(data=True) if data['name'] == 9]

    score = 0
    rating = 0
    for start in start_nodes:
        reachable_nodes = nx.descendants(G, start)
        count = sum(1 for node in reachable_nodes if G.nodes[node]['name'] == 9)
        score += count

        for target in end_nodes:
            paths = list(nx.all_simple_paths(G, source=start, target=target))
            rating += len(paths)

    print('1:', score)
    print('2:', rating)