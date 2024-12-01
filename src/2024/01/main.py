import numpy as np

if __name__ == '__main__':

    s1, s2 = [], []
    with open('input.txt') as f:
        for line in f:
            v1, v2 = [int(x) for x in line.strip().split()]
            s1.append(v1)
            s2.append(v2)

    s1 = np.array(s1)
    s2 = np.array(s2)

    s1.sort()
    s2.sort()

    print('1:', np.sum(np.abs(s1 - s2)))

    unique_s2, counts_s2 = np.unique(s2, return_counts=True)

    mask = np.isin(unique_s2, s1)
    filtered_counts = counts_s2[mask]
    filtered_values = unique_s2[mask]

    result = np.sum(filtered_values * filtered_counts)
    print('2:', result)

