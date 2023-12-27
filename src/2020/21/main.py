from collections import defaultdict

if __name__ == '__main__':

    allergen_map = defaultdict(list)
    ing_count = defaultdict(int)
    with open('input.txt') as f:
        for line in f:
            ing, allergen = line.strip()[:-1].split(' (contains ')
            ing = ing.split()
            allergen = allergen.split(', ')

            for a in allergen:
                allergen_map[a].append(set(ing))
            for i in ing:
                ing_count[i] += 1

    graph = {}
    contains = defaultdict(bool)
    for a in allergen_map:
        inter = set.intersection(*allergen_map[a])
        graph[a] = inter
        for i in inter:
            contains[i] = True

    p1 = 0
    for i in ing_count:
        if not contains[i]:
            p1 += ing_count[i]
    print('1:', p1)

    taken = set()
    items = []
    while True:
        for a in allergen_map:
            inter = set.intersection(*allergen_map[a])
            if len(inter - taken) == 1:
                o = min(inter - taken)
                items.append((a, o))
                taken.add(o)
                break
        else:
            break
    print('2:', ",".join(x[1] for x in sorted(items)))
