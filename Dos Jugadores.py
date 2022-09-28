from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
from time import sleep_ms, sleep
import random


i2c = I2C(0, scl=Pin(22), sda=Pin(23))
ancho = 128
alto = 64
oled = SSD1306_I2C(ancho, alto, i2c)

nombre_1 = input()
print("NOMBRE JUGADOR 'X': ")
nombre_3 = input()
print("NOMBRE JUGADOR 'O': ")
nombre_2 = input()


eje_x = ADC(Pin(33))
eje_x.atten(ADC.ATTN_11DB)
eje_x.width(ADC.WIDTH_12BIT)

eje_y = ADC(Pin(32))
eje_y.atten(ADC.ATTN_11DB)
eje_y.width(ADC.WIDTH_12BIT)

botón = Pin(13, Pin.IN, Pin.PULL_UP)

j2_eje_x = ADC(Pin(35))
j2_eje_x.atten(ADC.ATTN_11DB)
j2_eje_x.width(ADC.WIDTH_12BIT)

j2_eje_y = ADC(Pin(34))
j2_eje_y.atten(ADC.ATTN_11DB)
j2_eje_y.width(ADC.WIDTH_12BIT)

botón_2 = Pin(12, Pin.IN, Pin.PULL_UP)

posiciones = 0
posiciones_2 = 0
click_1 = 0
click_2 = 0

posO = [1, 2, 3, 4, 5, 6, 7, 8, 9]
j1_contador_x = 0
j1_contador_y = 0


j2_contador_x = 0
j2_contador_y = 0

matriz = [
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
]

matriz_impresión = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def seleccionar(j1_contador_x, j1_contador_y, j2_contador_x, j2_contador_y, posiciones, posiciones_2):
    if (j1_contador_x == 0 and j1_contador_y == 0):
        oled.text("■", 15, 15, 10)
        posiciones = 1
    else:
        oled.text(" ", 15, 15, 10)

    if (j1_contador_x == 1 and j1_contador_y == 0):
        oled.text("■", 60, 15, 10)
        posiciones = 2
    else:
        oled.text(" ", 60, 15, 10)

    if (j1_contador_x == 2 and j1_contador_y == 0):
        oled.text("■", 105, 15, 10)
        posiciones = 3
    else:
        oled.text(" ", 105, 15, 10)

    if (j1_contador_x == 0 and j1_contador_y == 1):
        oled.text("■", 15, 35, 10)
        posiciones = 4
    else:
        oled.text(" ", 15, 35, 10)

    if (j1_contador_x == 1 and j1_contador_y == 1):
        oled.text("■", 60, 35, 10)
        posiciones = 5
    else:
        oled.text(" ", 60, 35, 10)

    if (j1_contador_x == 2 and j1_contador_y == 1):
        oled.text("■", 105, 35, 10)
        posiciones = 6
    else:
        oled.text(" ", 105, 35, 10)

    if (j1_contador_x == 0 and j1_contador_y == 2):
        oled.text("■", 15, 51, 10)
        posiciones = 7
    else:
        oled.text(" ", 15, 51, 10)

    if (j1_contador_x == 1 and j1_contador_y == 2):
        oled.text("■", 60, 51, 10)
        posiciones = 8
    else:
        oled.text(" ", 60, 51, 10)

    if (j1_contador_x == 2 and j1_contador_y == 2):
        oled.text("■", 105, 51, 10)
        posiciones = 9
    else:
        oled.text(" ", 105, 51, 10)

    if (j2_contador_x == 0 and j2_contador_y == 0):
        oled.text("¤", 15, 15, 10)
        posiciones_2 = 1
    else:
        oled.text(" ", 15, 15, 10)

    if (j2_contador_x == 1 and j2_contador_y == 0):
        oled.text("¤", 60, 15, 10)
        posiciones_2 = 2
    else:
        oled.text(" ", 60, 15, 10)

    if (j2_contador_x == 2 and j2_contador_y == 0):
        oled.text("¤", 105, 15, 10)
        posiciones_2 = 3
    else:
        oled.text(" ", 105, 15, 10)

    if (j2_contador_x == 0 and j2_contador_y == 1):
        oled.text("¤", 15, 35, 10)
        posiciones_2 = 4
    else:
        oled.text(" ", 15, 35, 10)

    if (j2_contador_x == 1 and j2_contador_y == 1):
        oled.text("¤", 60, 35, 10)
        posiciones_2 = 5
    else:
        oled.text(" ", 60, 35, 10)

    if (j2_contador_x == 2 and j2_contador_y == 1):
        oled.text("¤", 105, 35, 10)
        posiciones_2 = 6
    else:
        oled.text(" ", 105, 35, 10)

    if (j2_contador_x == 0 and j2_contador_y == 2):
        oled.text("¤", 15, 51, 10)
        posiciones_2 = 7
    else:
        oled.text(" ", 15, 51, 10)

    if (j2_contador_x == 1 and j2_contador_y == 2):
        oled.text("¤", 60, 51, 10)
        posiciones_2 = 8
    else:
        oled.text(" ", 60, 51, 10)

    if (j2_contador_x == 2 and j2_contador_y == 2):
        oled.text("¤", 105, 51, 10)
        posiciones_2 = 9
    else:
        oled.text(" ", 105, 51, 10)


