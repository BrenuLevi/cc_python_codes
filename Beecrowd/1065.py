a = []
for i in range(5):
    n = int(input())
    a.append(int(n))

l = 0
for j in range(5):
    if a[j] % 2 == 0:
        l += 1
print(l, "valores pares")



'''

i = 0
x = input().split()
lista = [int(n) for n in x]
for n in lista:
    if n%2 == 0:
        i+=1
print(f"{i} valores pares")

'''
