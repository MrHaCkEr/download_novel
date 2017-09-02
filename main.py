from main_Classes import Logic
from main_Classes import ToFile
from qidian import Qidian
from wuxiaworld import Wuxiaworld


def main():
    webs = ["Wuxiaworld", "Qidian"]
    Logic.show_list_in_console(webs)
    number_web = Logic.which_number(len(webs))

    Logic.show_list_in_console(ToFile.FORMAT_FILE)
    format = ToFile.FORMAT_FILE[Logic.which_number(len(ToFile.FORMAT_FILE))]

    if webs[number_web] == "Wuxiaworld":
        Wuxiaworld(format).start_app()

    elif webs[number_web] == "Qidian":
        Qidian(format).start_app()


main()
