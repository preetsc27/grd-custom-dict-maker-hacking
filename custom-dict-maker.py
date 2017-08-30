import calendar
from random import randint
import threading
import sys
print("\n\n★·.·´¯`·.·★ GRD Dict Maker ★·.·´¯`·.·★\n\n"
      "Hello! My name is Coder Singh. This software is to make custom password dictionary by t"
      "aking the info about the person you want to hack. \n \n"
      "Please fill the necessary details if you do not know then leave it empty(press enter). \n"
      "『c』『o』『d』『e』『r』 『s』『i』『n』『g』『h』\n\n")

main_list = []

first_name = input("First Name: ")
main_list.append(first_name)

last_name = input("Last Name: ")
main_list.append(last_name)

birth_date = input("Birth date: ")
# birth_date = int(birth_date) if birth_date.isnumeric() else None
main_list.append(birth_date)

birth_month = input("Birth month(numeric): ")
# birth_month = int(birth_month) if birth_month.isnumeric() else None
main_list.append(birth_month)

birth_year = input("Birth year: ")
# birth_year = int(birth_year) if birth_year.isnumeric() else None
main_list.append(birth_year)

phone = input("Phone number: ")
# phone = int(phone) if phone.isnumeric() else None
main_list.append(phone)

pet_name = input("Pet name: ")
main_list.append(pet_name)

fav_number = input("Favourite number: ")
# fav_number = int(fav_number) if fav_number.isnumeric() else None
main_list.append(fav_number)

hints = input("Any other related words or numbers(please separate with comma ','): ")

print("\n\nProcessing........")

hints_list = hints.split(',')
main_list += hints_list

# print(main_list)

final_list = []


# ######## Letters to special chars FUNCTION
def lttr_to_special_chr(msg):
    output = []
    msg_ref = msg

    if msg is None:
        return

    for i in msg:
        if i == 'a':
            msg_ref = msg_ref.replace('a', '@')
            output.append(msg_ref)
            output.append(msg.replace('a', '@'))
        elif i == 'A':
            msg_ref = msg_ref.replace('A', '@')
            output.append(msg_ref)
            output.append(msg.replace('A', '@'))
        elif i == 's':
            msg_ref = msg_ref.replace('s', '$')
            output.append(msg_ref)
            output.append(msg.replace('s', '$'))

            # if s is &
            msg_ref = msg_ref.replace('s', '&')
            output.append(msg_ref)
            output.append(msg.replace('s', '&'))

        elif i == 'S':
            msg_ref = msg_ref.replace('s', '$')
            output.append(msg_ref)
            output.append(msg.replace('s', '$'))

            # if s is &
            msg_ref = msg_ref.replace('S', '&')
            output.append(msg_ref)
            output.append(msg.replace('S', '&'))

        elif i == 'i':
            msg_ref = msg_ref.replace('i', '!')
            output.append(msg_ref)
            output.append(msg.replace('i', '!'))

            # if i is 1
            msg_ref = msg_ref.replace('i', '1')
            output.append(msg_ref)
            output.append(msg.replace('i', '1'))

        elif i == 'I':
            msg_ref = msg_ref.replace('I', '!')
            output.append(msg_ref)
            output.append(msg.replace('I', '!'))

            # if i is 1
            msg_ref = msg_ref.replace('I', '1')
            output.append(msg_ref)
            output.append(msg.replace('I', '1'))

        elif i == 'e':
            msg_ref = msg_ref.replace('e', '3')
            output.append(msg_ref)
            output.append(msg.replace('e', '3'))

        elif i == 'E':
            msg_ref = msg_ref.replace('E', '3')
            output.append(msg_ref)
            output.append(msg.replace('E', '3'))

        elif i == 'o':
            msg_ref = msg_ref.replace('o', '0')
            output.append(msg_ref)
            output.append(msg.replace('o', '0'))

            # if o is *
            msg_ref = msg_ref.replace('o', '*')
            output.append(msg_ref)
            output.append(msg.replace('o', '*'))

        elif i == 'O':
            msg_ref = msg_ref.replace('O', '0')
            output.append(msg_ref)
            output.append(msg.replace('O', '0'))

            # if o is *
            msg_ref = msg_ref.replace('O', '*')
            output.append(msg_ref)
            output.append(msg.replace('O', '*'))

        elif i == 'p':
            msg_ref = msg_ref.replace('p', '9')
            output.append(msg_ref)
            output.append(msg.replace('p', '9'))

        elif i == 'P':
            msg_ref = msg_ref.replace('P', '9')
            output.append(msg_ref)
            output.append(msg.replace('P', '9'))

        return output


