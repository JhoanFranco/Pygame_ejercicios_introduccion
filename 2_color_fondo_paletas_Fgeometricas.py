import pygame as pg
import sys

#inicializar pygame
pg.init()

#Creacion de pantalla
ventana = pg.display.set_mode((500, 400))

#Especificacion del titulo
pg.display.set_caption("Mi primer juego :D")

pantalla = pg.display.get_surface()

# Crear una paleta de colores con (RGB)
blanco = (255, 255, 255)
negro = (0,0,0)
rojo = (255, 0 ,0 )
verde = (0 , 255, 0)
azul = (0, 0, 255)
HC74225 = (199, 66, 37)
H61CD35 = (97, 205, 53)

#Fondo de pantalla del juego 
pantalla.fill(rojo)

#Dibujar figura geometricas
    #Rectangulo
pg.draw.rect(pantalla, blanco, (100, 50, 100, 50) )
    #linea
pg.draw.line(pantalla, negro, (100, 104), (199, 104), 2)# cordenada1 coredenada2, ancho
    #elipse
pg.draw.ellipse(pantalla, H61CD35,(275, 200, 40, 200), 2)# rect = (x , y, tamañoXancho, tamañoYlargo), ancholinea
    # poligono
puntos= [(100, 300), (100 ,100), (150, 100)]
pg.draw.polygon(pantalla, azul, puntos, width=5) # Funciona el plano como un cuadrante(4) pero de solo positivos
    #Ojo uno los puntos faltantes de (150,100) lo unio con(100,300)

    
#¿Qué es la superpoción?
    # es cuando se pone primero el fondo y despues
    # los detalles mas pequeños (programacion del pintor)

pg.display.flip() # actualizar la pantalla

#Bucle de ejecucion
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
