from wuxiaworld import Wuxiaworld
from qidian import Qidian
from Abstract_Class import BaseWebSide
from Abstract_Class import Logic
import json


class Test1(Wuxiaworld):
    TIMES=0
    def __init__(self):
        super(Test1).__init__()
        self.index_adres=self.MAIN_ADRES
        self.number_of_novel=7

    def action(self,number):
        self.all_title_and_link_from_translating(self.OPTIONS_LIST["Chinese"])

        self.index_chapter_adres = self.links_for_all_novel_index[self.number_of_novel]
        adres = self.get_first_chapter(self.index_chapter_adres)
        while True != adres:
            soup = self.download_www_to_text(adres)
            adres = self.get_next_adres(soup)
            if self.TIMES==6:
                break
            self.TIMES+=1

#Test1().action(5)


class Test2(BaseWebSide):
    list_all_title_ajax = "https://www.webnovel.com/apiajax/listing/popularAjax?_csrfToken=vu0HnBRS6ValeqUdXH2MJaH9TgldX4UM1lkCG6Qp&category=&pageIndex=3"
    def __init__(self):
        soup=self.make_soup(self.list_all_title_ajax)
        str_soup=str(soup)

        self.tites_of_all_novel = []
        self.links_for_all_novel_index=[]

        id="bookId"
        name="bookName"

        s=str_soup.find("items")
        e=str_soup.rfind("totalBooksCnt")

        str_soup=str_soup[s+8:e-3]
        list_soup=str_soup.split("]},")

        new_list=[]
        print(("#"*40).join(list_soup))
        for sentens in list_soup:
            sentens=sentens.replace(r"\r\n"," ")
            sentens=sentens+ "}]},"
            for words in sentens.split(","):
                if id in words:
                    self.links_for_all_novel_index.append(int(words.split(":")[1].replace('"',"")))
                elif name in words:
                    self.tites_of_all_novel.append(words.split(":")[1].replace('"',""))
                    break

        for title in self.tites_of_all_novel[-5:]:
            print(title)


class Test3(Qidian):
    def __init__(self):
        adres="https://www.webnovel.com/book/6831850602000905"
        self.get_chapter(adres)











if __name__ == '__main__':
    print("start")
    Test3()
    print("end")