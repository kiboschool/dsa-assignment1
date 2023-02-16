class SortedListSet:
    def __init__(self):
        self.items = []

    def insert(self, item):
        if item in self.items:
            return False

        # insert item into its sorted position in list
        for idx, lst_item in enumerate(self.items):
            if item < lst_item:
                self.items = self.items[:idx] + [item] + self.items[idx:]
                return True

        # item is the greatest in the set
        self.items.append(item)
        return True

    def contains(self, item):
        for lst_item in self.items:
            if item < lst_item:
                return False
            if item == lst_item:
                return True
        return False

    def delete(self, item):
        if item not in self.items:
            return False

        self.items.remove(item)
        return True

    def size(self):
        return len(self.items)

    def to_list(self):
        return self.items.copy()
