from math import pow

L=input().split()
for index,value in enumerate(L):
    L[index]=float(L[index])
L.sort()
A=L[len(L)-1]
B=L[0]
C=L[1]

if A>=B+C :
    print("NAO FORMA TRIANGULO")
elif pow(A,2)==pow(B,2)+pow(C,2) :
    print("TRIANGULO RETANGULO")
elif pow(A,2)>pow(B,2)+pow(C,2) :
    print("TRIANGULO OBTUSANGULO")
elif pow(A,2)<pow(B,2)+pow(C,2) :
    print("TRIANGULO ACUTANGULO")

if A==B and B==C and C==A :
    print("TRIANGULO EQUILATERO")
elif L.count(A)>1 or L.count(B)>1 :
    print("TRIANGULO ISOSCELES")