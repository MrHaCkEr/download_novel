from Abstract_Class import BaseWebSide
from Abstract_Class import Logic


class Qidian(BaseWebSide):
    LIST_ALL_TITLE = "https://www.webnovel.com/popular"
    list_all_title_ajax = "https://www.webnovel.com/apiajax/listing/popularAjax?_csrfToken=vu0HnBRS6ValeqUdXH2MJaH9TgldX4UM1lkCG6Qp&category=&pageIndex="  # na koncu trzeba dodac numer poczatek to 1
    def __init__(self):
        pass

    def start_app(self):
        self.all_title_and_link_from_translating()
        Logic.show_list_in_console(self.tites_of_all_novel)
        number_of_novel=Logic.which_number(len(self.tites_of_all_novel))
        self.get_chapter(self.links_for_all_novel_index[number_of_novel])

    def get_chapter(self, adres):
        soup=self.make_soup(adres)
        soup=soup.find_all("a")
        for s in soup:
            print(s.get("href"))


        print(soup)







    def all_title_and_link_from_translating(self):
        adres="https://www.webnovel.com/book/"
        self.list_all_title_ajax = "https://www.webnovel.com/apiajax/listing/popularAjax?_csrfToken=vu0HnBRS6ValeqUdXH2MJaH9TgldX4UM1lkCG6Qp&category=&pageIndex="
        number_web=1
        self.tites_of_all_novel = []
        self.links_for_all_novel_index=[]
        last_soup=None
        id = "bookId"
        name = "bookName"
        while True:
            soup = self.make_soup(self.list_all_title_ajax+str(number_web))
            if soup == last_soup: break
            str_soup = str(soup)
            s = str_soup.find("items")
            e = str_soup.rfind("totalBooksCnt")
            str_soup = str_soup[s + 8:e - 3]
            list_soup = str_soup.split("]},")
            for sentens in list_soup:
                sentens = sentens.replace(r"\r\n", " ")
                sentens = sentens + "}]},"
                for words in sentens.split(","):
                    if id in words:
                        self.links_for_all_novel_index.append(int(words.split(":")[1].replace('"', "")))
                    elif name in words:
                        self.tites_of_all_novel.append(words.split(":")[1].replace('"', ""))
                        break

            number_web+=1
            last_soup=soup












