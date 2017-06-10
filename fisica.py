import math
from pygame.math import Vector2 as Vector

VELOCIDADE_MAXIMA = 3

def aplicaForca(corpo, forca):
    corpo['aceleracao'] = forca/corpo['massa']
    return corpo

def limitaVetor(u, lim):
    if Vector.length(u) > lim**2:
        u = Vector.normalize(u)*lim
    return u

def atualiza(corpo):
    corpo['velocidade'] += corpo['aceleracao']
    corpo['velocidade'] = limitaVetor(corpo['velocidade'], VELOCIDADE_MAXIMA)
    corpo['posicao'] += corpo['velocidade']
    corpo['aceleracao'] = 0
    return corpo

def criaCorpo():
    '''Retorna um dicionário com as características de um corpo
    físico'''
    corpo = {}
    corpo['velocidade'] = Vector()
    corpo['aceleracao'] = Vector()
    corpo['posicao'] = Vector()
    corpo['massa'] = 1
    corpo['angulo'] = 0
    return corpo

if __name__ == '__main__':
    import pygame, fisica
    pygame.init()
    w = 800
    h = 400
    tela = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0) 
    ROTACAO = 90
    nave_surface = pygame.image.load('./assets/images/jogador.png')
    nave_surface = pygame.transform.rotozoom(nave_surface, -90, 1)
    nave = fisica.criaCorpo()
    while 1:
        tela.fill((0, 0, 0))
        clock.tick(60)

        forca = Vector(0, 0)
#       keys = pygame.key.get_pressed()
#       if keys[pygame.K_UP]:
#           teta = math.radians(nave['angulo'])
#           x = math.cos(teta)
#           y = math.sin(teta)
#           forca += Vector(x, -y)
#       if keys[pygame.K_LEFT]:
#           nave['angulo'] += ROTACAO
#           nave_surface = pygame.transform.rotozoom(nave_surface, ROTACAO, 1)
#       if keys[pygame.K_RIGHT]:
#           nave['angulo'] -= ROTACAO
#           nave_surface = pygame.transform.rotozoom(nave_surface, -ROTACAO, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                teta = math.radians(nave['angulo'])
                x = math.cos(teta)
                y = math.sin(teta)
                forca += Vector(x, -y)
            if keys[pygame.K_LEFT]:
                nave['angulo'] += ROTACAO
                nave_surface = pygame.transform.rotozoom(nave_surface, ROTACAO, 1)
            if keys[pygame.K_RIGHT]:
                nave['angulo'] -= ROTACAO
                nave_surface = pygame.transform.rotozoom(nave_surface, -ROTACAO, 1)
        
        nave = fisica.aplicaForca(nave, forca)
        nave = fisica.atualiza(nave)
        tela.blit(nave_surface, nave['posicao'])
        pygame.display.update()
