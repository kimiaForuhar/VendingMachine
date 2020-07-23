class Vending:
    def __init__(self,id):
        self.id=id
        self.saleamount=0
        self.salecount=0
        self.products={}

    def buy(self,product):
        if product in self.products.items():
            if self.products[product]>0:
                self.products[product]-=1
                self.salecount+=1
                self.saleamount+=int(product.price)
                return True
            return False

    def addprod(self,product,amount):
        if product in self.products:
            self.products[product]+=int(amount)
        else: self.products[product]=int(amount)