# ######## STRING COMBINATION FUNCTION
def str_combination(names, text):
    if names is None or names == '':
        return
    name_list = [names]
    # simple combinations
    for x in lttr_to_special_chr(names):
        main_list.append(x)
        name_list.append(x)

    # special combination for name and year like grd97 if birth year is 1997
    for name in name_list:
        for name_2 in name_form_change(name):
            comb = str(name_2) + str(birth_year)[2:]
            final_list.append(comb)

    # concating name with every other input
    for i in main_list:
        for name in name_list:
            for name_2 in name_form_change(name):
                simple_comb = str(name_2) + str(i)
                final_list.append(simple_comb)

    # now adding special chars
    special_char_list = list("`~!@#$%^&*()_+{}|:\"<>?/.\,;'[]'")

    for j in special_char_list:
        for i in main_list:
            for name in name_list:
                for name_2 in name_form_change(name):
                    simple_comb = str(name_2) + str(j) + str(i)
                    final_list.append(simple_comb)

    # for numbers like grd0123456789
    new_str = ""
    for i in range(0, 10):
        new_str += str(i)
        for name in name_list:
            for name_2 in name_form_change(name):
                comb = name_2 + str(i)
                final_list.append(comb)
                comb = name_2 + new_str
                final_list.append(comb)

                for j in special_char_list:
                    simple_comb = str(name_2) + str(j) + str(i)
                    final_list.append(simple_comb)

                    simple_comb = str(name_2) + str(j) + new_str
                    final_list.append(simple_comb)

    # for combinations like grd345, grd1234
    for i in range(0, 11):
        for j in range(0, 11):
            y = ""
            for x in range(i, j):
                y += str(x)
            for name in name_list:
                for name_2 in name_form_change(name):
                    comb = name_2 + y
                    final_list.append(comb)

                    for j in special_char_list:
                        comb = name_2 + j + y
                        final_list.append(comb)

    # for combinations like grd9876, grd987654
    new_str = ""
    for i in range(9, 0, -1):
        new_str += str(i)
        for name in name_list:
            for name_2 in name_form_change(name):
                comb = name_2 + str(i)
                final_list.append(comb)

                comb = name_2 + new_str
                final_list.append(comb)

                for j in special_char_list:
                    comb = name_2 + j + str(i)
                    final_list.append(comb)

                    comb = name_2 + j + new_str
                    final_list.append(comb)

    # for combinations like grd765, grd 876543
    for i in range(9, -1, -1):
        for j in range(9, 0, -1):
            y = ""
            for x in range(j, i, -1):
                y += str(x)
            for name in name_list:
                for name_2 in name_form_change(name):
                    comb = name_2 + y
                    final_list.append(comb)

                    for j in special_char_list:
                        comb = name_2 + j + y
                        final_list.append(comb)

    # combinations for name + number

    for i in range(50):
        sys.stdout.write('\r')
        sys.stdout.write(text+"[%-100s] %d%%" % ('=' * i, 2 * i))
        sys.stdout.flush()

        for name in name_list:
            for name_2 in name_form_change(name):
                comb = name_2 + str(i)
                if comb not in final_list:
                    final_list.append(comb)

                for j in special_char_list:
                    comb = name_2 + j + str(i)
                    if comb not in final_list:
                        final_list.append(comb)

    for x in range(25):
        # print(x)
        sys.stdout.write('\r')
        sys.stdout.write(text+"[%-20s] %d%%" % ('=' * x, 4 * x))
        sys.stdout.flush()
        i = randint(0, 10000000000)
        for name in name_list:
            for name_2 in name_form_change(name):
                comb = name_2 + str(i)
                if comb not in final_list:
                    final_list.append(comb)
                    final_list.append(i)

                for j in special_char_list:
                    comb = name_2 + j + str(i)
                    final_list.append(comb)


# ######## name upper and cap
def name_form_change(name):
    out = [name, name.upper(), name.capitalize()]
    return out


# ######## DATE COMBINATION FUNCTION
def date_combination(month):
    combination = str(birth_date) + month + str(birth_year)
    final_list.append(combination)
    combination = str(birth_date) + month.lower() + str(birth_year)
    final_list.append(combination)
    combination = str(birth_date) + month.upper() + str(birth_year)
    final_list.append(combination)
    combination = str(birth_date) + month.capitalize() + str(birth_year)
    final_list.append(combination)
    combination = str(birth_date) + month.upper() + str(birth_year)[2:]
    final_list.append(combination)

# ################# first name combinations ############### #
print("# ################# first name combinations ############### #")
# str_combination(first_name)
t1 = threading.Thread(target=str_combination, args=(first_name, "First Name:",))


# ################# last name combinations ############### #
print("# ################# last name combinations ############### #")
# str_combination(last_name)
t2 = threading.Thread(target=str_combination, args=(last_name, "Last Name:",))


# ################# date combinations ############### #
print("# ################# date combinations ############### #")
if birth_date is not None or birth_date != '' or birth_month is not None or birth_month != '' or birth_year is not None or birth_year != '':
    combination = str(birth_date) + str(birth_month) + str(birth_year)
    final_list.append(combination)
if birth_month is not None and birth_month != '' and birth_month:
    date_combination(calendar.month_name[int(birth_month)])
    date_combination(calendar.month_abbr[int(birth_month)])

# ################# phone number combinations ############### #
print("# ################# phone number combinations ############### #")
if phone is not None or phone != '':
    final_list.append(phone)


# ################# pet combinations ############### #
print("# ################# pet combinations ############### #")
# str_combination(pet_name)
t3 = threading.Thread(target=str_combination, args=(pet_name, "Pet Name:",))

# ################# fav number combinations ############### #
print("# ################# fav number combinations ############### #")
# str_combination(str(fav_number))
t4 = threading.Thread(target=str_combination, args=(str(fav_number), "Fav Number:",))


# ########## LAUNCHING THE THREADS
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()


# ################# other hints combinations ############### #
print("\n# ################# other hints combinations ############### #")
for i in hints_list:
    if i is not None:
        str_combination(str(i), "Other Hints:")

print("\nNumber of combinations made:", len(final_list))

file_name = input("Enter file name(extension not required): ")
if file_name == None or file_name == "":
    file_name = "custom-dict.txt"
file_name = file_name.strip(".txt")
file_name += '.txt'

file_open = open(file_name, "w")
for word in final_list:
    file_open.write(str(word)+"\n")

print("Done. Dhan  GRD. \nTotal number of combinations made:", len(final_list))
