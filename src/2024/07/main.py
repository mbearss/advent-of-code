import itertools

def eval_no_order(values, operators):
    result = values[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += values[i + 1]
        elif op == '*':
            result *= values[i + 1]
        elif op == '|':
            result = int(str(result) + str(values[i + 1]))
    return result

def run(ops):
    sum = 0
    for i in range(len(y)):
        op_p = list(itertools.product(ops, repeat=len(x[i]) - 1))
        done = False
        for op_perm in op_p:
            if done:
                continue
            result = eval_no_order(x[i], op_perm)
            if result == y[i]:
                sum += y[i]
                done = True
    return sum

if __name__ == '__main__':

    y = []
    x = []
    with open('input.txt') as f:
        for line in f:
            eq = line.split()
            y.append(int(eq[0].split(':')[0]))
            x.append([int(i) for i in eq[0].split(':')[1].split() + eq[1:]])

    print('1:', run(['+', '*']))
    print('2:', run(['+', '*', '|']))