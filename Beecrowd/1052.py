x = int(input())

if x >= 0 and x <= 12:
    if x == 1:
        print("January")
    elif x ==2:
        print("February")
    elif x == 3:
        print("March")
    elif x == 4:
        print("April")
    elif x == 5:
        print("May")
    elif x == 6:
        print("June")
    elif x == 7:
        print("July")
    elif x == 8:
        print("August")
    elif x == 9:
        print("September")
    elif x == 10:
        print("October")
    elif x == 11:
        print("November")
    elif x == 12:
        print("December")


'''alternativo
x = int(input("Digite um valor inteiro entre 1 e 12\n"))
month = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if x > 0 and x < 13:
    if x == 1:
        print(month[0])
    if x == 2:
        print(month[1])
    if x == 3:
        print(month[2])
    if x == 4:
        print(month[3])
    if x == 5:
        print(month[4])
    if x == 6:
        print(month[5])
    if x == 7:
        print(month[6])
    if x == 8:
        print(month[7])
    if x == 9:
        print(month[8])
    if x == 10:
        print(month[9])
    if x == 11:
        print(month[10])
    if x == 12:
        print(month[11])
else:
    print("Digite um valor inteiro entre 1 e 12\nEncerrando...\nEncerrado")
'''    
