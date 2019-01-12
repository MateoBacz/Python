#dziedziczenie
class D:
    arg = 20

class C(D):
    arg = 30

class B(D):
    pass

class A(B, C):
    pass

a = A()

print (a.arg)

################
class A(object):
    def fun(self):
        return "funA invoke"

class B(A):

    def __init__(self):
        self.con = [1,2,3,4,5]
        print (self.fun())
        print (super(B, self).fun()) #super jest po to żeby czytał napis z klasy bazowej
        print (super().fun())
        print (A.fun(self))

    def fun(self):
        return "funB invoke"

b = B()
print (b.fun())

############
###polimorfizm

class Kot:
    def glos(self):
        Print("Miau")

class Pies:
    def glos(self):
        Print("Hau")

class Krowa:
    def glos(self):
        print("Mu")

for zwierze in [Kot(), Pies(), Krowa()]:
    zwierze.glos()

###P71
class Produkt:

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return "%s %5.2f zł " % (self.nazwa, self.cena)

class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa,cena)
        self.jezyk = jezyk
        self.system = system

    def rabat(self, procent):
        if(procent <=10):
            self.cena = round(self.cena - self.cena*(procent/100), 2)

    def __str__(self):
      return super().__str__() + ("%s %s" % (self.jezyk, self.system))

class Szkolenia(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin

    def rabat(self,procent):
        super().rabat(procent)

        if (procent <=15 and procent > 10):
            self.cena = round(self.cena-self.cena*(procent/100),2)

    def __str__ (self):
        return super().__str__() + ("%s" % (self.termin))

class Demo:

    def __init__(self):
        o1 = Oprogramowanie("Python 3.0", 2000, "Python", "Win")
        o1.rabat(7)
        print (o1)
        s1 = Szkolenia("Python podstawy", 1000, "Python", "Win ", "2019-2020")
        s1.rabat(5)
        print (s1)

demo = Demo()

###P72
class RGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __add__(self, other):
        kolorek = RGB((self.r + other.r)/2, (self.g + other.g)/2, (self.b + other.b)/2)
        return kolorek
    def __str__(self):
        return 'RGB[%i, %i, %i]' % (self.r, self.g, self.b)

k1 = RGB (255, 255, 0)
print(k1)
k2 = RGB(0, 0, 255)
print(k2)
k3 = k1 + k2
print(k3)

#########importowanie z innego modułu (np. z Brudnopis), w Brudnopisie było:
#def fun():
    #print ("fun")

import Brudnopis
    Brudnopis.fun()

from Brudnopis import fun
fun()

import Brudnopis
print(dir(Brudnopis))

#Importowanie z innego folderu
from Programming.myFolder.Foo import *
print (fun())

#####P74
import random
import urllib

print(dir(random))
print(dir(urllib))

class Company:

    def fun(self):
        print ("ds")

print(dir(Company))
