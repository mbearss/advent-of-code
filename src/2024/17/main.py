import re
from z3 import Optimize, BitVec

def run(A, B, C, program):
    inst = 0
    out = []
    while inst < len(program) - 1:
        lit = program[inst + 1]
        combo = lit
        if lit == 4:
            combo = A
        elif lit == 5:
            combo = B
        elif lit == 6:
            combo = C

        if program[inst] == 0:
            A //= 2 ** combo
        elif program[inst] == 1:
            B ^= lit
        elif program[inst] == 2:
            B = combo % 8
        elif program[inst] == 3:
            if A != 0:
                inst = lit
                continue
        elif program[inst] == 4:
            B ^= C
        elif program[inst] == 5:
            out.append(combo % 8)
        elif program[inst] == 6:
            B = A // 2 ** combo
        elif program[inst] == 7:
            C = A // 2 ** combo

        inst += 2
    return out

if __name__ == '__main__':
    with open('input.txt') as f:
        A = int(re.findall(r'\d+', f.readline())[-1])
        B = int(re.findall(r'\d+', f.readline())[-1])
        C = int(re.findall(r'\d+', f.readline())[-1])
        f.readline()
        program = [int(x) for x in f.readline().strip()[9:].split(',')]

    print('1:', ','.join(str(x) for x in run(A, B, C, program)))

    loop = [(1, 0)]
    pos = []
    for i, a in loop:
        for a in range(a, a + 8):
            if run(a, 0, 0, program) == program[-i:]:
                loop += [(i + 1, a * 8)]
                if i == len(program):
                    pos.append(a)

    print('2:', min(pos))




