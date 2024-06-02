class one:
    a=20
    b=40
    def add(self):
        z=self.a+self.b
        print(z)
class second(one):
    def sub(self):
        x=self.a-self.b
        print(x)
class third(one):
    def mul(self):
        y=self.a*self.b
        print(y) 
class four(one):
    def div(self):
        w=self.a/self.y
        print(w)
class five(third,four):
    def mod(self):
        r=self.a%self.b
        print(r)
k=five()
k.add()
k.sub()
k.mul()
k.div()
k.mod()               