def ponerXyO(posiciones, click_1, click_2, turno):

    contador = turno

    if (turno == 0):

        if (click_1 == 1 and matriz[0][0] == 2):
            matriz[0][0] = 1
            matriz_impresión[0][0] = "X"
            contador = not contador
        if (click_1 == 2 and matriz[0][1] == 2):
            matriz[0][1] = 1
            matriz_impresión[0][1] = "X"
            contador = not contador
        if (click_1 == 3 and matriz[0][2] == 2):
            matriz[0][2] = 1
            matriz_impresión[0][2] = "X"
            contador = not contador
        if (click_1 == 4 and matriz[1][0] == 2):
            matriz[1][0] = 1
            matriz_impresión[1][0] = "X"
            contador = not contador
        if (click_1 == 5 and matriz[1][1] == 2):
            matriz[1][1] = 1
            matriz_impresión[1][1] = "X"
            contador = not contador
        if (click_1 == 6 and matriz[1][2] == 2):
            matriz[1][2] = 1
            matriz_impresión[1][2] = "X"
            contador = not contador
        if (click_1 == 7 and matriz[2][0] == 2):
            matriz[2][0] = 1
            matriz_impresión[2][0] = "X"
            contador = not contador
        if (click_1 == 8 and matriz[2][1] == 2):
            matriz[2][1] = 1
            matriz_impresión[2][1] = "X"
            contador = not contador
        if (click_1 == 9 and matriz[2][2] == 2):
            matriz[2][2] = 1
            matriz_impresión[2][2] = "X"
            contador = not contador

    else:
        if (click_2 == 1 and matriz[0][0] == 2):
            matriz[0][0] = 0
            matriz_impresión[0][0] = "O"
            contador = not contador
        if (click_2 == 2 and matriz[0][1] == 2):
            matriz[0][1] = 0
            matriz_impresión[0][1] = "O"
            contador = not contador
        if (click_2 == 3 and matriz[0][2] == 2):
            matriz[0][2] = 0
            matriz_impresión[0][2] = "O"
            contador = not contador
        if (click_2 == 4 and matriz[1][0] == 2):
            matriz[1][0] = 0
            matriz_impresión[1][0] = "O"
            contador = not contador
        if (click_2 == 5 and matriz[1][1] == 2):
            matriz[1][1] = 0
            matriz_impresión[1][1] = "O"
            contador = not contador
        if (click_2 == 6 and matriz[1][2] == 2):
            matriz[1][2] = 0
            matriz_impresión[1][2] = "O"
            contador = not contador
        if (click_2 == 7 and matriz[2][0] == 2):
            matriz[2][0] = 0
            matriz_impresión[2][0] = "O"
            contador = not contador
        if (click_2 == 8 and matriz[2][1] == 2):
            matriz[2][1] = 0
            matriz_impresión[2][1] = "O"
            contador = not contador
        if (click_2 == 9 and matriz[2][2] == 2):
            matriz[2][2] = 0
            matriz_impresión[2][2] = "O"
            contador = not contador

    oled.text(matriz_impresión[0][0], 15, 15, 1)
    oled.text(matriz_impresión[0][1], 60, 15, 1)
    oled.text(matriz_impresión[0][2], 105, 15, 1)

    oled.text(matriz_impresión[1][0], 15, 35, 1)
    oled.text(matriz_impresión[1][1], 60, 35, 1)
    oled.text(matriz_impresión[1][2], 105, 35, 1)

    oled.text(matriz_impresión[2][0], 15, 51, 10)
    oled.text(matriz_impresión[2][1], 60, 51, 10)
    oled.text(matriz_impresión[2][2], 105, 51, 10)

    return contador


def refrescar(oled):

    seleccionar(j1_contador_x, j1_contador_y,
                j2_contador_x, j2_contador_y, posiciones, posiciones_2)


def Comprobar_partida():

    ganador = False

    for i in range(len(matriz)):
        if matriz[i][0] != 2 and matriz[i][1] != 2 and matriz[i][2] != 2 and (matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2]):
            if matriz[i][0] == 0:
                return 0
            else:
                return 1
                ganador = True
    for i in range(len(matriz[0])):
        if matriz[0][i] != 2 and matriz[1][i] != 2 and matriz[2][i] != 2 and (matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i]):
            if matriz[0][i] == 0:
                return 0
                ganador = True
            else:
                return 1
                ganador = True
    if matriz[1][1] != 2 and ((matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2]) or (matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0])):
        if matriz[1][1] == 0:
            return 0
            ganador = True
        else:
            return 1
            ganador = True

    empate = True

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 2:
                empate = False

    if empate == True and ganador == False:
        return 2

    return 3


