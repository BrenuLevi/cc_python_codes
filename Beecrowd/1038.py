'''resolução aceita pelo BeeCrowd'''
x = input().split()
a, b = x
if a == '1':
    print("Total: R$ {:.2f}".format(4.00 * int(b)))
if a == '2':
    print("Total: R$ {:.2f}".format(4.50 * int(b)))
if a == '3':
    print("Total: R$ {:.2f}".format(5.00 * int(b)))
if a == '4':
    print("Total: R$ {:.2f}".format(2.00 * int(b)))
if a == '5':
 print("Total: R$ {:.2f}".format(1.50 * int(b)))

 '''resolução alternativa
 cod_qtd = input().split()
cod, qtd = cod_qtd
if cod == '1':
    print("Total: R$ {:.2f}".format(4.00 * int(qtd)))
if cod == '2':
    print("Total: R$ {:.2f}".format(4.50 * int(qtd)))
if cod == '3':
    print("Total: R$ {:.2f}".format(5.00 * int(qtd)))
if cod == '4':
    print("Total: R$ {:.2f}".format(2.00 * int(qtd)))
if cod == '5':
 print("Total: R$ {:.2f}".format(1.50 * int(qtd)))
 '''
