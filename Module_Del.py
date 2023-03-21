def Del_line(data):
    spisok = []
    with open("file.txt", "r",encoding = 'utf-8') as file:
        for line in file:
            spisok.append(line)
        for i in range(len(spisok)-1):
            if data == spisok[i]:
                spisok.pop(i)
    with open("file.txt", "w",encoding = 'utf-8') as file:
        for i in spisok:
            file.write(i)
   


                

