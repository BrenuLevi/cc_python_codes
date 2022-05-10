A,B=map(int,input().split())

if A>B:
    print(f"O JOGO DUROU {24-(A-B)} HORA(S)")
elif B>A:
    print(f"O JOGO DUROU {abs(A-B)} HORA(S)")
elif B==A:
    print(f"O JOGO DUROU 24 HORA(S)")