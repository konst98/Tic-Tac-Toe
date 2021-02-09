# coding=utf-8
# Python3

def HayAlineaVertical (T:[[[int]]], y: int, z: int, N: int) -> bool:
    # Pre:  {0 <= y < N /\ 0 <= z < N /\ N > 1}
    # Post: {HayAlineaVertical = (forall i| 0 <= i < N - 1 : A[i][y][z] = A[i+1][y][z]) \/ ~(forall i| 0 <= i < N - 1 : A[i][y][z] = A[i+1][y][z])}

    i, Vertical = 0, True

    while i < N - 1 and Vertical:
        if (T[i][y][z] == T[i + 1][y][z]):            
            i = i + 1
        else:
            Vertical = False
            i = i + 1

    return Vertical    
    

def HayAlineaHorizontal (T:[[[int]]], x: int, z: int, N: int) -> bool:
	# Pre:  {0 <= x < N /\ 0 <= z < N /\ N > 1}
    # Post: {HayAlineaHorizontal = (forall j| 0 <= j < N - 1 : A[x][j][z] = A[x][j+1][z]) \/ ~(forall j| 0 <= j < N - 1: A[x][j][z] = A[x][j+1][z])}
    
    j, Horizontal = 0, True

    while j < N - 1 and Horizontal:
        if (T[x][j][z] == T[x][j+1][z]):            
            j = j + 1
        else:
            Horizontal = False
            j = j + 1

    return Horizontal   


def HayAlineaDiag (T:[[[int]]], x: int, y: int, z: int, N: int) -> bool:
    # Pre:  {0 <= x < N /\ 0 <= y < N /\ 0 <= z < N /\ N > 1}
    # Post: {HayAlineaDiag = (forall i,j| 0 <= i < N /\ 0 <= j < N /\ i = j: A[i][j][z] = A[x][y][z]) /\ (forall i,j| 0 <=  < N /\ 0 <= j < N  /\ i + j = N - 1s: A[i][j][z] = A[x][y][z])}

    i, j, HayDiagonalP, DiagonalP = 0, 0, False, True

    while x == y and i < N - 1 and j < N - 1 and DiagonalP:
        if (T[i][j][z] == T[i+1][j+1][z]):
            i, j = i + 1, j + 1
            HayDiagonalP = True
        else:
            DiagonalP, HayDiagonalP = False, False
            i, j = i + 1, j + 1
    
    i, j, HayDiagonalS, DiagonalS = 0, N - 1, False, True

    while x + y == N - 1 and i < N - 1 and j > 0 and DiagonalS:
        if (T[i][j][z] == T[i+1][j-1][z]):
            i, j = i + 1, j - 1
            HayDiagonalS = True
        else:
            DiagonalS, HayDiagonalS = False, False
            i, j = i + 1, j - 1

    return HayDiagonalP, HayDiagonalS


def HayAlineaTableros (T:[[[int]]], x: int, y: int, N: int) -> bool:
	# Pre:  {0 <= x < N /\ 0 <= y < N /\ N > 1}
    # Post: {HayAlineaTablero = Tablero = (forall k| 0 <= k < N -1 : A[x][y][k] = A[x][y][k+1])}
    
    k, Tablero = 0, True

    while k < N - 1 and Tablero:
        if (T[x][y][k] == T[x][y][k + 1]):            
            k = k + 1
        else:
            Tablero = False
            k = k + 1

    return Tablero
