class AnDict:
    items = []

    def __init__(self):
        pass

    def put(self, key, value):
        self.items.append([key,value])

    def get(self, key):
        return self.items[0][1]