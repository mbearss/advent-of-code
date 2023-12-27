if __name__ == '__main__':
    with open('input.txt') as f:
        time = int(f.readline())
        schedule = list(map(lambda x: int(x) if x != 'x' else 0, f.readline().strip().split(',')))
        bus_id, bus_time = 0, time
        for s in schedule:
            if s == 0:
                continue
            d = -(time % s - s)
            if d < bus_time:
                bus_id, bus_time = s, d
        print('1:', bus_id * bus_time)

        j, d = 0, 1
        for i, s in enumerate(schedule):
            if s == 0:
                continue
            while True:
                j += d
                if (j + i) % s == 0:
                    d *= s
                    break

        print('2:', j)
