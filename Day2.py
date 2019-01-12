"""
a = [eval(input("Enter number1")), eval(input("Enter number2")), eval(input("Enter number3")), eval(input("Enter letter a")), eval(input("Enter letter b"))]

List = []
for elem in a:
    if type(elem) is str:
        List.append(elem)

print (List)
print ("done")
"""

#######################
#Zajęcia
#######################

#P39
"""
numbers = {
    'jeden' : 1,
    'dwa'   : 2,
    'trzy'  : 3,
    'cztery': 4,
    'pięć'  : 5
}

number = input ("Type number")
print (numbers[number]) #słownik więc muszą być nawiasy kwadratowe
"""
#P41
kod = input ("Podaj kod produktu")
ilosc = int(input("Podaj ilosc produktu"))

produkty = {
    "k1" : ("Czekolada", 10.0),
    "k2" : ("Kanapka", 12.0),
    "k3" : ("Alko", 155.0)
}

print ("suma [zł]", produkty[kod][1]*ilosc, produkty[kod][0])

#kluczem w skłownku może być krotka i słownik, ale lista już nie bo jest zmienialna
#######

#Operacje na zbiorach

a = [1,2,3,4] #lista
b = (4,5,6,7) #krotka

aSet = set(a)
bSet = set(b)

print (aSet | bSet)
print (aSet & bSet)
print (aSet - bSet)
print (bSet - aSet)
print (aSet ^ bSet) #różnica symetryczna wywala wspólną wartość zbiorów


#P42
from random import randint
lotto = set()
while(len(lotto) < 6):
    lotto.add(randint(1, 49))
print (lotto)

#P43
X = list(range(0,21,2))
Y = list(range(0,11,1))

XY = (X,Y)
print(XY[0][0],XY[1][0])
print(XY[0][1],XY[1][1])

lista = []
#y = 1/2x
count = 0
while count <11:
    a = (count*2, count)
    lista.append(a)
    count=count+1
print(lista)

#P44
a = input("Numer1"), input("Numer2"), input("Numer3"), input("Numer4"), input("Numer5")

aSet = set(a)

print(len(aSet))


##### II opcja

x = input("podaj wartosc")
mojSet = set()
while x != 'exit': #jeżeli wpiszemy "exit" to program się wyłączy
    if x in mojSet: # te dwie linijki pozwalają na to
        exit() #że jak użytownik wprowadzi drugi raz ten sam numer to program się wyłączy
    mojSet.add(x)
    x = input("podaj wartosc")
print(len(mojSet))

#######
if 1<2:
    print ("Dobrze")
elif 1<3:
    print("Źle")
else:
    pass

#####
a = 9
b = 6

print(b) if (a<b) else print(a)

#P45

Test = list(range(0,5))
if(bool(Test[0])):
    print(Test[0])

if(bool(Test[1])):
    print(Test[1])

if(bool(Test[2])):
    print(Test[2])

if(bool(Test[3])):
    print(Test[3])

if(bool(Test[4])):
    print(Test[4])

#P46
x = int(input("podaj wartosc"))
a = range(0,10)
if x in a:
    print ("ok")
else:
    print ("out of range")

#II versja
x = int(input("podaj wartosc"))
if x >=0 and x <=9:
    print("ok")
else:
    print("out of range")

#P47
Elem = [3,8,3,4,4]

if Elem[0] >= 0 and Elem[1] >= 0:
    print("dwie dodatnie")
elif Elem[0] >= 0 or Elem[1] >= 0:
    print ("jedna dodatnia")
else:
    print("wszystkie ujemne")

#P48   #BŁĄD - spisać z Trello
dictionary = {
    0 : "parzyste",
    1 : "nieparzyste"
}

print (dictionary[(int(input('podaj liczbe') % 2))])

#P49

# user  : user
# admin : admin

access_dictionary = {

    "user"  :  "user",
    "admin" :  "admin"
}

login    = input("podaj login")
password = input("podaj haslo")

if login in access_dictionary and password == access_dictionary[login]:
    print ("zalogowany!")

    if login == "admin":
        print ("panel admina")
    else:
        print ("panel uzytkownika")
else:
    print ("nieprawidłowe dane")

#########
a = ['a', 'b', 'c', 'd', 'e']

for index, value in enumerate(a):
    print (index,value)

