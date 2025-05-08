import pygame
import sys
from pygame.locals import *

pygame.init()

pygame.mixer.music.set_volume(5)
musica_de_fundo = pygame.mixer.music.load('So.mp3')
pygame.mixer.music.play(-1)

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('EI! VOCÊ SABE O NOME DESSA IMAGEM?')

branco = (240,255,240)
preto = (0, 0, 0)
verde = (0, 255, 0)

font = pygame.font.SysFont('Cascadia Mono SemiBold', 55)
font0 = pygame.font.SysFont('Cascadia Mono SemiBold', 70)
font1 = pygame.font.SysFont('Cascadia Mono SemiBold', 30)

moldurap = 550
molduraq = 380
mx = (400 - moldurap // 2)
my = (300 - molduraq // 2)

moldurag = 400
moldurah = 90
mg = (400 - moldurag // 2)
mh = (550 - moldurah // 2)

coisas = [
    {'nome': 'flor', 'imagem': 'flor.png'},
    {'nome': 'uva', 'imagem': 'uva.jpg'},
]
for coiso in coisas:
    coiso['imagem'] = pygame.image.load(coiso['imagem'])

def texto(texto, font, cor, fundo, x, y):
    textobj = font.render(texto, 1, cor)
    textorect = textobj.get_rect()
    textorect.topleft = (x, y)
    fundo.blit(textobj, textorect)

coisado = 0
input_texto = ''
pontos = 0
vidas = 3

r = True
while r:
    tela.fill(branco)
    pygame.draw.rect(tela, preto, (mx, my, moldurap, molduraq), 5)
    pygame.draw.rect(tela, preto, (mg, mh, moldurag, moldurah), 5)
    texto(f'ACERTE O NOME DA IMAGEM', font, preto, tela, 120, 1)
    texto(f'VIDAS RESTANTES: {vidas}', font1, preto, tela, 285, 50)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                r = False
            elif event.key == K_RETURN:
                if input_texto == coisas[coisado]['nome']:
                    pontos += 1
                    parabens = 'PARABÉNS'
                    textof = font0.render(parabens, True, verde)
                    textolugar = textof.get_rect(center=(800 // 2, 600 // 2))
                    tela.fill(branco)
                    tela.blit(textof, textolugar)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    tela.fill(branco)
                    surface = pygame.display.set_mode((800, 600))
                    c = input_texto = ''

                    pygame.draw.rect(surface, branco, pygame.Rect(30, 30, 60, 60))
                    coisado = (coisado + 1) % len(coisas)

                elif input_texto != coisas[coisado]['nome']:
                    vidas -= 1
                    correcao = coiso['nome']
                    textof0 = font0.render(correcao, True, verde)
                    textolugar0 = textof0.get_rect(center=(800 // 2, 300 // 2))
                    tela.blit(textof0, textolugar0)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    surface = pygame.display.set_mode((800, 600))
                    tela.fill(branco)
                    coisado = (coisado + 1) % len(coisas)
                    c = input_texto = ''

                if vidas == 0:
                    r = False

            elif event.key == K_BACKSPACE:
                input_texto = input_texto[:-1]
            else:
                input_texto += event.unicode

    foto = coisas[coisado]['imagem']
    tela.blit(foto, (500 // 2, 300 // 2))
    texto(input_texto, font0, preto, tela, 275, 530)
    pygame.display.flip()

tela.fill(branco)
texto(f'SUA PONTUAÇÃO: {pontos}', font0, preto, tela, 150, 250)

pygame.display.flip()
pygame.time.wait(1000)
pygame.quit()
