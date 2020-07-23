from Vending import vendingM

m = int(input())
productList = []
vendingList = []
for i in range(m):
    id = int(input())
    name = input()
    price = int(input())
    productList.append(vendingM.Product(id, name, price))

for j in range(int(input())):
    vendingList.append(vendingM.Vending(j))
    p = input().split()
    for k in range(1, len(p)):
        vendingList[j].addprod(int(k), 1)

for t in range(int(input())):
    inp = input().split()
    vendingList[int(inp[0]) - 1].buy(int(inp[1]) - 1)

for h in range(len(vendingList)):
    print(h, ":", vendingList[h].saleamount, ",", vendingList[h].salecount)
