if __name__ == '__main__':
    with open('input.txt') as f:
        card = int(f.readline().strip())
        door = int(f.readline().strip())

    dl = 1
    while True:
        if pow(7, dl, 20201227) == door:
            break
        dl += 1

    print('p1:', pow(card, dl, 20201227))