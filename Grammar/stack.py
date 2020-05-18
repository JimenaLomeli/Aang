
class stack():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def top(self):
        try:
            return self.items[-1]
        except:
            pass
