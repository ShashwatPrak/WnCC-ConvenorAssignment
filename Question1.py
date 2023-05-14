# I am using the pseudo-Sudoku algorithm to solve this question.
# One can go through the cross hatching algorithm to understand my approach
# https://sudokugarden.de/en/solve/crosshatching
A = []
B = []
M = 0
N = 0 
C = []
def input_value():
    N = int(input("Enter the number of persons "))
    print("\nEnter the details of each person \n")
    for i in range(0,N):
        ele = input().split()
        A.append(ele)
    M = int(input("Enter the number of projects "))
    print("\nEnter the skill requirement of each project \n")
    for i in range(0,M):
        ele = input().split()
        B.append(ele)
    for i in range(0,N):
        for j in range(1,6):
            A[i][j] = int(A[i][j])
    for i in range(0,M):
        for j in range(1,6):
            B[i][j] = int(B[i][j])
input_value()
print(A)
print(B)
def skillreqmat():
    for i in range(0,M):
        C.append([])
        for j in range(1,6):
            C[i].append([])
    for i in range(0,M):
        for j in range(1,6):
            if(B[i][j]== 0 ):
                C[i][j-1] = -1
                continue
            C[i][j-1] = []
            for k in range(0,N):
                if( B[i][j] - 1 <= A[k][j]):
                    C[i][j-1].append(k)
skillreqmat()
def manipulation1():
    for i in range(0,len(C)):
        for j in range(0,5):
            if(len(C[i][j])==0):
                C[i].clear()
                break
    for i in range(0,M):
        if(len(C[i])==0):
            continue
        flag = 0
        for j in range(0,5):
            k = 0
            while k<len(C[i][j]):
                if(A[C[i][j][k]][j+1]<B[i][j+1]):
                    K = 0 
                    for a in range(0,5):
                        if(a==j):
                            continue
                        for b in range(0,len(C[i][a])):
                            if(A[C[i][a][b]][j+1]>B[i][j+1]):
                                K= K+1
                    if(K==0):
                        C[i][j].remove(C[i][j][k])
                        flag = 1
                k = k+1
        if(flag == 1):
            i=i-1
manipulation1()
PerReq = []
E = []
def calculations():
    for i in range(0,N):
        PerReq.append([])
        for j in range(0,5):
            count = 0
            for k in range(0,M):
                if(len(C[k])==0):
                    continue
                if i in C[k][j]:
                    count = count + 1
            PerReq[i].append(count)
    for i in range(0,M):
        E.append([])
        if(len(C[i])==0):
            continue
        for j in range(0,5):
            if(not(isinstance(C[i][j],int))):
                E[i].append(len(C[i][j]))
            else:
                E[i].append(-5)

