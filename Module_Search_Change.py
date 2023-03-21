def Search(data):
    with open('file.txt', 'r+', encoding='utf-8') as file:
        flag = True
        for line in file:
            if data in line:
                print(line)
                flag = False
                change = int(input("Введите номер команды: \n1-Удалить запись\n2-Изменить запись\n3-Выход\n"))
                match change:
                    case 1:
                        from Module_Del import Del_line
                        Del_line(line)
                    case 2:
                        from Module_Change import Change
                        Change(line)
                    case 3:
                        break

                             
        if flag:
            print("не найдено")