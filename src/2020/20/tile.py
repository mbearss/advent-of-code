class Tile:
    def __init__(self):
        self.id = 0
        self.data = ['0'] * 100
        self.types = []

    def top(self):
        return ''.join(self.data[:10])

    def bottom(self):
        return ''.join(self.data[90:100])

    def left(self):
        return ''.join(x for x in [self.data[10 * r] for r in range(10)])

    def right(self):
        return ''.join(x for x in [self.data[10 * r + 9] for r in range(10)])

    def edge_values(self):
        top = int(self.top(), 2)
        bottom = int(self.bottom(), 2)
        left = int(self.left(), 2)
        right = int(self.right(), 2)
        return [top, right, bottom, left]

    def all_edge_values(self):
        result = set(self.edge_values())
        self.flip_h()
        result = result.union(set(self.edge_values()))
        self.flip_h()
        self.flip_v()
        result = result.union(set(self.edge_values()))
        self.flip_v()
        return result

    def flip_h(self):
        data = ['0'] * 100
        for r in range(10):
            for c in range(10):
                data[10 * r + c] = self.data[10 * r + 10 - c - 1]
        self.data = data

    def flip_v(self):
        data = ['0'] * 100
        for r in range(10):
            for c in range(10):
                data[10 * r + c] = self.data[10 * (10 - r - 1) + c]
        self.data = data

    def rotate(self):
        data = ['0'] * 100
        for r in range(10):
            for c in range(10):
                data[10 * r + c] = self.data[10 * c + 10 - r - 1]
        self.data = data

    def tile_fits_below(self, other):
        bottom = self.bottom()
        if bottom == other.top(): return True
        other.rotate()
        if bottom == other.top(): return True
        other.rotate()
        if bottom == other.top(): return True
        other.rotate()
        if bottom == other.top(): return True
        other.rotate()
        other.flip_h()
        if bottom == other.top(): return True
        other.rotate()
        if bottom == other.top(): return True
        other.rotate()
        if bottom == other.top(): return True
        other.rotate()
        if bottom == other.top(): return True
        return False

    def tile_fits_right(self, other):
        right = self.right()
        if right == other.left(): return True
        other.rotate()
        if right == other.left(): return True
        other.rotate()
        if right == other.left(): return True
        other.rotate()
        if right == other.left(): return True
        other.rotate()
        other.flip_h()
        if right == other.left(): return True
        other.rotate()
        if right == other.left(): return True
        other.rotate()
        if right == other.left(): return True
        other.rotate()
        if right == other.left(): return True
        return False

    def print(self):
        print(self.id, self.edges())
        for r in range(10):
            print(self.data[10 * r:10 * (r + 1)])
        print()