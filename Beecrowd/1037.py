'''resolução aceita pelo BeeCrowd'''
x = float(input())
if 0<= x <= 25:
    print('Intervalo [0,25]')
if 25< x <= 50:
    print('Intervalo (25,50]')
if 50< x <= 75:
    print('Intervalo (50,75]')
if 75< x <= 100:
    print('Intervalo (75,100]')
if x >100 or x<0:
    print('Fora de intervalo')

'''resoluçãp alternativa

input_data = float(input())

if input_data >= 0 and input_data <= 25:
    print("Intervalo [0,25]")  

elif input_data > 25 and input_data <= 50:
    print("intervalo [25,50]")

elif input_data > 50 and input_data <=75:
    print("intervalo [50,75]")

elif input_data >75 and input_data <=100:
    print("intervalo [75, 100]")

else:
    print("Fora de Intervalo")

'''
