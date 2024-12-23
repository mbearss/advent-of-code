from itertools import combinations
import networkx as nx

if __name__ == '__main__':
    G = nx.Graph()

    with open('input.txt', 'r') as f:
        for line in f:
            G.add_edge(*line.strip().split('-'))

    cliques = list(nx.find_cliques(G))

    cliques_of_size_3 = []
    for clique in cliques:
        if len(clique) == 3:
            cliques_of_size_3.append(clique)
        elif len(clique) > 3:
            cliques_of_size_3.extend(list(combinations(clique, 3)))

    cliques_of_size_3 = list(set([tuple(sorted(clique)) for clique in cliques_of_size_3]))

    p1 = len([clique for clique in cliques_of_size_3 if any(node.startswith('t') for node in clique)])
    print('1:', p1)

    largest_clique = max(cliques, key=len)
    print('2:', ','.join(sorted(largest_clique)))