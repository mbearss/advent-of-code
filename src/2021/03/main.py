import numpy as np
from scipy import stats as st

if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(list(l.strip()) for l in f.readlines())

    data = np.array(data, dtype=int)
    m = np.array(st.mode(data, axis=0)[0], dtype=bool)
    g = int(''.join([str(1 if x else 0) for x in m]), 2)
    e = int(''.join([str(1 if x else 0) for x in np.invert(m)]), 2)
    print('1:', g * e)

    f = np.array(data)
    for i in range(len(f[0])):
        m, c = st.mode(f[:,i])
        ox = m if c != len(f) // 2 else 1
        f = f[f[:,i] == ox]
        if len(f) == 1:
            break
    ox = int(''.join([str(1 if x else 0) for x in f[0]]), 2)

    f = np.array(data)
    for i in range(len(f[0])):
        m, c = st.mode(f[:,i])
        co = (0 if m == 1 else 1) if c != len(f) // 2 else 0
        f = f[f[:,i] == co]
        if len(f) == 1:
            break
    co = int(''.join([str(1 if x else 0) for x in f[0]]), 2)

    print('2:', ox * co)




