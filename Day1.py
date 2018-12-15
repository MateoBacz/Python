a = 1
print (type(a))

a = "sample text"
print (type(a))

a = 1.0
print (type(a))

pi = 3.14
print (type(pi))

myChar = 'a'
print (type(myChar))

imie = "Anna"
adres_zamieszkania= "Nieznana 20"
#adres-zamieszkania = "Nieznana 20"
drugie_imię= "Beata"
#3ulubionePotrawy = "x, y, z"
#and = 51
and_Dana= 1023
And = "hello"
#twoje zainteresowania = „nurkowanie”
twoje2samochody = "v, m"
śćółżęąćł= " :-) "
twojaSzczesliwaLiczbaKtoraWylosowanoSpecjalnieDlaCiebie= 5

"""
Komentarz wielolinijkowy, '#' - na krótki komentarz, na długi 3x"
"""
#P0a
a = 45
b = "Szkolenie"
c = 23.5
d = "Test"
e = "?"

print(a)
print(b)
print(c)
print(d)
print(e)

#####################
# Syntax
#####################

a = 1
b = '1'
c = 1.0

print (a)
a= 20

#####################
# Tuple - krotka - wszystko liczy się od zera. Pierwsza pozycja na liście jest na pozycji 0
#####################

a = (1,2,3)
print (type(a))

print (a[0])
print (a[1])
print (a[2])

a = (1,2,3,'s','a','m','p','l','e')
print (type(a))

print (a[4])

#one element tuple (przecinek)
a = (1,)
print (type(a))

#TUPLE IS IMMUTABLE! niemodyfikowalna
#a[0] = 4

#3 typy krotek
a = (1,2,3,'s','a','m','p','l','e')
print (type(a))

a = 1,2,3,'s','a','m','p','l','e'
print (type(a))

a = tuple((1,2,3))
print(type(a))

#####################
# List - w porównaniu do krotki jest modyfikowalna
#####################

a = [1,2,3,4,5,'s','a','m','p','l','e']
print (type(a))

print (a[7])

#podmiana wartości na drugim miejscu bo w Python liczy się od 0
a[2] = "nowa"
print(a)

#dodaje wartości na końcu listy
a.append('nowa2')
print(a)

#wstawia element, reszte przesuwa ale nie wymienia
a.insert(2,'nowa3')
print(a)

#usuwanie elementu
del a[0]
print(a)

#pokazuje ilość elementów w liście
print(len(a))

#tworzenie krotki na podstawie listy
a_tuple = tuple(a)
print (type(a_tuple))

############
a = 1
b = 2

c = a
a = b
b = c

print (a) #2
print (b) #1

a = 1
b = 2

a,b = b,a

print (a) #2
print (b) #1

#pętla for each
a = [1,2,3,4,5,'s','a','m','p','l','e']
for elem in a:
    print (elem) #tabulator musi być (tabulator to 4*spacja

a = list(range(1,6,1)) #od 1 do 6 ale bez 6, liczone co 1
print (a)

for elem in a:
    print (elem) #pętla idzie 5 razy

a = list(range(1,6,1)) #od 1 do 6 ale bez 6, liczone co 1
print (a)
my_list = [1,2,3,'log',4,5,'s','a','m','p','l','e'] #pętla--- czyta listę, od pozycji zero, potem pokazuje co tam jest,
# potem counter +1 id od początku aż dojedzie do ostatniej pozycji czyli 5, bo a zdefiniowaliśmy że jest do 5
counter = 0
for elem in a:

    print (my_list[counter])
    counter +=1 #counter = counter + 1

###############################################
my_tuple = ('a','b','c')
for abc in my_tuple:
    print (abc)

a = list(range(1,3,1)) #definiuje ile razy ma iść pętla
print (a)
counter = 0
for abc in a:
    print (my_tuple[counter])
    counter +=1

################################################

a = [1,2,3,4,5]

for elem in a:
    print (elem * 2)

a = ['a','b','c']
for elem in a:
    print (elem * 2)

a = [1,2,3,4,5,6,7,8,9,10]
a = list(range(1,11,1))

new_list = []
new_list2 = []
for elem in a:
    if elem > 3:
        new_list.append(elem)
    else: #albo zmiast "else" dodać "elif elem <=3:"
        new_list2.append(elem)
print (new_list)
print (new_list2)

#lista liczb podzielnych przez 2
a = [1,2,3,4,5,6,7,8,9,10]
#liczba%2 liczby parzyste

lista_parzyste = []
for elem in a:
    if elem %2 == 0: #dzielenine przez 2 musi być równe 0
        lista_parzyste.append(elem)
print (lista_parzyste)

a = "sample text"
for x in a:
    print (x)
#############################
counter = 0
while counter<5:
    print (counter)
    counter +=1
#############################

while 1==1:
    counter = 4
    if counter > 0:
        break #przerywa działanie pętli
    counter =- 1

if 1<2:
    pass

####################
# set - zbiory, elementy nie mogą się powtarzać, nieuporządkowane
####################

a = [1,1,1,2,3,4,5]
b = 'sample text'
c = (1,2,1,2,3)

a_set = set(a)
print (type(a_set))
b_set = set(b)
print (type(b_set))
c_set = set(c)
print (type(c_set))

