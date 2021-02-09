# coding=utf-8
# Python3

def Quedan_fichas (N: int, jugadas: int) -> int:
    # Pre:  {N > 1 /\ 0 <= jugadas <= N*N*N}
    # Post: {Quedan_fichas = (exists i | 0 < i : Tfichas - jugadas = i) \/ ~(exists i | 0 < i : Tfichas - jugadas = i)}

    Tfichas = N * N * N    
    
    return Tfichas - jugadas

