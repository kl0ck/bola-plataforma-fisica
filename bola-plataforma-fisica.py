import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bola e Plataforma")

# Define as cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Parâmetros da bola
raio = 20
bola_x = largura // 2
bola_y = altura // 2 - 100
velocidade_x = 0
velocidade_y = 0
gravidade = 0.5
velocidade_max_y = 10

# Parâmetros da plataforma
plat_largura = 200
plat_altura = 10
plat_x = (largura - plat_largura) // 2
plat_y = altura // 2

# Loop principal
executando = True
relogio = pygame.time.Clock()

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Controle da bola pelas setas do teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        velocidade_x = -5
    elif teclas[pygame.K_RIGHT]:
        velocidade_x = 5
    else:
        velocidade_x = 0

    # Atualiza a posição da bola
    bola_x += velocidade_x

    # Aplica gravidade
    velocidade_y += gravidade
    if velocidade_y > velocidade_max_y:
        velocidade_y = velocidade_max_y
    bola_y += velocidade_y

    # Checa colisão com a plataforma
    if (plat_x <= bola_x <= plat_x + plat_largura) and (plat_y <= bola_y + raio <= plat_y + plat_altura):
        bola_y = plat_y - raio
        velocidade_y = 0

    # Checa colisão com o chão
    if bola_y + raio >= altura:
        bola_y = altura - raio
        velocidade_y = 0

    # Limpa a tela
    tela.fill(preto)

    # Desenha a bola
    pygame.draw.circle(tela, vermelho, (int(bola_x), int(bola_y)), raio)

    # Desenha a plataforma
    pygame.draw.rect(tela, branco, (plat_x, plat_y, plat_largura, plat_altura))

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de atualização
    relogio.tick(60)

pygame.quit()
