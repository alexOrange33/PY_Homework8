def Change(data):
    spisok = []
    with open("file.txt", "r",encoding = 'utf-8') as file:
        for line in file:
            spisok.append(line)
    lis =[]
    res = int(input("Что хотите изменить? \n1-Имя\n2-Фамилию\n3-Отчество\n4-Номер телефона\n"))
    match res:
        case 1:
            temp = input("Новое имя: ")
        case 2:
            temp = input("Новая Фамилия: ")
        case 3:
            temp = input("Новое Отчество: ")
        case 4:
            temp = input("Новый номер телефона: ")
    for i in range(len(spisok)-1):
        if data == spisok[i]:
            lis = spisok[i].split()
            lis[res-1]=temp
            spisok[i] =" ".join(lis)+'\n'         
    with open("file.txt", "w",encoding = 'utf-8') as file:
        for i in spisok:
            file.write(i)