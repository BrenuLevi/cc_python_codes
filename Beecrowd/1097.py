i = 1
j = 7

while i != 9:
    for i in range(1, 10, 2):
        if i == 1:
            for j in range(7, 4, -1):
                print(f"I={i} J={j}")
        elif i == 3:
            for j in range (9, 6, -1):
                print(f"I={i} J={j}")
        elif i == 5:
            for j in range (11, 8, -1):
                print(f"I={i} J={j}")
        elif i == 7:
            for j in range (13, 10, -1):
                print(f"I={i} J={j}")
        elif i == 9:
            for j in range (15, 12, -1):
                print(f"I={i} J={j}")
