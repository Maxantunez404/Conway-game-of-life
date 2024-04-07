import cv2
import numpy as np

#tamaño del tablero
filas = 100
columnas = 100

#tamaño de los cuadrados del tablero
ancho_cuadro = 100 // columnas
altura_cuadro = 100 // filas

#colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)

#se crea la matriz tablero
tablero = np.zeros((100, 100, 3), dtype=np.uint8)

#RELLENAR EL TABLERO DE NEGRO
for fila in range(filas):
    for columna in range(columnas):
        tablero[fila * altura_cuadro: (fila + 1) * altura_cuadro,
                columna * ancho_cuadro: (columna + 1) * ancho_cuadro] = NEGRO
        
#SETEAR CELULAS VIVAS
tablero[5*altura_cuadro:8*altura_cuadro,5*ancho_cuadro:6*ancho_cuadro] = BLANCO

tablero[10*altura_cuadro:12*altura_cuadro,10*ancho_cuadro:12*ancho_cuadro] = BLANCO

tablero[10*altura_cuadro:13*altura_cuadro,20*ancho_cuadro:21*ancho_cuadro] = BLANCO
tablero[9*altura_cuadro:10*altura_cuadro,21*ancho_cuadro:22*ancho_cuadro] = BLANCO
tablero[8*altura_cuadro:9*altura_cuadro,22*ancho_cuadro:24*ancho_cuadro] = BLANCO
tablero[13*altura_cuadro:14*altura_cuadro,21*ancho_cuadro:22*ancho_cuadro] = BLANCO
tablero[14*altura_cuadro:15*altura_cuadro,22*ancho_cuadro:24*ancho_cuadro] = BLANCO
tablero[11*altura_cuadro:12*altura_cuadro,24*ancho_cuadro:25*ancho_cuadro] = BLANCO
tablero[9*altura_cuadro:10*altura_cuadro,25*ancho_cuadro:26*ancho_cuadro] = BLANCO
tablero[13*altura_cuadro:14*altura_cuadro,25*ancho_cuadro:26*ancho_cuadro] = BLANCO
tablero[10*altura_cuadro:13*altura_cuadro,26*ancho_cuadro:27*ancho_cuadro] = BLANCO
tablero[11*altura_cuadro:12*altura_cuadro,27*ancho_cuadro:28*ancho_cuadro] = BLANCO

tablero[8*altura_cuadro:11*altura_cuadro,30*ancho_cuadro:32*ancho_cuadro] = BLANCO
tablero[7*altura_cuadro:8*altura_cuadro,32*ancho_cuadro:33*ancho_cuadro] = BLANCO
tablero[11*altura_cuadro:12*altura_cuadro,32*ancho_cuadro:33*ancho_cuadro] = BLANCO
tablero[6*altura_cuadro:8*altura_cuadro,34*ancho_cuadro:35*ancho_cuadro] = BLANCO
tablero[11*altura_cuadro:13*altura_cuadro,34*ancho_cuadro:35*ancho_cuadro] = BLANCO

tablero[8*altura_cuadro:10*altura_cuadro,44*ancho_cuadro:46*ancho_cuadro] = BLANCO


while True:

    n_tablero = np.copy(tablero)


    for y in range(filas):
        for x in range(columnas):
            vecinos_vivos = 0
            #recorrer vecinos
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    if dy == 0 and dx ==0:
                        continue
                    vecino_y = (y + dy) % filas
                    vecino_x = (x + dx) % columnas
                    vecinos_vivos += int((tablero[vecino_y*altura_cuadro:(vecino_y+1)*altura_cuadro,
                                            vecino_x*ancho_cuadro:(vecino_x+1)*ancho_cuadro][0][0] == BLANCO)[0])        
            #print("y: ",y)
            #print("x: ",x)
            #print("vecinos vivos: ",vecinos_vivos)
            if tablero[y*altura_cuadro:(y+1)*altura_cuadro,x*ancho_cuadro:(x+1)*ancho_cuadro][0][0][0] == BLANCO[0]:
                if vecinos_vivos <2 or vecinos_vivos>3:
                    n_tablero[y*altura_cuadro:(y+1)*altura_cuadro,x*ancho_cuadro:(x+1)*ancho_cuadro] = NEGRO
            else:
                if vecinos_vivos ==3:
                    n_tablero[y*altura_cuadro:(y+1)*altura_cuadro,x*ancho_cuadro:(x+1)*ancho_cuadro] = BLANCO
            #print(tablero[5*altura_cuadro:(5+1)*altura_cuadro,5*ancho_cuadro:(5+1)*ancho_cuadro][0][0][0] == BLANCO[0])
    cv2.namedWindow("Tablero", cv2.WINDOW_NORMAL)
    cv2.imshow("Tablero", n_tablero)
    cv2.waitKey(1)

    # Actualizar el tablero
    tablero = np.copy(n_tablero)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()        