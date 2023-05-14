# I am using the pseudo-Sudoku algorithm to solve this question.
# One can go through the cross hatching algorithm to understand my approach
# https://sudokugarden.de/en/solve/crosshatching
A = []
B = []
M = 0
N = 0 
C = []
# input_value() - just takes input from the user as per the specified format
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
# print(A) check if the input has been stored correctly
# print(B)
# skillreqmat() - giving values to a 3-dimensional matrix C, whose rows (i) signify a particular project and columns(j) contain 1D array containg the list of all persons eligible for the jth role in the ith project
# if a role is not required in a project , the corresponding position in matrix C is set to -1
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
# manipulation1() - if the length of the list at C[i][j] is zero, this means that there is no person suitable for that role => project i cannot be completed => clear the ith row from C
# 59 -73 => if a person is eligible for jth role in ith project as a mentee , he must have a mentor in ith project in the remaining j' roles. If we cannot find a mentor for the jth role from among the j' roles in the ith project , we need to remove that person from the list at C[i][j].
# 73-76 => suppose we found only one mentor for a person in jth role at (j+1)th role, but that person was himself a mentee for the (j+1)th role for whom we could not find a mentor,so we had to remove that person from the list at C[i][j+1]. Since that person was the mentor for the jth role,we'll have to recheck the ith row until no changes are made. 
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
# 82-92 => define a 2-Dimensional matrix PerReq with (i,j)th element as the number of projects in which the ith person is eligible for jth role
# 93 - 101 => define a 2-Dimensional matrix E with (i,j)th element as the number of persons which are eligible for the jth role in ith project. If ith project cannot be completed, then ith row is an empty list
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

