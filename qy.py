class plants:
    def plants_info(self):
        print("Plants are the eukaryotes")

class flowers:
    def flowers_info(self):
        print("Flower is the main reproductive part of the plant. ")

class garden(plants, flowers):
    pass


b1 = garden()

b1.plants_info()
b1.flowers_info()
