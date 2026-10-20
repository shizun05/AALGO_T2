def imprime(mat):
    for x in mat:
        print(x)
    print()

def valido(lab, res, f, c):
    if f >= len(lab):
        return False
    if f < 0:
        return False
    if c >= len(lab[0]):
        return False
    if c < 0:
        return False
    if res[f][c] == 1:
        return False
    if lab[f][c] == 0:
        return False
    return True

def puntos(valor):
    # Las celdas que tienen 3 o 4 suman ese valor
    if valor >= 3:
        return valor
    return 0

def laberB(lab, res, f, c, suma):
    if f == 0 and c == 0:
        # Celda de llegada (F), más de 23 puntos
        if valido(lab, res, f, c):
            if suma + puntos(lab[f][c]) >= 23:
                res[f][c] = 1
                return True
            else:
                return False
        else:
            return False
    else:
        if valido(lab, res, f, c):
            res[f][c] = 1
            suma = suma + puntos(lab[f][c])
            if laberB(lab, res, f-1, c, suma):      # arriba
                return True
            elif laberB(lab, res, f, c+1, suma):    # derecha
                return True
            elif laberB(lab, res, f+1, c, suma):    # abajo
                return True
            elif laberB(lab, res, f, c-1, suma):    # izquierda
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False

# Laberinto original
lab = [
    [1,1,1,3,0,1,1,1,4],
    [3,0,0,1,0,1,0,0,1],
    [1,1,0,1,1,1,1,0,1],
    [0,1,0,1,0,0,1,0,1],
    [1,1,1,1,1,1,3,1,1],
    [3,0,1,0,0,0,1,0,1],
    [1,1,1,1,3,1,1,1,1],
    [1,0,0,1,0,1,0,0,4],
    [1,1,3,1,0,1,1,1,1]
]
res = [[0 for _ in range(9)] for _ in range(9)]

print("Laberinto original:")
imprime(lab)

# El raton inicia en la esquina inferior izquierda (I)
if laberB(lab, res, 8, 0, 0):
    print("Salimos!")
else:
    print("Quedamos atrapados")

print("Matriz del camino:")
imprime(res)

total = 0
for i in range(len(lab)):
    for j in range(len(lab[0])):
        if res[i][j] == 1:
            total = total + puntos(lab[i][j])
print("Puntos acumulados:", total)