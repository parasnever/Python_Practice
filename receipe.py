class Recipe():
    def __init__(self,dish,items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish +  " has " + str(self.items) + \
            " and takes " + str(self.time) +" min to prepare." )

pizza = Recipe("pizza", ["chesse", "butter", "tomato"], 45)
pasta =Recipe("pasta",["penne","sauce"],55)

print(pizza.items)
print(pasta.items)

print(pizza.contents())
print(pasta.contents())