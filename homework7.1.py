class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        f = open(self.__file_name)
        ls_products = f.read()
        f.close()
        return ls_products


    def add(self, *products):
        for x in products:
            ls = list(x.__dict__.values())
            ls_str = list(map(str, ls))
            if ' '.join(ls_str) in self.get_products():
                print(f"Продукт {ls[0]} уже есть в магазине")
            else:
                f = open(self.__file_name, "a")
                f.write(' '.join(ls_str) + "\n")
                f.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
