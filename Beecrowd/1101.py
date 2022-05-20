
soma = 0
j=0
while j != 1:
    M,N = input().split(" ")
    M = int(M)
    N = int(N)
    soma = 0
    if M > N:
        aux = M
        M = N
        N = aux
    if M<=0 or N<=0:
        j = 1
    if j!=1:
        for i in range(M,N+1):
            print('%d '%(i),end="")
            soma+=i
            if i == N:
                print('Sum=%d'%(soma))
'''
alternativo não funcional

m, n = map(int, input().split())
a = m if m > n else n #maior
b = n if n < m else m #menor

for x in range (b, a+1):
    if a <= 0 or b <= 0:
        break
    else:
        lista1 =[]
        for i in range(b, a+1):
            lista1.append(i)
            soma = sum(lista1)
for y in lista1:
    print(f"{y}", end=" ")
print(f"sum = {soma}")

Em análise!!!!
'''
