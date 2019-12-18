class Shape:
    def __init__(self,n):
        self.side=n
    def tri(self,len,height):
        self.h=height
        self.l=len
    def rect(self,len,breadth):
        self.l=len
        self.b=breadth
    def cir(self,radius):
        self.r=radius
    '''
    def display(self):
        
            print("It is a triangle")
        
            print("It is a sqaure or a rectangle")
        else:
            print("It is a circle")
    '''
class Triangle(Shape):
    def area(self):
        a=0.5*self.l*self.h
        print("Area of trinagle is:",a,"sq m")
class Rectangle(Shape):
    def area(self):
        self.a=self.l*self.b
    def display(self):
        print("Area of rectangle is:",self.a,"sq m")
class Sqaure(Rectangle,Shape):
    def sqarea(self):
        print("Area of square is:",self.a,"sq m")
class Circle(Shape):
    def area(self):
        a=self.r*self.r*3.14
        print("Area of circle is:",a,"sq m")
    def perimeter(self):
        p=2*3.14*self.r
        print("Perimeter of circle is:",p,"m")

n=int(input("Enter the no of sides:"))
s=Shape(n)
T=Triangle(n)
R=Rectangle(n)
C=Circle(n)
S=Sqaure(n)
if n==4:
    len=int(input("Enter length:"))
    breadth=int(input("Enter breadth:"))
    if(len!=breadth):
        R.rect(len,breadth)
        R.area()
        R.display()
    else:
        S.rect(len,breadth)
        S.area()
        S.sqarea()

elif n==3:
    height=int(input("Enter height:"))
    len=int(input("Enter length:"))
    T.tri(len,height)
    T.area()
elif n==0:
    radius=int(input("Enter radius:"))
    C.cir(radius)
    C.area()
    C.perimeter()






