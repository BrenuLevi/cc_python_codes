A=input().split()
B=[]

for index, value in enumerate(A) :
    A[index] = int(A[index])
    B.append(A[index])

A.sort()
print(f"{A[0]}\n{A[1]}\n{A[2]}\n\n{B[0]}\n{B[1]}\n{B[2]}")