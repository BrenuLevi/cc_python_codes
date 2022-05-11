x = input()
y = input()
z = input()

if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    print('aguia')

elif x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    print('pomba')

elif x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    print('homem')

elif x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    print('vaca')
elif x == 'invertebrado' and y == 'inseto' and z == 'hematofago':
    print('pulga')

elif x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    print('lagarta')

elif x == 'invertebrado' and y == 'anelideo' and z == 'hematofago':
    print('sanguessuga')

elif x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    print('minhoca')


'''
acredito que a resolução é possível utilizando arrays, mas não consegui desenvolver dessa forma, abaixo o código que tentei utilizar

a = input().lower()
b = input().lower()
c = input().lower()

x = ['vertebrado', 'invertebrado']
y = ['ave', 'mamifero', 'inseto', 'anelideo']
z = ['carnivoro', 'onivoro', 'herbivoro', 'hematofago']

if x[0] and b == y[0] and c == [0]:
    print("aguia")
elif x[0] and b == y[0] and c == [1]:
    print("pomba")
elif x[0] and b == y[1] and c == [0]:
    print("homem")
elif x[0] and b == y[1] and c == [1]:
    print("vaca")
elif x[1] and b == y[0] and c == [0]:
    print("pulga")
elif x[1] and b == y[0] and c == [1]:
    print("lagarta")
elif x[1] and b == y[1] and c == [0]:
    print("sanguessuga")
elif x[1] and b == y[1] and c == [1]:
    print("minhoca")
'''
