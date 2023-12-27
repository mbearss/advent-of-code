if __name__ == '__main__':
    with open('input.txt') as f:
        line = f.read().strip()
        nums = list(map(int, line.split(',')))

    last = dict()
    for i, n in enumerate(nums):
        last[n] = [i]

    while len(nums) < 30000000:
        next = nums[-1]
        if next in last and len(last[next]) > 1:
            d = last[next][-1] - last[next][-2]
            if d in last:
                last[d].append(len(nums))
            else:
                last[d] = [len(nums)]
            nums.append(d)
        else:
            if 0 in last:
                last[0].append(len(nums))
            else:
                last[0] = [len(nums)]
            nums.append(0)

    print('1:', nums[2019])
    print('2:', nums[-1])


