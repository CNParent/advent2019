class Row:
    def __init__(self, data):
        self.data = data

    def countOf(self, c):
        return self.data.count(c)

    def show(self):
        return self.data.replace('0', ' ').replace('1','*').replace('2', ' ')

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

    def countOf(self, c):
        i = 0
        total = 0
        while i < len(self.rows):
            total += self.rows[i].countOf(c)
            i += 1

        return total

    def show(self):
        rows = list(map(lambda x: x.show(), self.rows))
        return '\n'.join(rows)

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

    def render(self):
        data = []
        i = 0
        while i < self.h:
            j = 0
            while j < self.w:
                data.append(self.renderAt(j, i))
                j += 1
            i += 1

        return Layer(self.w, self.h, ''.join(data))

    def renderAt(self, x, y):
        n = len(self.layers)
        i = 0
        while i < n:
            val = self.layers[i].rows[y].data[x]
            if val != '2': return val
            i += 1

def run(args):
    data = args[0]
    img = Image(25,6,data)
    return img.render().show()
