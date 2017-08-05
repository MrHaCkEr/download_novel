import json
from urllib.request import Request, urlopen

from Abstract_Class import BaseWebSide
from Abstract_Class import Logic


class Qidian(BaseWebSide):
    def __init__(self):
        pass

    def start_app(self):
        self.all_title_and_link_from_translating()
        Logic.show_list_in_console(self.tites_of_all_novel)
        number_of_novel=Logic.which_number(len(self.tites_of_all_novel))
        self.get_chapter(self.links_for_all_novel_index[number_of_novel])

    def get_chapter(self, number):
        adres = "https://www.webnovel.com/apiajax/chapter/GetChapterList?_csrfToken=vu0HnBRS6ValeqUdXH2MJaH9TgldX4UM1lkCG6Qp&bookId=%s&_=1501845622524" % number
        req = Request(adres, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = json.loads(webpage)
        chapterItems = webpage["data"]["chapterItems"]
        bookName = webpage["data"]["bookInfo"]["bookName"]
        self.title = bookName
        bookId = webpage["data"]["bookInfo"]["bookId"]

        for i in chapterItems:
            text = self.download_www_to_text(i["chapterId"], bookId)
            name = "%s-%s-%s" % (bookName, str(i["chapterIndex"]).rjust(4).replace(" ", "0"), i["chapterName"])
            name = self.clean_to_name_file(name.replace(" ", "_"))
            self.to_file(text, name)
            print(name)

    def download_www_to_text(self, chapterId, bookId):
        www = "https://www.webnovel.com/book/%s/%s" % (bookId, chapterId)
        soup = self.make_soup(www)
        text = soup.find("div", class_="cha-words")
        return text.text

    def all_title_and_link_from_translating(self, number_web=1):
        self.tites_of_all_novel = []
        self.links_for_all_novel_index=[]
        id = "bookId"
        name = "bookName"
        while True:
            adres_all_title_ajax = "https://www.webnovel.com/apiajax/listing/popularAjax?_csrfToken=vu0HnBRS6ValeqUdXH2MJaH9TgldX4UM1lkCG6Qp&category=&pageIndex=" + str(
                number_web)
            req = Request(adres_all_title_ajax, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            webpage = json.loads(webpage)
            items = webpage["data"]["items"]
            if not len(items): break
            number_web+=1

            for dic in items:
                self.links_for_all_novel_index.append(dic["bookId"])
                self.tites_of_all_novel.append(dic["bookName"])
