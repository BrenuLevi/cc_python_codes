i = 0
x = int(input())
lista = []
while i < 6:
    if x % 2 != 0:
        i+=1
        lista.append(x)
    x+=1
for x in lista:
    print(x)
