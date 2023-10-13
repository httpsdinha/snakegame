import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura, altura = 400, 400
tamanho_cobra = 20
velocidade = 15

# Cores
cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)
cor_texto = (255, 255, 255)

# Tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Função para desenhar a cobra
def desenhar_cobra(cobra, tamanho_cobra):
    for segmento in cobra:
        pygame.draw.rect(tela, cor_cobra, [segmento[0], segmento[1], tamanho_cobra, tamanho_cobra])

# Função para exibir mensagem inicial
def mensagem_inicial():
    fonte = pygame.font.Font(None, 36)
    mensagem = fonte.render("Pressione qualquer tecla para começar", True, cor_texto)
    tela.blit(mensagem, (50, altura // 2))
    pygame.display.update()

# Função para exibir pontuação
def mostrar_pontuacao(pontos):
    fonte = pygame.font.Font(None, 24)
    texto = fonte.render("Pontuação: " + str(pontos), True, cor_texto)
    tela.blit(texto, (10, 10))

# Função para mostrar a tela de game over
def tela_game_over(pontos):
    fonte = pygame.font.Font(None, 36)
    mensagem = fonte.render("Fim de jogo. Pontuação: " + str(pontos), True, cor_texto)
    tela.blit(mensagem, (50, altura // 2))
    pygame.display.update()
    pygame.time.delay(2000)  # Aguarda 2 segundos antes de fechar o jogo
    pygame.quit()
    sys.exit()

# Função principal
def jogo():
    cobra = [[largura // 2, altura // 2]]
    direcao = "direita"
    comida = [random.randrange(1, (largura//tamanho_cobra)) * tamanho_cobra,
              random.randrange(1, (altura//tamanho_cobra)) * tamanho_cobra]
    pontos = 0
    jogo_iniciado = False
    jogo_encerrado = False

    while not jogo_encerrado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_encerrado = True
            elif evento.type == pygame.KEYDOWN:
                if not jogo_iniciado:
                    jogo_iniciado = True
                if evento.key == pygame.K_UP and direcao != "baixo":
                    direcao = "cima"
                if evento.key == pygame.K_DOWN and direcao != "cima":
                    direcao = "baixo"
                if evento.key == pygame.K_LEFT and direcao != "direita":
                    direcao = "esquerda"
                if evento.key == pygame.K_RIGHT and direcao != "esquerda":
                    direcao = "direita"

        if jogo_encerrado:
            continue

        if not jogo_iniciado:
            tela.fill(cor_fundo)
            mensagem_inicial()
            pygame.display.update()
            continue  # Aguardar até que o jogo seja iniciado

        if direcao == "cima":
            cobra[0][1] -= tamanho_cobra
        if direcao == "baixo":
            cobra[0][1] += tamanho_cobra
        if direcao == "esquerda":
            cobra[0][0] -= tamanho_cobra
        if direcao == "direita":
            cobra[0][0] += tamanho_cobra

        if (cobra[0][0] < 0 or cobra[0][0] >= largura or cobra[0][1] < 0 or cobra[0][1] >= altura or
                cobra[0] in cobra[1:]):
            jogo_encerrado = True

        tela.fill(cor_fundo)
        desenhar_cobra(cobra, tamanho_cobra)
        pygame.draw.rect(tela, cor_comida, [comida[0], comida[1], tamanho_cobra, tamanho_cobra])

        if cobra[0] == comida:
            comida = [random.randrange(1, (largura // tamanho_cobra)) * tamanho_cobra,
                      random.randrange(1, (altura // tamanho_cobra)) * tamanho_cobra]
            pontos += 1

        mostrar_pontuacao(pontos)
        pygame.display.update()
        pygame.time.Clock().tick(velocidade)

    tela_game_over(pontos)

jogo()
