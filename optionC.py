def option_C():
    reservationNum = input("Enter the reservation number: ")
    file1 = open("/Users/oliviastopka/Desktop/reservationsystem/reservation.txt", "r")
    lines = file1.readlines()
    file1.close()
    file2 = open("reservation.txt", "w")

    for line in lines:
        if not line.startswith(reservationNum):
            file2.write(line)
    file2.close()
