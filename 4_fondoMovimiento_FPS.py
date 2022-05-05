# import pygame, sys

# #para modificar los valores de pantalla(variables)

# valores_pantalla = [1000, 600]
# pantalla = pygame.display.set_mode((valores_pantalla[0], valores_pantalla[1]))

# # # Optimizar imagenes-- Fondo del juego
# # fondo = pygame.image.load("imagenes/fondo_desierto_noche.png").convert()  #convert es para un menor consumo de recursos
# # pantalla.blit(fondo, (0,0))# 0 margenes

# #FONDO EN MOVIMIENTO
# fondo = pygame.image.load("imagenes/fondo_desierto_noche.jpeg").convert()
# x = 0  # margenes
# y = 0  # margenes 

# # #bucle del juego(parte de movimiento fondo- entender los calculos(hacer control + K + U)[borra_comentarios])
# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()
# #     #para que la pantalla se mueva
# #     # print(fondo.get_rect().width) # 1024
# #     x_relativa = x % fondo.get_rect().width # fondo.get_rect().width= obtener el ancho del fondo 
# #     # print(x_relativa) # va desde 1024, 1023,.. cuando llega a hay entonces el residuo vuelve 0 (-1024) % 1024 = 0) y sigue el ciclo
# #     pantalla.blit(fondo, (x_relativa - fondo.get_rect().width , y))
# #                           # mueve la pantalla de 1024, 1023 .. 0 vuele y repite el ciclo 1024
# #                           # un movimiento ciclico hacia la derecha          
# #     x -= 1 # +1 izq , -1 der
# #     pygame.display.update()

# # bucle del juego
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     # fondo movimiento 
#     x_relativa = x % fondo.get_rect().width
#     pantalla.blit(fondo, (x_relativa - fondo.get_rect().width, y))

#     print(f"x = {x}")
#     print(f"x_relativa = {x_relativa}")
#     print(f" x_relativa - fondo.get_rect().width = {x_relativa - fondo.get_rect().width}")

#     #sobre poner otra imagen para llenar el vacio que se deja(al principio es pequeño pero despues grande y sigue el ciclo)
#     if x_relativa < valores_pantalla[0]:
#         pantalla.blit(fondo, (x_relativa, 0))
#     x -= 1
#     pygame.display.update()

#--------------------------------------------------------
# Frames
import pygame, sys

valores_pantalla = [1000, 600]
pantalla = pygame.display.set_mode((valores_pantalla[0], valores_pantalla[1]))
FPS = 60
RELOJ = pygame.time.Clock()

#FONDO EN MOVIMIENTO
fondo = pygame.image.load("imagenes/fondo_desierto_noche.jpeg").convert()
x = 0  # margenes
y = 0  # margenes 

# bucle del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # fondo movimiento 
    x_relativa = x % fondo.get_rect().width
    pantalla.blit(fondo, (x_relativa - fondo.get_rect().width, y))

    #sobre poner otra imagen para llenar el vacio que se deja(al principio es pequeño pero despues grande y sigue el ciclo)
    if x_relativa < valores_pantalla[0]:
        pantalla.blit(fondo, (x_relativa, 0))
    x -= 1
    # control de FPS
    RELOJ.tick(FPS)     #This can be used to help limit the runtime speed of a game. By calling Clock.tick(40) once per frame, the program will never run at more than 40 frames per second.
    #Actualizacion de la ventana
    pygame.display.update()

