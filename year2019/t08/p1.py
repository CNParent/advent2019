class Row:
    def __init__(self, data):
        self.data = data
        print(data)

    def countOf(self, c):
        return self.data.count(c)

class Layer:
    def __init__(self, w, h, data):
        self.w = w
        self.h = h
        self.rows = []
        i = 0
        while i < self.h:
            s = i * self.w
            e = s + self.w
            self.rows.append(Row(data[s:e]))
            i += 1
        
        print('\n')

    def countOf(self, c):
        i = 0
        total = 0
        while i < len(self.rows):
            total += self.rows[i].countOf(c)
            i += 1

        return total

class Image:
    def __init__(self, w, h, data):
        self.w = w
        self.h = h
        self.size = w * h
        self.data = data
        self.layers = []
        nlayers = len(data) / self.size
        i = 0
        while i < nlayers:
            s = i * self.size
            e = s + self.size
            self.layers.append(Layer(w, h, data[s:e]))
            i += 1


def run(args):
    data = args[0]
    img = Image(25,6,data)
    i = 0
    counts = []
    while i < len(img.layers):
        counts.append(img.layers[i].countOf('0'))
        i += 1

    minCount = min(counts)
    i = counts.index(minCount)

    ones = img.layers[i].countOf('1')
    twos = img.layers[i].countOf('2')
    return ones * twos
