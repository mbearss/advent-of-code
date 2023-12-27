import re

if __name__ == '__main__':
    passport = []
    with open('input.txt') as f:
        p = {}
        for line in f:
            tokens = line.split()
            if len(line.strip()) == 0:
                passport.append(p)
                p = {}
            else:
                for t in tokens:
                    k, v = t.split(':')
                    p[k] = v

    passport.append(p)

    p1, p2 = 0, 0
    for p in passport:
        if len(p) == 8 or len(p) == 7 and 'cid' not in p:
            p1 += 1
        else:
            continue
        if not (1920 <= int(p['byr']) <= 2002):
            continue
        if not (2010 <= int(p['iyr']) <= 2020):
            continue
        if not (2020 <= int(p['eyr']) <= 2030):
            continue
        if p['hgt'][-2:] == 'cm' and 150 <= int(p['hgt'][:-2]) <= 193:
            pass
        elif p['hgt'][-2:] == 'in' and 59 <= int(p['hgt'][:-2]) <= 76:
            pass
        else:
            continue
        if not re.match(r'^#[0-9a-f]{6}$', p['hcl']):
            continue
        if p['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        if not re.match(r'^\d{9}$', p['pid']):
            continue
        p2 += 1


    print('1:', p1)
    print('2:', p2)
