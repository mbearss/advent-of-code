import re

def run(matches, part1=True):
    sum, enable = 0, True
    for m in matches:
        if m == "do()":
            enable = True
        elif m == "don't()":
            enable = False | part1
        elif enable:
            a, b = re.findall(r'\d{1,3}', m)
            sum += int(a) * int(b)
    return sum

if __name__ == '__main__':

    records = []
    with open('input.txt') as f:
        data = ''.join(f.readlines())

    matches = re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', data)

    print('1:', run(matches))
    print('2:', run(matches, False))