class AnDict:
    def __init__(self):
        self.items = []

    def put(self, key, value):
        self.items.append([key, value])

    def get(self, needle):
        for item in self.items:
            if item[0] == needle:
                return item[1]

    def size(self):
        return len(self.items)
