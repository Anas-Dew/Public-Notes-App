from pip import main
from termcolor import cprint
from pyfiglet import *
from time import sleep


def navigate_app():
    f = open("C:\\Users\Public\data.secret", "w+")
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
    n_details = []
    sleep(0.6)
    while True:
        name = input("Create Username (8 Charecters): ")
        if len(name) != 8:
            raise ValueError
        password = input("Create PIN (3 Digits): ")
        if len(password) != 3:
            raise ValueError
        secretnote = input("MY NOTE (98 Charecters only) : ")
        n_details.append("NAME : "+name+", PASS : " +
                         password+", SECRET : "+secretnote)

        with open("C:\\Users\Public\data.secret", "a") as f:
            f.write(str(n_details))
            f.write("\n")
            f.close()
            break


def viewnotes():
    e_details = []
    sleep(0.6)
    name = input("Enter Username : ")
    password = str(input("Enter PIN : "))
    e_details.append("NAME : "+name+", PASS : "+password)

    with open("C:\\Users\Public\data.secret", "r") as f:
        read = f.readlines()
        for i in range(len(read)):
            readn = read[i][9:17]
            if readn == name:
                readp = read[i][26:29]
                if readp == password:
                    readed = read[i][40:138]
                    cprint('\nYOUR SECRET NOTE IS : ', 'blue')
                    cprint(readed, 'green')
                    break
                else:
                    pass
            else:
                pass


def modify():  # UNDER CONSTRUCTION ---------------------------------------------->>>>>>>>>>
    e_details = []
    name = input("Enter Username : ")
    password = str(input("Enter PIN : "))
    e_details.append("NAME : "+name+", PASS : "+password)

    with open("C:\\Users\Public\data.secret", "r") as f:
        read = f.readlines()
        for i in range(len(read)):
            readn = read[i][9:17]
            if readn == name:
                readp = read[i][26:29]
                if readp == password:
                    readed = read[i][40:138]

                    cprint('\nYOUR SECRET NOTE IS : ', 'blue')
                    cprint(readed, 'green')
                    cprint('ADD SOMETHING :', 'blue')

                    add_new = input()
                    e_details.append(
                        "NAME : "+name+", PASS : "+password + add_new)
                    with open("C:\\Users\Public\data.secret", "a") as a:
                        a.write(str(e_details))
                    break
                else:
                    pass

            else:
                pass


if __name__ == "__main__":
    title = 'PUBLIC   DIARY   NOTES'
    cprint(figlet_format(title, width=120), 'yellow')
    cprint('\t\t\t\tMOST UNSECURE NOTES APP EVER ;)', 'yellow')

    navigate_app()
