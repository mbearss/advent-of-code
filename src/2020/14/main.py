import numpy as np

def dec_to_bin(x):
    i = 2**35
    y = []
    while i >= 1:
        if x // i == 1:
            y.append(1)
            x -= i
        else:
            y.append(0)
        i //= 2
    return np.array(y, dtype=bool)

def bin_to_dec(x):
    y = 0
    for i, v in enumerate(x[::-1]):
        y += 2**i * v
    return y


if __name__ == '__main__':
    mask = np.zeros(shape=(2, 36), dtype=bool)
    memory = np.zeros(shape=(2**36, 36), dtype=bool)
    modified = set()
    with open('input.txt') as f:
        for line in f:
            token = line.strip().split(' ')
            if token[0] == 'mask':
                mask[0] = [0 if x == 'X' else 1 for x in token[2]]
                mask[1] = [1 if x == '1' else 0 for x in token[2]]
            elif token[0][:3] == 'mem':
                addr = int(token[0][4:-1])
                val = dec_to_bin(int(token[2]))

                val[mask[0] & mask[1]] = 1
                val[mask[0] & np.invert(mask[1])] = 0
                modified.add(addr)
                memory[addr] = val

    print('1:', sum(map(bin_to_dec, memory[list(modified)])))

    mask = np.zeros(shape=(2, 36), dtype=bool)
    memory = np.zeros(shape=(2**36, 36), dtype=bool)
    modified = set()
    with open('input.txt') as f:
        for line in f:
            token = line.strip().split(' ')
            if token[0] == 'mask':
                mask[0] = [0 if x == '0' else 1 for x in token[2]]
                mask[1] = [1 if x == '1' else 0 for x in token[2]]
            elif token[0][:3] == 'mem':
                addr = dec_to_bin(int(token[0][4:-1]))
                val = dec_to_bin(int(token[2]))
                addr[mask[0] & mask[1]] = 1

                floating = [addr]
                for i, v in enumerate(mask[0] & np.invert(mask[1])):
                    if v:
                        r = len(floating)
                        for j in range(r):
                            x = np.array(floating[j])
                            x[i] = 0
                            floating.append(x)
                            x = np.array(floating[j])
                            x[i] = 1
                            floating.append(x)
                        del floating[:r]
                for a in floating:
                    #print(bin_to_dec(a))
                    ab = bin_to_dec(a)
                    modified.add(ab)
                    memory[ab] = val

    print('2:', sum(map(bin_to_dec, memory[list(modified)])))