def vaciar_matrices():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = 2
            matriz_impresión[i][j] = ""


contador = 0
end = False

while True:

    estado = Comprobar_partida()

    if estado == 0:
        click_1 = 0
        click_2 = 0
        oled.fill(0)
        vaciar_matrices()
        oled.text("GANA JUGADOR", 15, 27, 1)
        oled.text("O"+nombre_2+"O", 37, 42, 1)
        oled.show()
        sleep(3)

    if estado == 1:
        click_1 = 0
        click_2 = 0
        oled.fill(0)
        vaciar_matrices()
        oled.text("GANA JUGADOR", 15, 27, 1)
        oled.text("X"+nombre_3+"X", 37, 42, 1)
        oled.show()
        sleep(3)
    if estado == 2:
        click_1 = 0
        click_2 = 0
        oled.fill(0)
        vaciar_matrices()
        oled.text("EMPATE", 37, 27, 1)
        oled.show()
        sleep(3)

    oled.line(42, 12, 42, 64, 1)
    oled.line(84, 12, 84, 64, 1)
    oled.line(128, 30, 0, 30, 1)
    oled.line(128, 47, 0, 47, 1)
    oled.text("GAME ONE", 30, 00, 1)

    j1_temp_x = eje_x.read()
    j1_temp_y = eje_y.read()

    j2_temp_x = j2_eje_x.read()
    j2_temp_y = j2_eje_y.read()

    if (j1_temp_x == 0 and j1_contador_x != 2):
        j1_contador_x +=1
        sleep_ms(200)
    if (j1_temp_x == 4095 and j1_contador_x != 0):
        j1_contador_x -=1
        sleep_ms(200)
    if (j1_temp_y == 0 and j1_contador_y != 2):
        j1_contador_y +=1
        sleep_ms(200)
    if (j1_temp_y == 4095 and j1_contador_y != 0):
        j1_contador_y -=1
        sleep_ms(200)

    if (j2_temp_x == 0 and j2_contador_x != 2):
        j2_contador_x +=1
        sleep_ms(200)
    if (j2_temp_x == 4095 and j2_contador_x != 0):
        j2_contador_x -=1
        sleep_ms(200)
    if (j2_temp_y == 0 and j2_contador_y != 2):
        j2_contador_y +=1
        sleep_ms(200)
    if (j2_temp_y == 4095 and j2_contador_y != 0):
        j2_contador_y -=1
        sleep_ms(200)

    if j1_contador_x == 0 and j1_contador_y == 0:
        posiciones = 1
    if j1_contador_x == 1 and j1_contador_y == 0:
        posiciones = 2
    if j1_contador_x == 2 and j1_contador_y == 0:
        posiciones = 3
    if j1_contador_x == 0 and j1_contador_y == 1:
        posiciones = 4
    if j1_contador_x == 1 and j1_contador_y == 1:
        posiciones = 5
    if j1_contador_x == 2 and j1_contador_y == 1:
        posiciones = 6
    if j1_contador_x == 0 and j1_contador_y == 2:
        posiciones = 7
    if j1_contador_x == 1 and j1_contador_y == 2:
        posiciones = 8
    if j1_contador_x == 2 and j1_contador_y == 2:
        posiciones = 9

    if j2_contador_x == 0 and j2_contador_y == 0:
        posiciones_2 = 1
    if j2_contador_x == 1 and j2_contador_y == 0:
        posiciones_2 = 2
    if j2_contador_x == 2 and j2_contador_y == 0:
        posiciones_2 = 3
    if j2_contador_x == 0 and j2_contador_y == 1:
        posiciones_2 = 4
    if j2_contador_x == 1 and j2_contador_y == 1:
        posiciones_2 = 5
    if j2_contador_x == 2 and j2_contador_y == 1:
        posiciones_2 = 6
    if j2_contador_x == 0 and j2_contador_y == 2:
        posiciones_2 = 7
    if j2_contador_x == 1 and j2_contador_y == 2:
        posiciones_2 = 8
    if j2_contador_x == 2 and j2_contador_y == 2:
        posiciones_2 = 9

    if (not botón.value()):
        click_1 = posiciones
        sleep_ms(200)

    if (not botón_2.value()):
        click_2 = posiciones_2
        sleep_ms(200)

    contador = ponerXyO(posiciones, click_1, click_2, contador)
    refrescar(oled)

    oled.show()
    oled.fill(0)
