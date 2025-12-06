# Importando a biblioteca pygame
import pygame
import os
import sys

# Desenhando formas na tela
def desenhar_formas_geometricas(tela, circ_x, circ_y, circ_raio, rect_x, rect_y, rect_largura, rect_altura, vidas, tempo_protecao_ativo):
    
    # Desenhando formas geométricas com parâmetros dinâmicos
    
    VERDE = (0,255,0)
    VERMELHO = (255,0,0)
    BRANCO = (255,255,255)
    AZUL = (100,100,255)

    # Retângulo obstáculo
    pygame.draw.rect(tela, VERDE, (rect_x, rect_y, rect_altura, rect_altura), 0)
    
    # Círculo controlável (azul se protegido, vermelho se vulnerável)
    cor_circulo = AZUL if tempo_protecao_ativo else VERMELHO
    pygame.draw.circle(tela, cor_circulo, (circ_x, circ_y), circ_raio, 0)
    
    # Linha divisória
    pygame.draw.line(tela, BRANCO, (50,200),(750,200),3)
    
    # Borda branca quando protegido
    if tempo_protecao_ativo:
        pygame.draw.circle(tela, BRANCO, (circ_x, circ_y), circ_raio, 3)
    
    # Exibindo uma imagem na tela
    def exibir_imagem_externa(tela, imagem, posicao):
        BRANCO = (255, 255, 255)
        tela.blit(imagem, posicao)
        rect = imagem.get_rect(topleft=posicao)
        pygame.draw.rect(tela, BRANCO, rect, 2)
    
    # Exibindo texto na tela usando uma fonte
    def exibir_texto_com_fonte(tela, texto, posicao, cor = (255, 255, 255), tamanho_fonte=36):
        fonte = pygame.font.SysFont(None, tamanho_fonte)
        texto_renderizado = fonte.render(texto, True, cor)
        tela.blit(texto_renderizado, posicao)
    
    # Movendo círculo com as teclas WASD ou setas
    def mover_circulo_com_teclado(teclas, x, y, velocidade, limite_tela, raio):   
        if teclas[pygame.K_w] or teclas.K_UP:
            y -= velocidade
        if teclas[pygame.K_s] or teclas.K_DOWN:
            y += velocidade
        if teclas[pygame.K_a] or teclas.K_LEFT:
            x -= velocidade
        if teclas[pygame.K_d] or teclas.K_RIGHT:
            x += velocidade
    
        # Lmimitando movimentos dentro da tela
        x = max(raio, min(x, limite_tela[0]-raio))
        y = max(raio, min(x, limite_tela[0]-raio))
    
        return x, y

# Verificando colisão entre círculo e retângulo
def verificar_colisao_circulo_retangulo(circ_x, circ_y, circ_raio, rect_x, rect_y, rect_largura, rect_altura):
    
    # Ponto mais próximo do círculo dentro do retângulo
    ponto_x = max(rect_x, min(circ_x, rect_x + rect_largura))
    ponto_y = max(rect_y, min(circ_y, rect_y + rect_largura))
    
    # Distância ao quadrado entre círculo dentro do retângulo
    distancia_x = circ_x - ponto_x
    distancia_y = circ_x - ponto_y
    
    # Comparando com raio ao quadrado (evita cálculo de raiz quadrada)
    return(distancia_x * distancia_x + distancia_y * distancia_y) <= (circ_raio * circ_raio)

# Atualizando o sistema de vidas quando há colisão
def atualizar_sistema_vidas(colidiu, vidas_atual, tempo_atual, ultima_colisao, tempo_protecao):
    if colidiu and (tempo_atual - ultima_colisao > tempo_protecao):
        return max(0, vidas_atual -1), tempo_atual
    return vidas_atual, ultima_colisao

def main():
    
    # Inicializando
    pygame.init()
    
    # Configurando a tela
    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("PyGame: Movimento, Colisão e Vidas")