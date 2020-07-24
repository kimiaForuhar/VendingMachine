class Vending_machine:
    # products={}
    def __init__(self, id):
        self.id = id
        self.saleamount = 0
        self.salecount = 0
        self.products = {}

    def buy(self, product):
        if product in self.products.keys():
            if self.products[product] >= 1:
                self.products[product] -= 1
                self.salecount += 1
                for i in productList:
                    if i.id == product:
                        self.saleamount += int(i.price)
                        break

    def addprod(self, product, amount):
        if product in self.products.keys():
            self.products[product] += int(amount)
        else:
            self.products[product] = int(amount)


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


print('number of products you want to add to machine: ')
m = int(input())
productList = []
vendingList = []
for i in range(m):
    print('product id: ')
    id = int(input())
    print("product name: ")
    name = input()
    print("product price: ")
    price = int(input())
    productList.append(Product(id, name, price))

print("number of vending machines you wish to have: ")
n=int(input())
print("""first enter the number of products you want to add to machin then enter the products ids:
(Note:products in the FIRST line will be added to vending machine with id=1 and so on)""")
for j in range(n):
    vendingList.append(Vending_machine(j))
    p = input().split()
    for k in range(1, len(p)):
        vendingList[j].addprod(int(p[k]), 1)

print('number of your orders:')
print("""first enter the vending id you wish to buy from then enter the product id
(NOTE: each line takes one machine id and one product id.)""")
for t in range(int(input())):
    inp = input().split()
    vendingList[int(inp[0]) - 1].buy(int(inp[1]))

for h in range(len(vendingList)):
    print('vendin machine', h + 1, ":", vendingList[h].salecount, ' product(s) were sold' ",", vendingList[h].saleamount,
          "$s earned")
