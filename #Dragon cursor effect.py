import pygame
import math
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dragon Cursor Effect")

# Cores
BACKGROUND_COLOR = (60, 97, 153)

# Carrega a imagem do dragão localmente
dragon_image = pygame.image.load("drangon.png").convert_alpha()

# Parâmetros do dragão
N = 40
elems = [{'x': width // 2, 'y': height // 2} for _ in range(N)]
pointer = {'x': width // 2, 'y': height // 2}
rad = 0
frm = 0

# Função para desenhar o dragão
def draw_dragon():
    for i in range(N):
        elem = elems[i]
        size = (162 + 4 * (1 - i)) / 50
        scaled_image = pygame.transform.scale(dragon_image, (int(size * 50), int(size * 50)))  # Ajuste o tamanho conforme necessário
        screen.blit(scaled_image, (elem['x'] - scaled_image.get_width() // 2, elem['y'] - scaled_image.get_height() // 2))

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            pointer['x'], pointer['y'] = event.pos

    screen.fill(BACKGROUND_COLOR)

    # Atualiza a posição do dragão
    e = elems[0]
    ax = (math.cos(3 * frm) * rad * width) / height
    ay = (math.sin(4 * frm) * rad * height) / width
    e['x'] += (ax + pointer['x'] - e['x']) / 10
    e['y'] += (ay + pointer['y'] - e['y']) / 10

    for i in range(1, N):
        ep = elems[i - 1]
        a = math.atan2(elems[i]['y'] - ep['y'], elems[i]['x'] - ep['x'])
        elems[i]['x'] += (ep['x'] - elems[i]['x'] + (math.cos(a) * (100 - i)) / 5) / 4
        elems[i]['y'] += (ep['y'] - elems[i]['y'] + (math.sin(a) * (100 - i)) / 5) / 4

    if rad < min(pointer['x'], pointer['y']) - 20:
        rad += 1

    frm += 0.003
    if rad > 60:
        pointer['x'] += (width / 2 - pointer['x']) * 0.05
        pointer['y'] += (height / 2 - pointer['y']) * 0.05

    draw_dragon()
    pygame.display.flip()
    pygame.time.delay(16)  # Aproximadamente 60 FPS
