import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake Elegante")

# Colores
COLOR_FONDO = (30, 30, 30)
COLOR_SERPIENTE = (0, 255, 127)
COLOR_COMIDA = (255, 69, 0)
COLOR_TEXTO = (255, 255, 255)

# Configuración de la serpiente
tamaño_bloque = 20
velocidad = 15

reloj = pygame.time.Clock()

# Fuente para el texto
fuente = pygame.font.SysFont('Arial', 30)

def mostrar_puntuacion(puntuacion):
    texto = fuente.render(f"Puntuación: {puntuacion}", True, COLOR_TEXTO)
    ventana.blit(texto, [10, 10])

def dibujar_serpiente(lista_serpiente):
    for bloque in lista_serpiente:
        pygame.draw.rect(ventana, COLOR_SERPIENTE, [bloque[0], bloque[1], tamaño_bloque, tamaño_bloque])

def mensaje_final(texto):
    mensaje = fuente.render(texto, True, COLOR_TEXTO)
    ventana.blit(mensaje, [ancho//2 - 120, alto//2 - 20])
    pygame.display.update()

def juego():
    game_over = False
    game_close = False

    x_serpiente = ancho // 2
    y_serpiente = alto // 2
    dx = 0
    dy = 0

    lista_serpiente = []
    longitud_serpiente = 1

    comida_x = round(random.randrange(0, ancho - tamaño_bloque) / tamaño_bloque) * tamaño_bloque
    comida_y = round(random.randrange(0, alto - tamaño_bloque) / tamaño_bloque) * tamaño_bloque

    while not game_over:
        while game_close:
            ventana.fill(COLOR_FONDO)
            mensaje_final("Game Over! Presiona Espacio para jugar de nuevo o Esc para salir")
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx != tamaño_bloque:
                    dx = -tamaño_bloque
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx != -tamaño_bloque:
                    dx = tamaño_bloque
                    dy = 0
                elif event.key == pygame.K_UP and dy != tamaño_bloque:
                    dy = -tamaño_bloque
                    dx = 0
                elif event.key == pygame.K_DOWN and dy != -tamaño_bloque:
                    dy = tamaño_bloque
                    dx = 0

        if x_serpiente >= ancho or x_serpiente < 0 or y_serpiente >= alto or y_serpiente < 0:
            game_close = True

        x_serpiente += dx
        y_serpiente += dy

        ventana.fill(COLOR_FONDO)
        pygame.draw.rect(ventana, COLOR_COMIDA, [comida_x, comida_y, tamaño_bloque, tamaño_bloque])
        
        cabeza_serpiente = []
        cabeza_serpiente.append(x_serpiente)
        cabeza_serpiente.append(y_serpiente)
        lista_serpiente.append(cabeza_serpiente)
        
        if len(lista_serpiente) > longitud_serpiente:
            del lista_serpiente[0]

        for bloque in lista_serpiente[:-1]:
            if bloque == cabeza_serpiente:
                game_close = True

        dibujar_serpiente(lista_serpiente)
        mostrar_puntuacion(longitud_serpiente - 1)
        
        pygame.display.update()

        if x_serpiente == comida_x and y_serpiente == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_bloque) / tamaño_bloque) * tamaño_bloque
            comida_y = round(random.randrange(0, alto - tamaño_bloque) / tamaño_bloque) * tamaño_bloque
            longitud_serpiente += 1

        reloj.tick(velocidad)

    pygame.quit()
    quit()

juego()