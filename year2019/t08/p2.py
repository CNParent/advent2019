class Row:
    def __init__(self, data):
        self.data = data

    def show(self):
        return self.data.replace('0', ' ').replace('1','*').replace('2', ' ')

class Layer:
    def __init__(self, w, data):
        self.rows = []
        while len(data) != 0:
            self.rows.append(Row(data[0:w]))
            data = data[w:]

    def show(self):
        rows = list(map(lambda x: x.show(), self.rows))
        return '\n'.join(rows)

class Image:
    def __init__(self, w, h, data):
        self.w = w
        self.h = h
        self.layers = []
        size = w * h
        while len(data) != 0:
            self.layers.append(Layer(w, data[0:size]))
            data = data[size:]

    def render(self):
        data = []
        for i in range(0, self.h):
            for j in range(0, self.w):
                data.append(self.renderAt(j, i))

        return Layer(self.w, ''.join(data))

    def renderAt(self, x, y):
        n = len(self.layers)
        for z in range(0, n):
            val = self.layers[z].rows[y].data[x]
            if val != '2': return val

def run(args):
    data = args[0]
    img = Image(25,6,data)
    return img.render().show()
