def subset(A, B):
    n = len(A)
    L= ([[None for i in range(B+1)]
         for i in range(n+1)])
    

    for i in range(n+1):
        L[i][0] = True

    for j in range(B+1):
        L[0][j] = False 

    for i in range(1, n+1):
        for j in range(1, B+1):
            if j- A[i-1]<0:
                L[i][j] = L[i-1][j]
            else:
                L[i-1][j] or L[i-1][j-A[i-1]] 
    if L[n][B]:
        m=n
        b=B 
        s=set()

        while b>0:
            if L[m][b]:
                m = m-1
        
            else:
                m=m-1
                s.add(A[m])
                b=b-A[m]

    return L[n][B]