zmienna = enumerate(a, 10)
print (list(zmienna)

#########
for x in range (5,100,10):
    print ("%14i%10i%40i" % (x, x**2, x**3)) #i dziesiętna liczba całkowita, % to odpowiednik każdego x, cyfra to wcięcie kolumny, odstęp

for x in range (5,100,10):
    print ("pierwiastkiem liczby %2i jest %6.4f" % (x, x**0.5)) #% odpowiednik x, i dziesiętna liczba, f liczba zmiennopozycyjna w postaci ułamka dziesiętnego, 4 ilość liczb po przeicnku

for x in range(5,100,10):
    print ("%-3i%#-6o%#-5x" % (x,x,x)) # - powoduje, że liczby są ustawione do lewej krawędzi

for x in range(5,100,10):
    print ("%3i %#08o %#04x" % (x,x,x)) #0 - powoduje, że zamiast spacji jest 0

##################

a = 24
b = "sample"
c = 27
d = "text"

print (str(a) + b + str(c) + d) #bez spacji
print ("%i %s %i %s" % (a,b,c,d)) #lepszy format, już jest spacja

######################
liczby = [eval(input("Podaj liczbe")),
          eval(input("Podaj liczbe")),
          eval(input("Podaj liczbe"))]

szukana = eval(input("Podaj liczbę do znalezienia"))
for p,x in enumerate(liczby):
    if x != szukana:
        continue
    print("Znaleziono liczbę %i na pozycji %i" % (x,p+1)) #p to pozycja na liście, bo pierwszs jest 0 więc musi wiświetlić od 1
    break
else:
    print("Liczby %i nie ma na liście" % szukana)

#P51

cyfry = {
    1 : "jeden",
    2 : "dwa",
    3 : "trzy",
    4 : "cztery",
    5 : "pięć",
    6 : "sześć",
    7 : "siedem",
    8 : "osiem",
    9 : "dziewięć"
}
a = input("Podaj liczbę")
result = ""
for znak in a:
    if(znak.isdigit()):
        result += cyfry[int(znak)]
        result += " "
    else:
        result += "x"
        result += " "
print (result)

#P53

for x in range (3,10,1):
    print (x**2)

###
liczba = 3
while(liczba > 0 and liczba < 10):
    print('%2i - %2i' % (liczba, liczba**2))
    liczba +=1

#P54

numbers = [5, 2, 1, 10]

print(numbers.index(int(input("podaj numer"))))

#P55

#celcius = (fahrenheit - 32) / 1.8

cel = list(range(-20,45,5))

for x in range(-20,45,5):
    print(x,"C",(x * 1.8) +32, "F")

# sformatować na jutro żeby ciągi tekstu były koło siebie, żeby powstała tabelka.
for x in range(1,11):
    for y in range(1,11):
        print (x*y)
    print("\n")
print(x*y)

###### tabliczka mnożenia
for x in range(1, 11):
        for y in range(1, 11):
            z = x * y
            print(z, end="\t")
        print()

        # lista a i dodać nową listę z elementami >3 z listy a
        a = [1, 2, 3, 4, 5]
        new_list = []
        for elem in a:
            if elem > 3:
                new_list.append(elem)
            else:
                pass
        print(new_list)

        print([elem for elem in a if elem > 3])  # to samo w jednej linii

        a = [1, 2, 3, 4, 5]
        new_list = []

        for elem in a:
            new_list.append(elem * 2)
        print(new_list)

        print([elem * 2 for elem in a])

        # P56 DZIEKANAT
        oceny = [2, 3, 3.5, 4, 4.5, 5]
        wprowadzone = []
        suma = 0

        while 1 == 1:
            ocena = input("wprowadz ocene")
            if ocena == "":  # jak użytkownik wciśnie sam enter
                for ocena in wprowadzone:
                    suma = suma + ocena
                break
            else:
                try:  # try wstawia sie kiedy jest możliwość że użytkownik wprowadzi błąd, potem wprowadza się except żeby wyskakiwało że coś źle zrobiono
                    ocena = float(ocena)
                    if ocena in oceny:
                        wprowadzone.append(ocena)
                    else:
                        print("nie ma takiej oceny!")
                except:
                    print("bledna wartosc")

        print('Średnia ocen: %4.1f' % (suma / len(wprowadzone)))  # f liczba z przecinkiem 1 miejsce po przecinku
