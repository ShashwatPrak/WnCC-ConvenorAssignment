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
    global M
    global N
    N = int(input())
    for i in range(0,N):
        ele = input().split()
        A.append(ele)
    M = int(input())
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
# restore() - the 1-D array at (i,j)th position in C contains the list of all persons eligible for jth role in ith project.
# If length of this array is 0, this project i cannot be completed as there is no one eligible for jth role. We delete ith row from C
# before deleting the ith row, we restore back the persons allocated to various roles of ith project, and add them back to their respective places in matrix C
def restore(list1):
    restoredarray = []
    for i in range(0,5):
        if(isinstance(list1[i],int)):
            if(not(list1[i]==-1)):
                restoredarray.append(list1[i])
    for i in restoredarray:
        for j in range(0,M):
            if(len(C[j])==0):
                continue
            for k in range(0,5):
                if(B[j][k+1]-1 <= A[i][k+1]):
                    if(not(isinstance(C[j][k],int))):
                        C[j][k].append(i)
                        C[j][k].sort()
                    else:
                        if(not(C[j][k]==-1)):
                            C[j][k]=[C[j][k],i]
                            C[j][k].sort()
# manipulation1() - if the length of the list at C[i][j] is zero, this means that there is no person suitable for that role => project i cannot be completed => clear the ith row from C
# 85 -103 => if a person is eligible for jth role in ith project as a mentee , he must have a mentor in ith project in the remaining j' roles. If we cannot find a mentor for the jth role from among the j' roles in the ith project , we need to remove that person from the list at C[i][j].
# 103- 106 => suppose we found only one mentor for a person in jth role at (j+1)th role, but that person was himself a mentee for the (j+1)th role for whom we could not find a mentor,so we had to remove that person from the list at C[i][j+1]. Since that person was the mentor for the jth role,we'll have to recheck the ith row until no changes are made. 
def manipulation1():
    for i in range(0,len(C)):
        if(len(C[i])==0):
            continue
        for j in range(0,5):
            if(isinstance(C[i][j],int)):
                continue
            if(len(C[i][j])==0):
                restore(C[i])
                C[i].clear()
                break
    for i in range(0,M):
        if(len(C[i])==0):
            continue
        flag = 0
        for j in range(0,5):
            k=0
            if(isinstance(C[i][j],int)):
                continue
            while k<len(C[i][j]):
                if(A[C[i][j][k]][j+1]<B[i][j+1]):
                    K = 0 
                    for a in range(0,5):
                        if(a==j):
                            continue
                        if(isinstance(C[i][a],int)):
                            continue
                        for b in range(0,len(C[i][a])):
                            if(A[C[i][a][b]][j+1]>B[i][j+1]):
                                K=K+1
                    if(K==0):
                        C[i][j].remove(C[i][j][k])
                        flag = 1
                k = k+1
        if(flag == 1):
            i=i-1
PerReq = []
E = []
# 111-122 => define a 2-Dimensional matrix PerReq with (i,j)th element as the number of projects in which the ith person is eligible for jth role
# 123 - 131 => define a 2-Dimensional matrix E with (i,j)th element as the number of persons which are eligible for the jth role in ith project. If ith project cannot be completed, then ith row is an empty list
def calculations():
    for i in range(0,N):
        PerReq.append([])
        for j in range(0,5):
            count = 0
            for k in range(0,M):
                if(len(C[k])==0):
                    continue
                if((isinstance(C[k][j],int))):
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
# sortSeconds() - used in sorting a 2-D list according to the value of 2nd index
def sortSeconds(val):
    return val[2]
# calculations2() => 
# 139 - 143 - define a list freq_PerReq with ith element as the number of vacancies for which the ith person is eligible
# 144 - 158 - finding the minimum element in E (role for which least number of persons are eligible) and adding the locations of C which have minimum number of elements to minEreqarray
# 159 - 165 - adding the number of roles filled in minEreqarray[i][0]th project to minEreq[i][2] and sorting the minEreqarray as per the [i][2] values
# 168 -172 - comparing the persons in C[minEreqarray[0][0]][minEreqarray[0][1] according to the number of roles they are eligible for and returning the person with least number of roles available
def calculations2():
    freq_PerReq = []
    for i in range(0,N):
        freq_PerReq.append(0)
        for ele in PerReq[i]:
            freq_PerReq[i] += ele
    minEreq = N
    for i in range(0,M):
        if(len(E[i])==0):
            continue
        for j in range(0,5):
            if(E[i][j]<minEreq and E[i][j]>0):
                minEreq=E[i][j]
    minEreqarray = []
    for i in range(0,M):
        if(len(E[i])==0):
            continue
        for j in range(0,len(E[i])):
            if(minEreq==E[i][j]):
                minEreqarray.append([i,j]) 
    for i in range(0, len(minEreqarray)):
        minEreqarray[i].append(0)
        for j in range(0,5):
            if(E[minEreqarray[i][0]][j]==-5):
                minEreqarray[i][2] += 1
    minEreqarray.sort(key =sortSeconds, reverse = True)
    evaluate=0 
    evalcriteria = 5*M
    for i in range(0,len(C[minEreqarray[0][0]][minEreqarray[0][1]])):
        if(freq_PerReq[C[minEreqarray[0][0]][minEreqarray[0][1]][i]]<evalcriteria):
            evaluate = C[minEreqarray[0][0]][minEreqarray[0][1]][i]
            evalcriteria = freq_PerReq[C[minEreqarray[0][0]][minEreqarray[0][1]][i]]
    return [minEreqarray[0][0],minEreqarray[0][1],evaluate]
# defmanipulations2() => adds the person given by calculations2() to respective site in C and erases its value from other locations of C
def manipulations2():
    m2 = calculations2()
    C[m2[0]][m2[1]] = m2[2]
    for i in range(0,M):
        if(len(C[i])==0):
            continue
        for j in range(0,5):
            if(not(isinstance(C[i][j],int))):
                if m2[2] in C[i][j]:
                    C[i][j].remove(m2[2])
def main():
    while True:
        manipulation1()
        calculations()
        flag = True
        for i in range(0,M):
            if(len(E[i])==0):
                continue
            for j in range(0,5):
                if(not(E[i][j]==-5)):
                    flag = False
                    break
        if(flag == True):
            break
        manipulations2()
        PerReq.clear()
        E.clear()
    Project_count = M
    for i in range(0,M):
        if(len(E[i])==0):
            Project_count -=1
    print(Project_count)
main()



