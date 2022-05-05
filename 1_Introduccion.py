#4.1 importar modulos
#py -m pip install -U pygame --user
import pygame , sys, os

#4.2 inicializar pygame (6 modulos)
pygame.init()

##4.3 Arreglar la pantalla
# areglar la pantalla 468 de ancho y 600 de largo
window = pygame.display.set_mode((468,600))

#Caption(subtitulo de la pantalla)
pygame.display.set_caption("monkey fever")

# finalmente se obtine la pantalla
screen = pygame.display.get_surface()
 
## 4.4 contruir el nombre del archivo

# #Crea un relativo nombreRuta para un archivo
# monkey_head_file_name = os.path.join("data","chimp.bmp")
# print(monkey_head_file_name)# data\chimp.bmp

monkey_surface = pygame.image.load("mono.PNG") # la imagen debe estar cargada en el mismo lugar del archivo

#Dibujar el mono en la pantalla
screen.blit(monkey_surface, (0,0))

#Actualizar toda la pantalla
pygame.display.flip()

#Añadir una forma de salir

def input(events):
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit(0)
        else:
            print(event)

# un evento son como acciones hechas por el usuario mover el mouse
#    una tecla, joystick  

#Una vez el evento terminar  el programa sale cerrando la ventana
#o presionando Alt + F4

while True:
    input(pygame.event.get())