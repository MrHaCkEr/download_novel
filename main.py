from wuxiaworld import Wuxiaworld
from Abstract_Class import Logic

def main():
    webs = ["Wuxiaworld"]
    if len(webs)>1:
        Logic.show_list_in_console(webs)
        number_web=Logic.which_number("give mi number",len(webs))

    else:
        web=Wuxiaworld()
        web.start_app()


main()