def Input():
    data = open('file.txt', 'a')
    first_name = input("Введите имя: ")
    second_name = input("Введите фамилию: ")
    mid_name = input("Введите отчество: ")
    number = input("Введите номер телефона")
    item = [first_name, second_name, mid_name, number]
    s = ' '
    data.writelines(s.join(item) + '\n')
    data.close()
  