import networkx as nx


def check_order(p):
    g = G.subgraph(p)
    for i in range(len(p)-1):
        for j in range(i + 1, len(p)):
            if not nx.has_path(g, p[i], p[i + 1]):
                return False
    return True

def get_order(p):
    g = G.subgraph(p)
    source = [n for n in g.nodes if g.in_degree(n) == 0][0]
    sink = [n for n in g.nodes if g.out_degree(n) == 0][0]
    return longest_path_dag(g, source, sink)


def longest_path_dag(dag, source, sink):
    topological_order = list(nx.topological_sort(dag))

    distances = {node: float('-inf') for node in dag.nodes}
    distances[source] = 0
    predecessors = {node: None for node in dag.nodes}

    for node in topological_order:
        if node in distances and distances[node] > float('-inf'):
            for neighbor in dag.successors(node):
                if distances[neighbor] < distances[node] + 1:
                    distances[neighbor] = distances[node] + 1
                    predecessors[neighbor] = node

    # Backtrack to find the longest path
    path = []
    current = sink
    while current is not None:
        path.append(current)
        current = predecessors[current]

    return path[::-1] if path[-1] == source else []


if __name__ == '__main__':

    G = nx.DiGraph()
    pages = []
    with open('input.txt') as f:
        for line in f:
            if '|' in line:
                a, b = [int(c) for c in line.split('|')]
                G.add_edge(a, b)
            elif ',' in line:
                pages.append(list(int(c) for c in line.split(',')))

    part1 = 0
    part2 = 0
    for p in pages:
        if check_order(p):
            part1 += p[len(p) // 2]
        else:
            part2 += get_order(p)[len(p) // 2]

    print('1:', part1)
    print('2:', part2)
