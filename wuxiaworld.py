from Abstract_Class import BaseWebSide
from Abstract_Class import Logic


class Wuxiaworld(BaseWebSide):
    MAIN_ADRES = "http://www.wuxiaworld.com/"
    OPTIONS_LIST = {"Completed": "menu-item-12207", "Chinese": "menu-item-2165", "Korean": "menu-item-116520"}
    NEXTCOMMAND = "Next Chapter"

    def __init__(self):
        super(Wuxiaworld, self).__init__(self.MAIN_ADRES, self.OPTIONS_LIST.keys())

    def action(self, number):
        self.all_title_and_link_from_translating(self.OPTIONS_LIST[self.list[number]])
        Logic.show_list_in_console(self.tites_of_all_novel)
        self.number_of_novel = Logic.which_number(len(self.tites_of_all_novel))

        # self.get_link_all_chapter_from_index(self.links_for_all_novel_index[self.number_of_novel])

        self.index_chapter_adres = self.links_for_all_novel_index[self.number_of_novel]
        adres = self.get_first_chapter(self.index_chapter_adres)
        while True != adres:
            soup = self.download_www_to_text(adres)
            adres = self.get_next_adres(soup)

    def get_next_adres(self, soup):
        for link in soup.find_all('a')[:]:
            if link.text == self.NEXTCOMMAND:
                return link.get("href")
        return True

    def get_first_chapter(self, adres):
        self.getTitle(self.tites_of_all_novel, self.number_of_novel)
        soup = self.make_soup(adres)
        # soup = soup.find(itemprop="articleBody")
        for link in soup.find_all('a'):
            if "chapter-1" in str(link.get('href')):
                return link.get('href')
        raise "I can't find first chapter"

    def get_link_all_chapter_from_index(self, adres):
        self.getTitle(self.tites_of_all_novel, self.number_of_novel)
        print(self.title)
        soup = self.make_soup(adres)
        soup = soup.find(itemprop="articleBody")
        for link in soup.find_all('a')[:]:
            adres = link.get('href')
            if adres[-4:] != ".jpg" and "index" in adres:
                print(link.text)
                print(adres)
                print("#" * 20)
                self.download_www_to_text(adres, link.text)

    # download all titles with links
    def all_title_and_link_from_translating(self, table):
        soup = self.make_soup(self.index_adres)
        self.links_for_all_novel_index = []
        self.tites_of_all_novel = []
        soup = soup.find(id=table)
        for link in soup.find_all('a')[1:]:
            text = link.text
            text = self.clean_from_bad_characters(text)
            text = text.replace("()", "")
            self.tites_of_all_novel.append(text)
            self.links_for_all_novel_index.append(link.get('href'))

    def download_www_to_text(self, adres):
        print(adres)
        name = adres.split("/")
        if "index" in name[-2]:
            name = name[-1]
        else:
            name = name[-2]
        soup = self.make_soup(adres)
        soup = soup.find(itemprop="articleBody")
        if soup != None:
            text = soup.text
            text = self.clean_big_text(text)
            self.to_file(text, name)
            return soup

    def clean_big_text(self, text):
        text = text.replace("Previous Chapter", "").replace("Next Chapter", "")
        text = text.lstrip().rstrip()
        text = text.split("\r\n")
        texti = ""
        for t in text:
            if len(t) > len(texti):
                texti = t
        return texti.replace("\r\n", "\r\n\r\n")
