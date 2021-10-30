class Hall:
    def __init__(self, name, fileName):
        self.name = name

        file = open(fileName)

        infos = file.read().split("\n")

        items = [Item(info) for info in infos]

class Item:
    def __init__(self, info):
        self.name, self.rating = info.split()
