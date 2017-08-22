class AnDict:
    def __init__(self):
        self.items = []

    def put(self, key, value):
        item = self._find_item(key)
        if item:
            item[1] = value
            return

        self.items.append([key, value])

    def get(self, needle):
        item = self._find_item(needle)
        if item:
            return item[1]

    def size(self):
        return len(self.items)

    ## Internal methods ##

    def _find_item(self, needle):
        for item in self.items:
            if item[0] == needle:
                return item

        return None
