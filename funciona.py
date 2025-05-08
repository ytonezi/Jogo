import pygame
import sys
from pygame.locals import *

pygame.init()

pygame.mixer.music.set_volume(5)
musica_de_fundo = pygame.mixer.music.load('So.mp3')
pygame.mixer.music.play(-1)

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('EI! VOCÊ SABE O NOME DESSA IMAGEM?')

branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)

font = pygame.font.SysFont('Comic Sans MS', 35)
font0 = pygame.font.SysFont('Comic Sans MS', 50)
font1 = pygame.font.SysFont('Comic Sans MS', 20)

moldurap = 550
molduraq = 380
mx = (400 - moldurap // 2)
my = (300 - molduraq // 2)

moldurag = 400
moldurah = 90
mg = (400 - moldurag // 2)
mh = (550 - moldurah // 2)

coisas = [
    {'nome': 'cachorro', 'imagem': 'cachorro.png'},
    {'nome': 'bolo', 'imagem': 'bolo.png'},
    {'nome': 'borboleta', 'imagem': 'borboleta.png'},
    {'nome': 'casa', 'imagem': 'casa.png'},
    {'nome': 'estrela', 'imagem': 'estrela.png'},
    {'nome': 'cogumelo', 'imagem': 'cogumelo.png'},
    {'nome': 'flor', 'imagem': 'flor.png'},
    {'nome': 'carro', 'imagem': 'carro.png'},
    {'nome': 'gato', 'imagem': 'gato.png'}
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
estado = 'inicio'

while True:
    tela.fill(branco)

    if estado == 'inicio':
        texto('APERTE START PARA COMEÇAR', font, preto, tela, 135, 250)
        start = pygame.Rect(300, 400, 200, 50)
        pygame.draw.rect(tela, verde, start)
        texto(' START', font, preto, tela, 325, 400)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if start.collidepoint(event.pos):
                    estado = 'jogo'

    elif estado == 'jogo':
        pygame.draw.rect(tela, preto, (mx, my, moldurap, molduraq), 3)
        pygame.draw.rect(tela, preto, (mg, mh, moldurag, moldurah), 3)
        texto('ACERTE O NOME DA IMAGEM!', font, preto, tela, 120, 1)
        texto(f'VIDAS RESTANTES: {vidas}', font1, preto, tela, 285, 50)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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
                        input_texto = ''
                        coisado = (coisado + 1) % len(coisas)
                    else:
                        vidas -= 1
                        correcao = coisas[coisado]['nome']
                        textof0 = font0.render(correcao, True, verde)
                        textolugar0 = textof0.get_rect(center=(800 // 2, 600 // 2))
                        tela.blit(textof0, textolugar0)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        tela.fill(branco)
                        surface = pygame.display.set_mode((800, 600))
                        coisado = (coisado + 1) % len(coisas)
                        input_texto = ''
                    if vidas == 0:
                        estado = 'fim'
                elif event.key == K_BACKSPACE:
                    input_texto = input_texto[:-1]
                else:
                    input_texto += event.unicode

        foto = coisas[coisado]['imagem']
        tela.blit(foto, (440 // 2, 250 // 2))
        texto(input_texto, font0, preto, tela, 275, 520)

    elif estado == 'fim':
        tela.fill(branco)
        texto(f'SUA PONTUAÇÃO: {pontos}', font0, preto, tela, 150, 250)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()