print (a_set) #pokazuje tylko jeden z powtarzających się elementów ponieważ w zbiorze nic nie może się powtarzać
print (b_set)
print (c_set)

for abc in a_set:
    if abc ==1:
        print ("ok istnieje")

print (1 in a)

a = {1,1,2,3}
print(a)

a.add(1) #nie doda bo już jest
a.add(4)
print(a)

a.remove(1) #usuwa wartość 1, nie można użyć del bo przy del trzeba podać miejsce elementu, a zbiór jest nieuporządkowany, losowy
#ale remove usuwa tylko pierwszy element, jeżeli jest kilka 1 to usunie tylko pierwszą jedynkę
print(a)

a = [1,2,3]
a_set = frozenset(a) #frozenset jest niemodyfikowalny

######################
#Dictionary - słownik/tablica inicjacyjna
######################

numbers = {
    'a': 2,
    'b': 3,
    'c': 4
}

print (numbers)
print (type(numbers))
print (numbers['b'])

print (numbers.keys())
print(numbers.values())
print(numbers.items()) #lista krotek

items = numbers.items()
for item in items:
    print(item)
    print(item[0]) #pokazuje a - pierwsza wartość
    print (item[1])#pokazuje 2 - druga wartość
###############
a = [1,2,3,4,5,6,7,8,9,10]
print(a[0:3:1])
print(a[0:7:2])
print(a[9])
print(a[len(a) -1])

#last element
print (a[-1]) #-1 ostatni
print (a[-1:-4:-1])
print(a[::])
print(a[::-1])

text = "sample text"
textList = text.split(" ")
print(textList)
print ("|".join(textList))

a = "sample text"
print (a[::-1])

#P0c
a = "Ciekawe"
b = "Programowanie"
c = "Jest"
d = "Wciągające"
e = "I"

print(b+" "+c+" "+a+" "+e+" "+d)


eval ("2+2") #zamienia ciąg tekstowy na kod

#P7d
czas_kolor = 5
ilość_kolor = 2
czas_cb = 2
ilość_cb = 8
czas = 45
print((czas/czas_kolor*ilość_kolor))
print((czas/czas_cb*ilość_cb))
print ((czas/czas_kolor*ilość_kolor)+ (czas/czas_cb*ilość_cb))

############################
a = 1
print (str(a))

print (str(1) + "a") #nie można zrobić 1+a żeby wyszło 1a, trzeba z 1 zrobić string str(1)

#P10

brutto = 1000
VAT3 = 0.03
VAT7 = 0.07
VAT23 = 0.23

print(round(brutto/(VAT3+1),2))
print(round(brutto/(VAT7+1),2))
print(round(brutto/(VAT23+1),2))

#P11
print((2*1.99)+(2.5*0.5)+(0.3/1)*12.99)

#011 is equal to 1*(8**1) + 1*(8**0) = 9
a = 0o11
print(a)

#0o27 is equal to 2*(8**1) + 7*(8**0) = 16 + 7 =23
a = 0o27
print(a)

#P16
a = 7
print(bool(a))

#P22
Imię = 'Zenon'
Nazwisko = 'Nowak'
Wiek = 35
Pensja = 6000
Stanowisko = 'młodszy inżynier procesu'

print(10 * ("Pan "+Imię+" "+Nazwisko+"(wiek: "+str(Wiek)+" lat) "+"pracuje na stanowisku: "+Stanowisko+" (pensja: "
            +str(Pensja)+" brutto)"))


#a = input("enter number 1")
#b = input("enter number 2")

#P22a
Dochód = 700
Koszt = 500
Zysk = 200
Miesiąc1 = 700*1.5
Miesiąc2 = Miesiąc1*1.5
Miesiąc3 = Miesiąc2*1.5
Miesiąc4 = Miesiąc3*1.5
Miesiąc5 = Miesiąc4*1.5
Miesiąc6 = Miesiąc5*1.5

print(round((Miesiąc1-Koszt),2))
print(round((Miesiąc2-Koszt),2))
print(round((Miesiąc3-Koszt),2))
print(round((Miesiąc4-Koszt),2))
print(round((Miesiąc5-Koszt),2))

#P25
Wynagrodzenie = 5500
Czas = 168

print(round((Wynagrodzenie/Czas),2))
print(round((Wynagrodzenie/Czas)*1.23,2))

#P27
a = bool(0)
b = bool(0)
c = bool(1)

W1 = (not a) and (not b) and (not c)
W2 = (not a) and (not b) and (c)
W3 = (not a) and (b) and (not c)
W4 = (a) and (not b) and (not c)
W = W1 or W2 or W3 or W4
print(W)

print("\"")

#imie = input("Wczyta napis")
#print (30*(imie + "\n"))

#P37
#wysokość = input("Podaj wysokość")
#długość = input ("Podaj długość")
#print("Pole trójkąta wynosi: "+str((0.5*float(wysokość)*float(długość))))


a = "aaaaabbbbccc"

dictionary = dict()
for letter in a:
    if letter in dictionary:
        dictionary[letter] = dictionary[letter] + 1
    else:
        dictionary[letter] = 1
print (dictionary)





















a = "aaaabbbbbccc"



