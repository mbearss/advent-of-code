import re

from computer import Computer


def simulate_until_loop(c: Computer):
    run = set()
    while True:
        run.add(c.ip)
        if c.step(v=False):
            return False
        if c.ip in run:
            return True


if __name__ == '__main__':
    with open('input.txt') as f:
        org_tape = f.read()
        c = Computer(org_tape)

        simulate_until_loop(c)
        print('1:', c.acc)

        for i in re.finditer('nop', org_tape):
            c2 = Computer(org_tape[:i.start()] + 'jmp' + org_tape[i.end():])
            if not simulate_until_loop(c2):
                break

        for i in re.finditer('jmp', org_tape):
            c2 = Computer(org_tape[:i.start()] + 'nop' + org_tape[i.end():])
            if not simulate_until_loop(c2):
                break

        print('2:', c2.acc)
