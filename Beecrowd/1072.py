inn = 0
out = 0
n = int(input())#quatidade de valores que serão digitados
lista = []
for num in range(n):
    x = int(input())
    lista.append(x)
    if x >= 10 and x <= 20:
        inn +=1
    else:
        out+=1
print(f'{inn} in\n{out} out')
