import os
from string import ascii_letters
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class BaseWebSide(object):
    def __init__(self,adres,options_list):
        self.index_adres = adres
        self.list = list(options_list)

    def start_app(self):
        Logic.show_list_in_console(self.list)
        self.choice_of_action=Logic.which_number("podaj numer ",len(self.list))
        self.action(self.choice_of_action)

    def action(self,number):
        pass


    def getTitle(self, tites_of_all_novel, number_of_novel):
        self.title = tites_of_all_novel[number_of_novel]
        self.title = self.clean_from_bad_characters(self.title).replace(" ", "_")
        if self.title[-1] == "_":
            self.title = self.title[:-1]

    def make_soup(self,url):
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            return BeautifulSoup(webpage, "html.parser")
        except:
            print("ostatnia strona")
            exit()

    def clean_from_bad_characters(self, text):
        new = ""
        for i in text:
            if i.isdigit() or i in ascii_letters or i == " ":
                new += i
            if i == "\r\n":
                new += "\r\n"
            if i in "!%&*()<>?.,:\/{}[];'" or i == '"':
                new += i
        return new

    def to_file(self, text,name):
        if not os.path.isdir(self.title):
            os.makedirs(self.title)
        # errors="namereplace" powoduje brak problemu z wystepujacymi chinskimi znakami
        file = open(os.path.join(os.getcwd(), self.title, name  + ".txt"),mode="w",errors="namereplace")
        file.write(text)
        file.close()


class Logic():

    @staticmethod
    def which_number(max,text="podaj numer", min=0):
        if max-min==1:
            return 0
        number = min - 1
        while min > number or number >= max:
            number = input(text + " ")
            if not number.isdigit():
                print("nie podales samej cyfry")
                number = min - 1
            number = int(number)
        return number

    @staticmethod
    def show_list_in_console(list):
        max=len(list)
        max=str(max)
        max=len(max)
        for r,text in enumerate(list):
            print(str(r).rjust(max,"0")+". "+text)



