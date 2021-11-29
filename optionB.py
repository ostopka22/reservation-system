def option_B():
    with open("/Users/oliviastopka/Desktop/reservationsystem/reservation.txt", "r") as file:
        for last_line in file:
            pass

    if last_line[0] == "#":
        num = 1
    else:
        num = int(last_line[0]) + 1

    name = input("Enter Name: ")
    date = input("Enter Date: ")
    time = input("Enter Time: ")
    adults = int(input("Amount of Adults: "))
    children = int(input("Amount of Children: "))
    file = open("reservation.txt", "a")
    file.write(f"{num}\t\t\t{name:>10}\t\t\t{date:>10}\t\t\t{time:>10}\t\t\t{adults:>10}\t\t\t{children:>10}\n")
    file.close()
    print()
