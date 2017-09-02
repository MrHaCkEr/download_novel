import os
from string import ascii_letters
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import exc_info

from bs4 import BeautifulSoup

#from pyPdf import PdfFileWriter




class BaseWebSite(object):
    def __init__(self, format):
        self.toFile = ToFile(self, format)
        self.to_file = self.toFile.toFile

    def start_app(self):
        Logic.show_list_in_console(self.list)
        self.choice_of_action = Logic.which_number(len(self.list))
        self.action(self.choice_of_action)

    def action(self, number):
        pass

    def getTitle(self, tites_of_all_novel, number_of_novel):
        self.title = tites_of_all_novel[number_of_novel]
        self.title = self.clean_from_bad_characters(self.title).replace(" ", "_")
        if self.title[-1] == "_":
            self.title = self.title[:-1]

    def make_soup(self, url):
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            return BeautifulSoup(webpage, "html.parser")
        except HTTPError:
            print("it's last chapter")
            exit()
        except:
            print(exc_info())
            exit()

    def clean_to_name_file(self, text):
        new = ""
        for l in text:
            if l not in ("/", "\\", "|", "'", ":", "?", ">", "<"):
                new += l
        return new

    def clean_from_bad_characters(self, text):
        new = ""
        for i in text:
            if i.isdigit() or i in ascii_letters or i == " ":
                new += i
            elif i == "\r\n":
                new += "\r\n"
            elif i in "!%&*()<>?.,:\/{}[];'" or i == '"':
                new += i
        return new


class ToFile(object):
    FORMAT_FILE = ["txt", "pdf"]

    def __init__(self, web, format="txt"):
        self.web = web
        self.format=format
        self.chack_catalog=False

    def toFile(self, text, name):
        if self.format=="txt":
            self.toFileTxt(text, name)
        elif self.format=="pdf":
            self.toFilePdf(text, name)
        else:
            print(self.format)
            print("whay you life, I can't never see you")
            exit()

    def toFileTxt(self, text, name):
        if not self.chack_catalog:
            self.web.title=self.web.title.strip()
            if not os.path.isdir(self.web.title):
                os.makedirs(self.web.title)
            self.chack_catalog = True
        # errors="namereplace" it error is with chinese character
        file = open(os.path.join(os.getcwd(), self.web.title, name + ".txt"), mode="w", errors="namereplace")
        file.write(text)
        file.close()

    def toFilePdf(self, text, name):
        if not self.chack_catalog:
            self.web.title=self.web.title.strip()
            if not os.path.isdir(self.web.title):
                os.makedirs(self.web.title)
            self.chack_catalog = True



    def toOneFilePdf(self):
        pass

    def toOneFileEpub(self):
        pass


class Logic():
    @staticmethod
    def which_number(max, text="give me number", min=0):
        if max - min == 1:
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
        max = len(list)
        max = str(max)
        max = len(max)
        for r, text in enumerate(list):
            print(str(r).rjust(max, "0") + ". " + text)
