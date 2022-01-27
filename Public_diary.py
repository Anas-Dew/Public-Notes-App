from pickletools import read_long1
from cv2 import line
from pip import main
from termcolor import cprint
from pyfiglet import *
from time import sleep
from Clear_Screen_Func import clear


def navigate_app():

    f = open("C:\\Users\Public\data.secret", "a")
    print("CHOOSE NUMBERS TO NEVIGATE---")
    while True:
        sleep(0.5)
        cprint('\n0-CREATE NOTE\n1-VIEW NOTE\n2-EXIT', 'blue')
        user_choice = int(input())
        if user_choice == 0:
            addnotes()
        elif user_choice == 1:
            viewnotes()
        elif user_choice == 2:
            cprint('THANKS FOR USING MY LITTLE APP', 'green')
            exit(0)
        else:
            cprint('Enter a valid key', 'red')


def addnotes():
    clear()
    n_details = []
    sleep(0.6)
    while True:
        name = input("Create Username (8 Charecters): ")
        if len(name) != 8:
            cprint('Username isnot 8 Charecters long', 'red')
            navigate_app()
        with open("C:\\Users\Public\data.secret", "r") as f:
            read = f.readlines()

        for i in range(len(read)):
            readn = read[i][9:17]

            if name == readn:
                cprint('Username Already Exists !!!', 'red')
                sleep(0.7)
                navigate_app()
        password = input("Create PIN (3 Digits): ")
        if len(password) != 3:
            cprint('PIN isnot 3 Digits long', 'red')
            navigate_app()
        secretnote = input("MY NOTE (98 Charecters only) : ")
        n_details.append("NAME : "+name+", PASS : " +
                         password+", SECRET : "+secretnote)

        with open("C:\\Users\Public\data.secret", "a") as f:
            f.write(str(n_details))
            f.write("\n")
            f.close()
            cprint('\nNote successfully created.','green')
            break


def remove(string):
    return "".join(string.split())


def viewnotes():
    clear()
    e_details = []
    sleep(0.6)
    name = input("Enter Username : ")
    password = str(input("Enter PIN : "))

    with open("C:\\Users\Public\data.secret", "r") as f:
        read = f.readlines()

        for i in range(len(read)):

            readn = read[i][9:17]
            if readn == name:
                readp = read[i][26:29]
                if readp == password:
                    readed = read[i][40:138]
                    clear()

                    cprint('\nYOUR SECRET NOTE IS : ', 'blue')
                    cprint(readed, 'green')
                    
                    

                else:
                    pass
            else:
                pass


def modify():  # UNDER CONSTRUCTION ---------------------------------------------->>>>>>>>>>
    e_details = []
    name = input("Enter Username : ")
    password = str(input("Enter PIN : "))
    e_details.append("NAME : "+name+", PASS : "+password)
    
    cprint('\n1 - Add Something\n0 - Exit')
    usc = int(input())
    if usc == 1:
        with open("C:\\Users\Public\data.secret", "a") as mod:
            cprint('Write here : ', 'green')
            added_more = input()
            joinit = remove(readed)+added_more
            e_details.append('NAME : '+name+', PASS : ' +
                                             password+', SECRET : '+joinit)
            mod.writelines(str(e_details))
            mod.write("\n")
            mod.close()
            
    elif usc == 0:
        navigate_app()
    



if __name__ == "__main__":
    title = 'PUBLIC   DIARY   NOTES'
    cprint(figlet_format(title, width=120), 'yellow')
    cprint('\t\t\t\tMOST UNSECURE NOTES APP EVER ;)', 'yellow')

    navigate_app()
