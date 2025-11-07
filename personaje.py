import pygame
import colores

class Personaje(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen):
        self.imagen = imagen
        self.forma = pygame.Rect(0, 0, 48, 78)
        self.forma.center = (x, y)

    def dibujar(self, interfaz):
        interfaz.blit(self.imagen, self.forma)
        # pygame.draw.rect(interfaz, colores.AMARILLO, self.forma, 1)

    def movimiento(self, delta_x, delta_y):
        self.forma.x += delta_x
        self.forma.y += delta_y
        
    def update(self):
        if self.forma.left < 0:
            self.forma.left = 0
        if self.forma.right > 800:
            self.forma.right = 800
        # if self.forma.top < 0:
        #     self.forma.top = 0
        # if self.forma.bottom > 600:
        #     self.forma.bottom = 600