# importación de paquetes
import pygame 
import sys

# Inicialización de Pygame
pygame.init()

#Creacion de pantalla
ventana = pygame.display.set_mode((1000, 400))

#Especificacion del titulo
pygame.display.set_caption("juegoVaquero")


pantalla = pygame.display.get_surface()



#Imagen de fondo
fondo = pygame.image.load("imagenes/fondo_desierto_montañoso.JPEG")

    #donde debe mostrar la imagen blit == draw
pantalla.blit(fondo,(-100,0)) # imagen, (0,0) no margenes

## PARA REDIMENSIONAR CON Pygame
# anchoDeseado = 1000
# altoDeseado = 400
# imagenOriginal = pygame.image.load("imagenes/fondo_desierto_noche.JPEG") # 1300 * 774 px
# imagenRedimensionada = pygame.transform.scale(imagenOriginal, (anchoDeseado, altoDeseado))

# pantalla.blit(imagenRedimensionada, (0,0))


#Añadir icono 
icono = pygame.image.load("imagenes/icon_vaquero.png") # maximo 32 *32 pixel
pygame.display.set_icon(icono)



# Bucle de ejecución
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()