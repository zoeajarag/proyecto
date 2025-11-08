import pygame
from personaje import Personaje
import colores
from random import randint
from comida import Comida
from chatarra import Chatarra
from extra import Extra

pygame.init()

ventana = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Food Drop Zoe")

#texto y otras cosas:
puntos = 0
N = "N"
vida = 3

fuente = pygame.font.Font("Retro Gaming.ttf", 15)
fuente_vida = pygame.font.Font("Hearts Salad.otf", 20)
fuente_perder = pygame.font.Font("Retro Gaming.ttf", 25)
fuente_final = pygame.font.Font("Retro Gaming.ttf", 50)


#defino los movimientos en falso
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#llamo al personaje y le digo donde quiero que esté
gatito = pygame.image.load("gatito1.png")
gatito = pygame.transform.scale(gatito, (gatito.get_width() * 3, gatito.get_height() * 3))
reserva = pygame.image.load("gatito2.png")
reserva = pygame.transform.scale(gatito, (gatito.get_width() * 3, gatito.get_height() * 3))
jugador = Personaje(400,350, gatito)


#todo lo referido a la comidita
sandia = pygame.image.load("sandia.png")
sandia = pygame.transform.scale(sandia, (sandia.get_width() * 1.5, sandia.get_height() * 1.5))
x1 = randint(15, 785)
y1 = 0
comidita1 = Comida(x1, y1, sandia)

frutilla = pygame.image.load("frutilla.png")
frutilla = pygame.transform.scale(frutilla, (frutilla.get_width() * 1.5, frutilla.get_height() * 1.5))
x2 = randint(15, 785)
y2 = -100
comidita2 = Comida(x2, y2, frutilla)

naranja = pygame.image.load("naranja.png")
naranja = pygame.transform.scale(naranja, (naranja.get_width() * 1.5, naranja.get_height() * 1.5))
x3 = randint(15, 785)
y3 = -200
comidita3 = Comida(x3, y3, naranja)

arandanos = pygame.image.load("arandanos.png")
arandanos = pygame.transform.scale(arandanos, (arandanos.get_width() * 1.5, arandanos.get_height() * 1.5))
x4 = randint(15, 785)
y4 = -300
comidita4 = Comida(x4, y4, arandanos)

cerezas = pygame.image.load("cerecitas.png")
cerezas = pygame.transform.scale(cerezas, (cerezas.get_width() * 1.5, cerezas.get_height() * 1.5))
x5 = randint(15, 785)
y5 = -400
comidita5 = Comida(x5, y5, cerezas)

#todo lo de chatarra
hacha = pygame.image.load("hachas.png")
hacha = pygame.transform.scale(hacha, (hacha.get_width() * 1.5, hacha.get_height() * 1.5))
xx1 = randint(15, 785)
yy1 = -50
Chatarrita1 = Chatarra(xx1, yy1, hacha)

botas = pygame.image.load("botas.png")
botas = pygame.transform.scale(botas, (botas.get_width() * 1.5, botas.get_height() * 1.5))
xx2 = randint(15, 785)
yy2 = -150
Chatarrita2 = Chatarra(xx2, yy2, botas)

CD = pygame.image.load("CD.png")
CD = pygame.transform.scale(CD, (CD.get_width() * 1.5, CD.get_height() * 1.5))
xx3 = randint(15, 785)
yy3 = -250
Chatarrita3 = Chatarra(xx3, yy3, CD)

botella = pygame.image.load("botella.png")
botella = pygame.transform.scale(botella, (botella.get_width() * 1.5, botella.get_height() * 1.5))
xx4 = randint(15, 785)
yy4 = -350
Chatarrita4 = Chatarra(xx4, yy4, botella)

bomba = pygame.image.load("bomba.png")
bomba = pygame.transform.scale(bomba, (bomba.get_width() * 1.5, bomba.get_height() * 1.5))
xx5 = randint(15, 785)
yy5 = -450
Chatarrita5 = Chatarra(xx5, yy5, bomba)

#Vida extra
imagen_extra1 = pygame.image.load("corazon1.png")
imagen_extra1 = pygame.transform.scale(imagen_extra1, (imagen_extra1.get_width() * 1.5, imagen_extra1.get_height() * 1.5))
extraX = randint(22, 778)
extraY = -800
vida_extra = Extra(extraX, extraY, imagen_extra1)

