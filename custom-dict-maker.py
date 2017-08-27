import calendar

print("★·.·´¯`·.·★ GRD Dict Maker ★·.·´¯`·.·★\n"
      "Hello! My name is Coder Singh. This software is to make custom password dictionary by t"
      "aking the info about the person you want to hack. \n \n"
      "Please fill the necessary details if you do not know then leave it empty(press enter). \n"
      "『c』『o』『d』『e』『r』 『s』『i』『n』『g』『h』")

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
def str_combination(names):
    if names is None or names == '':
        return
    name_list = [names]
    # simple combinations
    for x in lttr_to_special_chr(names):
        main_list.append(x)
        name_list.append(x)

    for i in main_list:
        for name in name_list:
            simple_comb = str(name) + str(i)
            final_list.append(simple_comb)
            simple_comb = str(name).capitalize() + str(i)
            final_list.append(simple_comb)
            simple_comb = str(name).upper() + str(i)
            final_list.append(simple_comb)

    # now adding special chars
    special_char_list = list("`~!@#$%^&*()_+{}|:\"<>?/.\,;'[]'")

    for j in special_char_list:
        for i in main_list:
            for name in name_list:
                simple_comb = str(name) + str(j) + str(i)
                final_list.append(simple_comb)
                simple_comb = str(name).capitalize() + str(j) + str(i)
                final_list.append(simple_comb)
                simple_comb = str(name).upper() + str(j) + str(i)
                final_list.append(simple_comb)


# ######## DATE COMBINATION FUNCTION
def date_combination(month):
    combination = str(birth_date) + month + str(birth_year)
    final_list.append(combination)
    combination = str(birth_date) + month.lower() + str(birth_year)
    final_list.append(combination)
    combination = str(birth_date) + month.upper() + str(birth_year)
    final_list.append(combination)

# ################# first name combinations ############### #
str_combination(first_name)



# ################# last name combinations ############### #
str_combination(last_name)


# ################# date combinations ############### #
if birth_date is not None or birth_date != '' or birth_month is not None or birth_month != '' or birth_year is not None or birth_year != '':
    combination = str(birth_date) + str(birth_month) + str(birth_year)
    final_list.append(combination)
if birth_month is not None and birth_month != '' and birth_month:
    date_combination(calendar.month_name[int(birth_month)])
    date_combination(calendar.month_abbr[int(birth_month)])

# ################# phone number combinations ############### #
if phone is not None or phone != '':
    final_list.append(phone)


# ################# pet combinations ############### #
str_combination(pet_name)


# ################# fav number combinations ############### #
str_combination(str(fav_number))

# ################# other hints combinations ############### #
for i in hints_list:
    if i is not None:
        str_combination(str(i))

file_name = input("Enter file name(extension not required): ")
first_name = file_name.strip(".txt")
file_name += '.txt'

file_open = open(file_name, "w")
for word in final_list:
    file_open.write(word+"\n")

print("Done. Dhan  GRD. ")