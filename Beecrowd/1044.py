x = input().split()
a, b, c = map(float, x)

if a > abs(b-c) and a < b+c : # verifica se o triangulo é possivel
    peri = a+b+c
    print(f"Perimetro = {peri}")
else:
    area = ((a + b)*c)/2
    print(f"Area = {area}")
