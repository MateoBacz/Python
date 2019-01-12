#########
#Funkcje
#########

def calculate_square(x):
    return x**2

print (calculate_square(3))

def calculate_even(x):
    if x % 2 ==0:
        return "parzysta"
    else:
        return "nieparzysta"


print(calculate_even(5))
print(calculate_even(x=10))

###########
def fun(*args):#* używamy kiedy chcemy podać różną ilość argumentów
    suma = 0

    for x in args:
        suma += x
    return suma

print (fun(1,2,3,4,5))
print (fun(1,2,3))
print (fun(1))

#######silnia
def silnia(n):
    wynik = 1
    while(n > 1):
        wynik *= n #wynik * n
        n -= 1
    return wynik

print (silnia(5))

## ciąg fibonacciego
def fib(n):
    L = [1,1]
    i = 2
    while(i <= n):
        L.append(L[i-2]+L[i-1])
        i+=1
    return L
    #return sum(L)
print(fib(8))

#P59
from random import randint

def losowe_zdanie(n=5):

    wyrazy = ["ala", "ma", "kota",
              "a", "kot", "ma", "ale"]
    i = 0
    zdanie = ""
    while i < n:
        index_los = randint(0, len(wyrazy) -1)
        zdanie += wyrazy[index_los]
        i +=1
    return zdanie

print(losowe_zdanie(3))

#P60
def dist(x1, y1, x2, y2):
    import math

    roz_y = y2 - y1
    roz_x = x2 - x1

    if roz_y < 0:
        roz_y = roz_y + roz_y * 2
    if roz_x < 0:
        roz_x = roz_x + roz_x * 2

    kw_przec = roz_y * roz_y + roz_x * roz_x
    przec = math.sqrt(kw_przec)
    return przec


print(dist(1, 1, 2, 2))

##II wersja

def distance(p1, p2):
    return ((p2[0]-p1[0])**2 + (p2[1] - p1[1])**2)**0,5

p1_x = int(input('p1_x:'))
p1_y = int(input('p1_y:'))
p2_x = int(input('p2_x:'))
p2_y = int(input('p2_y:'))

print (distance( (p1_x,p1_y), (p2_x,p2_y) ))

#P61
#an = a1 * g ** (n-1) #n ty wyraz ciągu geometrycznego
#Sn = a1 * ((1-q ** n) / (1 - q)) #suma ciągu geometrycznego

def suma_i_wyraz(n, a1 = 1, q = 2):
    licznik = 1 - q ** n
    mianownik = 1 - q
    wynik = a1 * licznik/mianownik
    print(wynik, a1 * q ** (n-1))

print (suma_i_wyraz(4,3,2))

#P62
def avg(*n):
    if len(n) > 0:
        print(sum(n)/len(n))
    else:
        print("0")

avg(1,2)

#P63
def myHTML(color = 'black', size = 16, text = 'Lorem Ipsum'):
    return '<span style="color: %s; font-size: %s; ">%s</span>' % (color, size, text)

print(myHTML())

#P64
color = 'white'
def color_change():
    global color
    if color == "white":
        color = "black"
    else:
        color = "white"
    return color

print (color_change())
print (color_change())
print (color_change())
print (color_change())
print (color_change())
print (color_change())

#P65
from random import randint
def fun(min, ilosc):

    lst = []
    for elem in range(0, ilosc):
        lst.append(randint(-1000, 1000))

    print (lst, "wylosowane liczby")

    lst_upper_than_min = []

    suma = 0
    for elem in lst:
        if elem > min:
            lst_upper_than_min.append(elem)
            suma += elem
    print (lst_upper_than_min, "wylosowane liczby", suma)

fun(10,5)

##############
def fun(**args): #**zamienia na słownik i wtedy trzeba podać klucz i wartość np. a = 1
    return args

print(fun(a = 1, b = 2, c = 3))
print(fun(a = 1, b = 2))
print(fun(a = 1))

#sprawdzamy czy coś jest palindromem
def fun(text):
    if str(text) == str(text)[::-1]:
        print("Jest palindromem")
    else:
        print("Nie jest palindromem")
    pass

fun("kajak")
fun("palindrom")

###########programowanie obiektowe

class Felga:

    def __init__(self, marka, rozmiar, szerokość):
        self.marka = marka
        self.rozmiar   = rozmiar
        self.szerokość = szerokość

    def __str__(self):
        return self.marka + " " + str(self.rozmiar) + " " + str(self.szerokość)


class Car:

    def __init__(self, color, moc, marka, felga):
        print ("init")
        self.color = color
        self.moc   = moc
        self.marka = marka
        self.bak   = 0
        self.felga = felga
        self.spalanie = 6 #6L/10

    def __str__(self):
        return self.color + " " + self.moc + " " + str(self.bak) + " " + self.felga.marka


    def go_speed(self):
        return "jedź szybko"

    def tankuj(self, ilość_litrów):
        self.bak += ilość_litrów

   # def __calculate_petrol(self, distance):
        #if self.bak <= 0




    def jedź(self, distans):
        self.spalanie
        if self.bak <=0:
            return "bak pusty"
        else:
            self.bak = self.bak - (distans/100) * self.spalanie

bbs = Felga("bbs", 18, 9)
oz = Felga("oz", 20, 10)

print(bbs)
print(oz)

polonez = Car("green", "60KM", "polonez", bbs)
audi    = Car("black", "130KM", "audi", oz)
ford    = Car("white", "105KM", "ford", oz)

print (polonez.color)
print (audi.color)
print (ford.color)

print(polonez)
print(audi)
print(ford)

print (polonez.go_speed())
audi.tankuj(10)
audi.tankuj(15)
print(audi)

audi.jedź(100)
print(audi)

################
class Cat:

    def __init__(self, name):
        self.name = name

    def __add__(self, other_cat):
        print ("add invoke")
        return self.name + " " + other_cat.name

    def __sub__(self, other_cat):
        return self.name + " " + other_cat.name + " odejmowanie"

cat1 = Cat("mruczek")
cat2 = Cat("filemon")

print (cat1 + cat2)
print (cat1 - cat2)

##############
class Zawodnik:

    def __init__(self, imie, waga, wzrost):
        self.imie   = imie
        self.waga   = waga
        self.wzrost = wzrost

    def __str__(self):
        return self.imie + " "

    def oblicz_BMI(self):
        BMI = round((self.waga/(((self.wzrost/100)**2))),2)
        return str(BMI)

Adam = Zawodnik("Adam", 94, 185)

print(Adam)
print(Adam.oblicz_BMI())


################## Lotto
from random import randint
class Lotto:

    def __init__(self):
        self.wynik = set()

    def losuj(self):
        while (len(self.wynik) < 6):
            self.wynik.add(randint(1,49))

    def pokaz(self):
        return self.wynik

los1 = Lotto()
los2 = Lotto()
los3 = Lotto()

los1.losuj()
print (los1.pokaz())
los2.losuj()
print (los2.pokaz())
los3.losuj()
print (los3.pokaz())

# print dir(a) - wyświetla metodę


phone = {'a': '2', 'b': '22', 'c': '222',
         'd': '3', 'e': '33', 'f': '333',
         'g': '4', 'h': '44', 'i': '444',
         'j': '5', 'k': '55', 'l': '555',
         'm': '6', 'n': '66', 'o': '666',
         'p': '7', 'q': '77', 'r': '777', 's': '7777',
         't': '8', 'u': '88', 'v': '888',
         'w': '9', 'x': '99', 'y': '999', 'z': '9999', ' ' : '#'}

text = input ("Zdanie")
for elem in text:
    print (phone[elem.lower()], end="")
