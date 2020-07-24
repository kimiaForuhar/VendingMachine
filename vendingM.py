class Vending_machine:
    def __init__(self, id):
        self.id = id
        self.saleamount = 0
        self.salecount = 0
        self.products = {}


    def buy(self, product):
        if product in self.products.keys():
            if self.products[product] > 0:
                self.products[product] -= 1
                self.salecount += 1
                self.saleamount += int(Product(id=product,).getprice(product))
            #     return True
            # return False

    def addprod(self, product, amount):
        if product in self.products.keys():
            self.products[product] += int(amount)
        else:
            self.products[product] = int(amount)


class Product:
    # prod = {}

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def getprice(self, id):
        for i in productList:
            if i.id == id:
                return i.price


m = int(input())
productList = []
vendingList = []
for i in range(m):
    id = int(input())
    name = input()
    price = int(input())
    productList.append(Product(id, name, price))
    # Product.prod[id]=[name,price]
# print(productList[1].price)

for j in range(int(input())):
    vendingList.append(Vending_machine(j))
    p = input().split()
    for k in range(1, len(p)):
        vendingList[j].addprod(int(p[k]), 1)

for t in range(int(input())):
    inp = input().split()
    vendingList[int(inp[0]) - 1].buy(int(inp[1]) - 1)

for h in range(len(vendingList)):
    print(h+1, ":", vendingList[h].saleamount, ",", vendingList[h].salecount)
