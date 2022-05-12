a = []
for i in range(5):
    n = int(input())
    a.append(int(n))

l = 0
m = 0
o = 0
p = 0
for j in range(5):
    if a[j] % 2 == 0:
        l += 1
    if a[j] % 2 == 1:
        m += 1
    if a[j] > 0:
        o += 1
    if a[j] < 0:
        p += 1
print(l, "valor(es) par(es)")
print(m, "valor(es) impar(es)")
print(o, "valor(es) positivo(s)")
print(p, "valor(es) negativo(s)")


'''
par = 0
imp = 0
pos = 0
neg = 0
x = input().split()
lista = [int(n) for n in x]

for n in lista:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    
    if n % 2 == 0:
        par += 1
    else:
        imp += 1
print(f"{par} valor(es) par(es)\n{imp} valor(es) impar(es)\n{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)")
'''
