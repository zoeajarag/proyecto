import pygame
import colores

class Comida(pygame.sprite.Sprite):
    def __init__(self, j, k):
        self.forma = pygame.Rect(0, 0, 20, 20)
        self.forma.center = (j, k)
    
    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, colores.OLIVA, self.forma)

    def movimientos(self, x, y):
        self.forma.x = x
        self.forma.y = y
        
