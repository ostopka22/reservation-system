from optionB import *
from optionC import *
from optionD import *
from optionE import *


class reservation:
    def __init__(self, choice):
        self.choice = choice
        if choice == "A":
            count = 0
            file = open("/Users/oliviastopka/Desktop/reservationsystem/reservation.txt")
            lines = file.readlines()[1:]
            file.close()
            for line in lines:
                count += 1

            if count == 0:
                print("No reservations found")
                print()
            else:
                file = open("/Users/oliviastopka/Desktop/reservationsystem/reservation.txt", "r")
                print(file.read())
                file.close()

        elif choice == "B":
            option_B()

        elif choice == "C":
            option_C()

        elif choice == 'D':
            option_D()

        elif choice == 'E':
            option_E()

        elif choice == "F":
          import sys
          sys.exit("Goodbye,have a nice day!")

        else:
            print("Invalid, Try again")


while True:
    try:
        file = open("/Users/oliviastopka/Desktop/reservationsystem/reservation.txt", "r")
    except FileNotFoundError:
        file = open("/Users/oliviastopka/Desktop/reservationsystem/reservation.txt", "w+")
        file.write("#\t\t\tName\t\t\t        Date\t\t\t        Time\t\t\t    Adults\t\t\tChildren\n")
    file.close()

    print("        TATRA HAUS RESERVATION")
    print("Please choose an option from the menu")
    print("A. View all Reservations")
    print("B. Make Reservation")
    print("C. Delete Reservation ")
    print("D. Change Reservation Amount")
    print("E. Change Reservation Time")
    print("F. Exit the system\n")

    selection_menu = input('Please enter a option: ').upper()
    reservation(selection_menu)
