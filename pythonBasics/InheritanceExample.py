# Parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print(f'The sku is {self.sku}')


# Parent class 2
class Garment():
    def __init__(self, section, tipo):
        self.section = section
        self.tipo = tipo

    def print_garment(self):
        print(f'The garment is {self.section} and {self.tipo}')


# Child Class
class Shirts(Item, Garment):
    def __init__(self, sku, section, tipo, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, tipo)

    def print_shirt(self):
        print(f'The shirt is {self.sku},  {self.section}, {self.tipo}, '
              f'{self.name}, {self.color}')


Blouse = Shirts('00001', 43, 'Tops', 'Formal Blouse', 'White')
Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()
