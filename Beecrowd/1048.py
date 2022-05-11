x = float(input())

if x >= 0 and x <= 400:
    percent = 15
    rpercent = (percent/100)
    r = rpercent*x
    newX = r+x
    print(f"Novo salario: {newX:.2f}\nReajuste ganho: {r:.2f}\nEm percentual: {percent} %")
elif x > 400 and x <= 800:
    #reajustar 12%
    percent = 12
    rpercent = (percent/100)
    r = rpercent*x
    newX = r+x
    print(f"Novo salario: {newX:.2f}\nReajuste ganho: {r:.2f}\nEm percentual: {percent} %")
elif x > 800 and x <= 1200:
    #reajustar 10%
    percent = 10
    rpercent = (percent/100)
    r = rpercent*x
    newX = r+x
    print(f"Novo salario: {newX:.2f}\nReajuste ganho: {r:.2f}\nEm percentual: {percent} %")
elif x > 1200 and x <= 2000:
    #reajustar 7%
    percent = 7
    rpercent = (percent/100)
    r = rpercent*x
    newX = r+x
    print(f"Novo salario: {newX:.2f}\nReajuste ganho: {r:.2f}\nEm percentual: {percent} %")
elif x > 2000:
    percent = 4
    rpercent = (percent/100)
    r = rpercent*x
    newX = r+x
    print(f"Novo salario: {newX:.2f}\nReajuste ganho: {r:.2f}\nEm percentual: {percent} %")
