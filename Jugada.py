# coding=utf-8
# Python3

def EsValida (T:[[[int]]], x:int, y: int, z: int, N: int) -> bool:
	# Pre:  {N > 1 /\ 0 <= x < N /\ 0 <= y < N /\ 0 <= z < N /\ (T[i][j][k] = 0 \/ T[i][j][k] = 1 \/ T[i][j][k] = 2)}
	# Post: {EsValida == (T[i][j][k] = 0)}	

	if T[x][y][z] == 0:
		return True
	else:						
		return False

def CambiarJugador (turno: int)	-> int:
	# Pre:  {0 < turno < 3}
	# Post: {CambiarJugador == (turno = 1 \/ turno = 2)}
	if turno == 1:
		turno = 2
	else:
		turno = 1
	return turno

def ReflejarJugada (T:[[[int]]], N: int, turno: int) -> 'void':
    # Pre:  {N > 1}
    # Post: {ReflejarJugada = A : array [0..N) x [0..N) x [0..N) of int}
    
	for k in range (0,N):
		for j in range (0,N):
			for i in range (0,N):
				print (T[i][j][k], end = " ")
			print (sep = "\n")
		print (sep = "\n")

def SumarLinea (turno: int, Puntos1: int, Puntos2: int) -> int:
	# Pre:  {0 < turno < 3}
	# Post: {0 <= Puntos1 < N*N /\ 0 <= Puntos2 < N*N}
	if turno == 1:
		Puntos1 = Puntos1 + 1
	elif turno == 2:
		Puntos2 = Puntos2 + 1
	
	return Puntos1, Puntos2