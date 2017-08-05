from Abstract_Class import Logic
from qidian import Qidian
from wuxiaworld import Wuxiaworld


def main():
    webs = ["Wuxiaworld", "Qidian"]
    Logic.show_list_in_console(webs)
    number_web = Logic.which_number(len(webs))

    if webs[number_web] == "Wuxiaworld":
        Wuxiaworld().start_app()

    elif webs[number_web] == "Qidian":
        Qidian().start_app()






    else:
        web=Wuxiaworld()
        web.start_app()


main()