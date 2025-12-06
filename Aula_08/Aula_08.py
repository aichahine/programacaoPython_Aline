# Importando a biblioteca pygame
import pygame
import os
import sys

# Desenhando formas na tela
def desenhar_formas_geometricas(tela):
    BRANCO = (255,255,255)
    VERMELHO = (255,0,0)
    VERDE = (0,255,0)

    # Criando um círculo preenchido na cor vermelha
    pygame.draw.circle(tela,VERMELHO, (400,100),50,0)

    # Criando um retângulo
    pygame.draw.rect(tela,VERDE, (50,50,200,100),0)

    # Criando uma linha - o último parâmetro define a espessura
    pygame.draw.line(tela,BRANCO, (50,20),(750,200), 1)

    # Criando um polígono
    pygame.draw.polygon(tela, BRANCO, [(600, 500), (750, 550), (550, 550)], 0)

# Exibindo uma imagem na tela
def exibir_imagem_externa(tela, imagem, posicao):
    BRANCO = (255,255,255)
    tela.blit(imagem, posicao)
    rect = imagem.get_rect(topleft=posicao)
    pygame.draw.rect(tela, BRANCO, rect, 2)

# Inicializando a biblioteca pygame
def main():

    pygame.init()

    # Definindo o tamanho da tela
    # Constantes sempre com letras maiúsculas
    LARGURA = 800
    ALTURA = 600

    # O método recebe as constantes que foram definidas para as dimensões da tela
    tela = pygame.display.set_mode((LARGURA,ALTURA))

    # Definindo o título da tela
    pygame.display.set_caption("Minha primeira tela de jogo")

    # Definindo as cores do jogo (neste caso, são tuplas = imutáveis, separadas por vírgulas)
    PRETO = (0,0,0)
    BRANCO = (255,255,255)
    VERMELHO = (255,0,0)
    VERDE = (0,255,0)
    AZUL = (0,0,255)
    AMARELO = (255,255,0)

    # Uma constante recebendo outra constante para que não seja modificada, definindo a cor de fundo
    COR_FUNDO = AZUL

    # Carregando imagem externa
    try:
        imagem = pygame.image.load("sprite.png")
        imagem = pygame.transform.scale(imagem, (150,150))
    except:
        print("Criando outra imagem")
        imagem = pygame.surface((150,150))
        imagem.fill(AMARELO)
         # Criando um círculo preenchido na cor vermelha
        pygame.draw.circle(tela,VERMELHO, (400,100),50,0)

        # Criando um retângulo
        pygame.draw.rect(tela,VERDE, (50,50,200,100),0)

    # Criando o loop principal do jogo
    executando = True
    # Taxa de atualização (FPS)
    relogio = pygame.time.Clock()

    # Controlando a taxa de atualização (60 frames por segundo)
    while executando:
        relogio.tick(60)

        # Processando os eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: # Configurando Exit
                executando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE: # Configurando a ação da tecla Esc
                    executando = False
                # Mudando as cores de fundo com as teclas
                elif evento.key == pygame.K_r:
                    COR_FUNDO = BRANCO
                elif evento.key == pygame.K_g:
                    COR_FUNDO = AMARELO
                elif evento.key == pygame.K_b:
                    COR_FUNDO = VERDE
        
        # Atualização da lógica do jogo
        
        # -----------------------------
        
        # Rendericação da tela do jogo
        tela.fill(COR_FUNDO)

        desenhar_formas_geometricas(tela)

        exibir_imagem_externa(tela, imagem)

        # Atualização da tela
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()