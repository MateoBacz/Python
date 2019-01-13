import pymysql

"""
obiekt kursora:
Aby móc wykonywać operacje na bazie, potrzebujemy obiektu tzw. kursora służy do pobierania oraz 
modyfikacji danych w bazie danych.
"""
class Helper:

    @classmethod #pozwala na ustanowienie metody statycznej, w tym momencie nie trzeba powtarzać w każdym miejscu print...
    #tylko wpisujemy wszedzie gdzie trzeba Helper.getConnectionMessage() i wtedy przekopiuje wszędzie tekst stąd "Polaczenie..."
    def getConnectionMessage(cls):
        print("Polaczenie ustanowione")

class DBConnect:

    def __init__(self):
        try:
            self.conn = pymysql.connect("localhost", "root", "Stas2016", "text_python")###dane do bazy w MySQL
            #print("polaczenia ustanowione")
            Helper.getConnectionMessage()

            self.logowanie()

        except:
           print ("bledne dane logowania")

    def logowanie(self):

            login = input("podaj login")
            passw = input("podaj haslo")

            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * from logowanie WHERE login=%s and passwd= %s", (login, passw))
            resultsLogs = self.cursor.fetchall() #pobiera wyniki zapytania

            if(len(resultsLogs) == 1):
                print ("zalogowano w systemie")
                self.menu()
            else:
                print ("niepoprawny login lub haslo")
                self.logowanie()

    def menu(self):
        while(True):
            dec = input("S-show, I-insert, D-delete, U-update, Q-exit").upper()

            if(dec=="S"):
                self.select()
            elif(dec=="I"):
                self.insert()
            elif(dec=="D"):
                self.delete()
            elif(dec=="U"):
                self.update()

    def update(self):
        self.select()

        pesel = input("pesel")
        imie = input("imie")
        self.cursor.execute("UPDATE pracownicy SET imie = %s WHERE pesel = %s", (imie, pesel))
        dec = input("czy na pewno chcesz zmienic imie T/N").upper()

        if (dec == "T"):
            self.conn.commit()
            print("Rekord zostal zmieniony")
        else:
            self.conn.rollback()
            print("Powrot do MENU")

    def delete(self):
        self.select()

        pesel = input("pesel")
        self.cursor.execute("DELETE FROM pracownicy WHERE pesel = %s", pesel)
        dec = input("czy na pewno chcesz usunac rekord T/N").upper()

        if(dec=="T"):
            self.conn.commit()
            print("Usunieto rekord")
        else:
            self.conn.rollback()
            print("come to MENU!")

    def insert(self):

        imie     = input("imie")
        nazwisko = input("nazwisko")
        pesel    = input("PESEL")
        data     = input("data")

        self.cursor.execute("INSERT INTO pracownicy (imie, nazwisko, pesel, data_ur) values (%s, %s, %s, %s)",(imie, nazwisko, pesel, data))
        self.conn.commit()

    def select(self):
        self.cursor.execute("SELECT * FROM pracownicy")
        pracownicy = self.cursor.fetchall()

        i = 0

        #print (type(pracownicy))
        for row in pracownicy:
            NAME = 1
            SURNAME = 2
            PESEL = 3
            DATA_URODZENIA = 4
            print (row[NAME], row[SURNAME], row[PESEL], row[DATA_URODZENIA])

DBConnect = DBConnect()

