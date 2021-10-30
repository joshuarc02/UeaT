class Hall:
    def __init__(self, name, fileName):
        self.name = name

        file = open(fileName)

        self.items = []
        for line in file:
            name, number = line.rsplit(" ", 1)
            item = Item(name, number)
            self.items.append(item)


class Item:
    def __init__(self, name, number):
        self.name = name
        self.number = number