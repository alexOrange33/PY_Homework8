def OutputAll():
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)

def Search(data):
    with open('file.txt', 'r', encoding='utf-8') as file:
        flag = True
        for line in file:
            if data in line:
                print(line)
                flag = False
        if flag:
            print("не найдено")