import pygame
import sys
from pygame.locals import *

pygame.init()

pygame.mixer.music.set_volume(5)
musica_de_fundo = pygame.mixer.music.load('So.mp3')
pygame.mixer.music.play(-1)

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('EI! VOCÊ SABE QUAL O NOME DESSA IMAGEM?')

branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0,255,0)

font = pygame.font.SysFont('Cascadia Mono SemiBold',40)
font0 = pygame.font.SysFont('Cascadia Mono SemiBold',90)

frutas = [
    {'nome': 'bolo', 'imagem': 'bolo.png'},
    {'nome': 'maca', 'imagem': 'maca2.png'},
]

for fruta in frutas:
    fruta['imagem'] = pygame.image.load(fruta['imagem'])

def texto(texto, font, cor, fundo, x, y):
    textobj = font.render(texto, 1, cor)
    textorect = textobj.get_rect()
    textorect.topleft = (x, y)
    fundo.blit(textobj, textorect)

frutaatual = 0
input_texto = ''.upper()
pontos = 0
tentativas = 3
r = True
while r:

    tela.fill(branco)
    texto(f'                         ACERTE O NOME DA IMAGEM        VIDAS: {tentativas}', font, preto, tela, 1, 1)


    for event in pygame.event.get():
        if event.type == QUIT:

            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                r = False

            elif event.key == K_RETURN:
                if input_texto.upper() == frutas[frutaatual]['nome']:
                    pontos += 1

                    message = 'parabens'
                    text_surface = font0.render(message, True, verde, )
                    text_rect = text_surface.get_rect(center=(800//2, 600// 2))
                    tela.fill(branco)
                    tela.blit(text_surface, text_rect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    tela.fill(branco)
                    surface = pygame.display.set_mode((800, 600))
                    c = input_texto = ''
                    pygame.draw.rect(surface, branco, pygame.Rect(30, 30, 60, 60))
                    frutaquejafoi = (frutaatual + 1) % len(frutas)

                elif input_texto.lower() != frutas[frutaatual]['nome']:
                    tentativas -= 1
                    pontos -= 1
                    input_texto = fruta['nome']

                if pontos == 2 or tentativas == 0:
                    r = False
            elif event.key == K_BACKSPACE:
                input_texto = input_texto[:-1]

            else:
                input_texto += event.unicode


    foto = frutas[frutaatual]['imagem']
    tela.blit(foto, (150, 50))
    pygame.draw.line(tela, preto, (175, 200//2), (600, 100), 3)
    pygame.display.update()


    texto(input_texto, font, preto, tela, 200, 500)

    pygame.display.flip()

tela.fill(branco)
texto(f'Sua pontuação: {pontos}', font0, preto, tela, 170, 250)
pygame.display.flip()

pygame.time.wait(5000)
pygame.quit()