#musiquita
pygame.mixer.music.load("musiquita_juego2_2.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

contador = 0

#esto me permite controlar la velocidad de los eventos?
reloj = pygame.time.Clock()

#esto es para que el bucle siga hasta que cierres la ventana
run = True

while run == True:

    reloj.tick(60) #velocidad en que las cosas pasan

    ventana.fill(colores.NEGRO) #fondo del juego

    #introduzco y acomodo los textos
    corazones_llenos = N * vida
    texto_vida = fuente.render("Vida:", True, colores.AMARILLO)
    texto_corazones = fuente_vida.render(corazones_llenos, True, colores.ROJO)
    texto = fuente.render(f"Puntuacion: {puntos}", True, colores.AMARILLO)
    texto_perder = fuente_perder.render(f"Puntuacion final: {puntos}", True, colores.BLANCO)
    texto_final = fuente_final.render("¡ESTAS ELIMINADO!", True, colores.ROJO)
    ventana.blit(texto, (20, 10))
    ventana.blit(texto_vida, (20, 30))
    ventana.blit(texto_corazones, (70, 30))

    #Movimientos
    delta_x = 0
    delta_y = 0
        
    if vida > 0:
        if mover_derecha == True:
            delta_x = 5
        if mover_izquierda == True:
            delta_x = -5

        #llamo a las funciones de la clase Personaje
        jugador.movimiento(delta_x, delta_y)
        jugador.update()
        jugador.dibujar(ventana)


        #cosas de la comida
        comidita1.dibujar(ventana)
        comidita2.dibujar(ventana)
        comidita3.dibujar(ventana)
        comidita4.dibujar(ventana)
        comidita5.dibujar(ventana)

        Chatarrita1.dibujar(ventana)
        Chatarrita2.dibujar(ventana)
        Chatarrita3.dibujar(ventana)
        Chatarrita4.dibujar(ventana)
        Chatarrita5.dibujar(ventana)

        contador += 1
        
        comidita1.movimientos(x1, y1)
        comidita2.movimientos(x2, y2)
        comidita3.movimientos(x3, y3)
        comidita4.movimientos(x4, y4)
        comidita5.movimientos(x5, y5)

        Chatarrita1.movimientos(xx1, yy1)
        Chatarrita2.movimientos(xx2, yy2)
        Chatarrita3.movimientos(xx3, yy3)
        Chatarrita4.movimientos(xx4, yy4)
        Chatarrita5.movimientos(xx5, yy5)

        if vida < 3:
            vida_extra.movimientos(extraX, extraY)
            vida_extra.dibujar(ventana)

            if contador%10 == 0:
                extraY += 20
            
            if extraY > 400:
                extraX = randint(22, 778)
                extraY -= 1200

            if extraX in range(jugador.forma.left, jugador.forma.right) and extraY > jugador.forma.top:
                extraX = randint(22, 778)
                extraY -= 1200
                vida += 1

        if contador%10 == 0:
            y1 += 15
            y2 += 15
            y3 += 15
            y4 += 15
            y5 += 15
            yy1 += 18
            yy2 += 18
            yy3 += 18
            yy4 += 18
            yy5 += 18

        if y1 > 400:
            x1 = randint(15, 785)
            y1 -= 500
        if y2 > 400:
            x2 = randint(15, 785)
            y2 -= 550
        if y3 > 400:
            x3 = randint(15, 785)
            y3 -= 550
        if y4 > 400:
            x4 = randint(15, 785)
            y4 -= 550
        if y5 > 400:
            x5 = randint(15, 785)
            y5 -= 550

        if yy1 > 400:
            xx1 = randint(15, 785)
            yy1 -= 500
        if yy2 > 400:
            xx2 = randint(15, 785)
            yy2 -= 550
        if yy3 > 400:
            xx3 = randint(15, 785)
            yy3 -= 550
        if yy4 > 400:
            xx4 = randint(15, 785)
            yy4 -= 550
        if yy5 > 400:
            xx5 = randint(15, 785)
            yy5 -= 550


        if x1 in range(jugador.forma.left, jugador.forma.right) and y1 > jugador.forma.top:
            x1 = randint(15, 785)
            y1 -= 500
            puntos += 10

        if x2 in range(jugador.forma.left, jugador.forma.right) and y2 > jugador.forma.top:
            x2 = randint(15, 785)
            y2 -= 550
            puntos += 10

        if x3 in range(jugador.forma.left, jugador.forma.right) and y3 > jugador.forma.top:
            x3 = randint(15, 785)
            y3 -= 550
            puntos += 10

        if x4 in range(jugador.forma.left, jugador.forma.right) and y4 > jugador.forma.top:
            x4 = randint(15, 785)
            y4 -= 550
            puntos += 10

        if x5 in range(jugador.forma.left, jugador.forma.right) and y5 > jugador.forma.top:
            x5 = randint(15, 785)
            y5 -= 550
            puntos += 10        

        
        if xx1 in range(jugador.forma.left, jugador.forma.right) and yy1 > jugador.forma.top:
            xx1 = randint(15, 785)
            yy1 -= 500
            vida -= 1

        if xx2 in range(jugador.forma.left, jugador.forma.right) and yy2 > jugador.forma.top:
            xx2 = randint(15, 785)
            yy2 -= 550
            vida -= 1

        if xx3 in range(jugador.forma.left, jugador.forma.right) and yy3 > jugador.forma.top:
            xx3 = randint(15, 785)
            yy3 -= 550
            vida -= 1

        if xx4 in range(jugador.forma.left, jugador.forma.right) and yy4 > jugador.forma.top:
            xx4 = randint(15, 785)
            yy4 -= 550
            vida -= 1

        if xx5 in range(jugador.forma.left, jugador.forma.right) and yy5 > jugador.forma.top:
            xx5 = randint(15, 785)
            yy5 -= 550
            vida -= 1

    #abre la ventana hasta que la cierres
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False 
        
        #teclas y movimiento
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                mover_izquierda = True
            if evento.key == pygame.K_RIGHT:
                mover_derecha = True

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                mover_izquierda = False
            if evento.key == pygame.K_RIGHT:
                mover_derecha = False
        
    
    if vida < 1:
        ventana.fill(colores.AZUL_OSCURO )
        ventana.blit(texto_final, (100, 100))
        ventana.blit(texto_perder, (250, 200))

    pygame.display.update()
        
pygame.quit()
