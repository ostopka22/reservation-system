def option_E():
    reservation_number = input("Enter the reservation number: ")
    new_time = input("Enter the new time: ")

    file1 = open("/Users/oliviastopka/Desktop/reservationsystem/reservation.txt", "r")
    lines = file1.readlines()
    file1.close()
    file2 = open("reservation.txt", "w")

    for line in lines:
        if not line.startswith(reservation_number):
            file2.write(line)
        else:
            line_list = line.strip().split("\t\t\t")
            name = line_list[1]
            date = line_list[2]
            num_adults = line_list[4]
            num_children = line_list[5]

            new_line_to_add = "{}\t\t\t{:>10}\t\t\t{:>10}\t\t\t{:>10}\t\t\t{:>10}\t\t\t{:>10}\n".format(
                reservation_number, name, date, new_time, num_adults, num_children)

            file2.write(new_line_to_add)
