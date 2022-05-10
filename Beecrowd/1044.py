x = input().split()
a, b  = map(int, x)

if a%b == 0 or b%a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
