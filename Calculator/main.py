from User import User

class main():

    play = "Y"

    while play != "N":
        u = User()
        u.run_user()
        play = input("Do you want to continue? Y/N : ").upper()

        if play == "N":
            break

#start project