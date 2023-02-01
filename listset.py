class ListSet:
    def __init__(self):
        self.items = []

    def insert(self, item):
        # Task 1, Step 1: implement this method
        return False

    def contains(self, item):
        # Task 1, Step 2: implement this method
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
