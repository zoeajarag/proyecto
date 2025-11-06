import pygame
import colores

class Extra(pygame.sprite.Sprite):
    def __init__(self, j, k, image):
        self.image = image
        self.forma = pygame.Rect(0, 0, 45, 45)
        self.forma.center = (j, k)
    
    def dibujar(self, interfaz):
        interfaz.blit(self.image, self.forma)
        pygame.draw.rect(interfaz, colores.BLANCO, self.forma, 1)

    def movimientos(self, x, y):
        self.forma.x = x
        self.forma.y = y
