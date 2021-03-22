##ALMOST DEBUGGED
def subtract(X, Y):
    result = [[0 for i in range(len(X))] for j in range(len(X))]

    for i in range(len(X)):
        for j in range(len(X)):
            result[i][j] = X[i][j] - Y[i][j]

    return result

def add(X, Y):
    result = [[0 for i in range(len(X))] for j in range(len(X))]

    for i in range(len(X)):
        for j in range(len(X)):
            result[i][j] = X[i][j] + Y[i][j]

    return result

def padding(A):
    for i in range(0, len(A)):
        A[i] = A[i] + [0]
  
    final_row = [0] * (len(A)+1)
    A.insert(len(A), [0] * (len(A)+1)) 


def strassen(A, B):
    if len(A[0]) == 1:
        print (len([A[0][0] * B[0][0]]))
        return [A[0][0] * B[0][0]]

    if len(A) % 2 != 0:
        padding(A)
        padding(B)

    half = int(len(A)/2)

    a = [A[0][:half] for i in range(half)]
    e = [B[0][:half] for i in range(half)]
    b = [A[i][half:] for i in range(half)]      
    f = [B[i][half:] for i in range(half)]      
   
    c = [A[i][:half] for i in range(half, len(A))]      
    g = [B[i][:half] for i in range(half, len(B))]      

    d = [A[i][half:] for i in range(half, len(A))]      
    h = [B[i][half:] for i in range(half, len(B))] 
        

    P1 = strassen(a, subtract(f,h))   
    P2 = strassen(add(a,b), h)         
    P3 = strassen(add(c,d), e)         
    P4 = strassen(d, subtract(g,e))         
    P5 = strassen(add(a,d), add(e,h))         
    P6 = strassen(subtract(b, d), add(g,h))   
    P7 = strassen(subtract(a,c), add(e,f)) 

    # do the necessary additions 
    c11 = add(subtract(add(P5,P4), P2),P6)   
    c12 = add(P1,P2)            
    c21 = add(P3,P4)          
    c22 = subtract(subtract(add(P1,P5), P3), P7)
    
    result = [[0 for i in range(len(A))] for j in range(len(B))]

    for i in range(half):
        for j in range(half):
            result[i][j] = c11[i][j]
            result[i][j+half] = c12[i][j]
            result[i+half][j] = c21[i][j]
            result[i+half][j+half] = c22[i][j]


    return result



if __name__ == "__main__":
    A = [[1,1,1],[1,1,1],[1,1,1]]
    B = [[1,1,1],[1,1,1],[1,1,1]]


    print(strassen(A,B))
