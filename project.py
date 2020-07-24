class test1():
    def __init__(self,id):
        self.id=id

    def getid(self,i):
        return i+1


class test2():
    def __init__(self,name):
        self.name=name

    def kkk(self,j):
        print(test1(1).getid(j))


t=test2()
t.kkk(1)
test2('kim').kkk(1)