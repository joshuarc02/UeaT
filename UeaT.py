class Hall:
    names = []

    def __init__(self, name, fileName):
        self.name = name

        file = open(fileName)

        self.items = []
        for line in file:
            name, number = line.strip().rsplit(" ", 1)
            if name in Hall.names:
                continue
            Hall.names.append(name)
            item = Item(name, number)
            self.items.append(item)

        self.items = sorted(self.items, key=lambda item: item.name.lower())


class Item:
    def __init__(self, name, number):
        self.name = name.replace(' ', '_')
        self.number = number

    def getAvaliable(self):
        if self.number == '1':
            return '✓'
        else:
            return 'X'

    def toString(self):
        return item.name + " " + number