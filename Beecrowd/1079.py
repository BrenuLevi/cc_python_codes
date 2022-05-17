n  = int(input())
lista =[]
for x in range(n):
    i = list(map(float, input().split()))
    med =((i[0]*2) + (i[1]*3) + (i[2]*5))/10
    lista.append(med)
for media in lista:
    print(f"{media:.1f}")
