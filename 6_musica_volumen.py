import pygame as pg
import sys
#inicializacion de pygame
pg.init()
# pantalla
W,H = 1000, 600 
pantalla =pg.display.set_mode((W, H))
pg.display.set_caption("exterminador")
#icono = pg.image.load("")#poner icono

#color pantalla
color = (255,255,255)
pantalla.fill(color)
pg.display.flip()

#fondo del juego
#fondo = pg.image.load("imagenes/")# cargar
#MUSICA DE FONDO
pg.mixer.music.load("musica/musica-esther-garcia-indomitable.mp3")# cargar musica python
# reproducir la musica 
pg.mixer.music.play(-1) # se reproduce segun el numero -- (-1) es un bucle infinito

# CARGAR IMAGENES SONIDO
sonido_bajar = pg.image.load("imagenes/sonido/bajar_volumen.png")
sonido_subir= pg.image.load("imagenes/sonido/subir_volumen.png")
sonido_maximo = pg.image.load("imagenes/sonido/maximo_volumen.png")
sonido_nulo = pg.image.load("imagenes/sonido/silenciar_volumen.png")

reloj = pg.time.Clock()

ejecuta = True
while ejecuta:
  # FPS
  reloj.tick(18)
  for event in pg.event.get():
    if event.type == pg.QUIT:
      ejecuta = False
      
  # Opción tecla pulsada
  keys = pg.key.get_pressed()

  #CONTROL DE SONIDO
  volumen_actual = pg.mixer.music.get_volume()

  #baja volumen
  if keys[pg.K_1] and volumen_actual > 0.0: # 0.0 volumen nulo
    pg.mixer.music.set_volume(volumen_actual - 0.01) # para colocar o cambiar el volumen
    pantalla.blit(sonido_bajar,(850,30))
  elif keys[pg.K_1] and volumen_actual == 0.0:
    pantalla.blit(sonido_bajar,(850,30))
  
  #sube volumen
  if keys[pg.K_2] and volumen_actual < 1.0: # 1.0 maximo volumen
    pg.mixer.music.set_volume(volumen_actual + 0.01)
    pantalla.blit(sonido_subir,(850,30))
  elif keys[pg.K_2] and volumen_actual == 0.0:
    pantalla.blit(sonido_subir,(850,30))

  # volumen nulo
  elif keys[pg.K_3]:
    pg.mixer.music.set_volume(0.0)
    pantalla.blit(sonido_nulo, (850,30))
  # volumen maximo
  elif keys[pg.K_4]:
    pg.mixer.music.set_volume(1.0)
    pantalla.blit(sonido_maximo,(850,30))# 850,30


  #JJAJAJAJAJAJ HAY QUE BUSCAR MEJORES IMAGENES QUE SEAN IGUALES DE TAMAÑO Y COLOR, PARA cuando se pongan una sobre la otra no se  vea asi de feo  
  #actualizar pantalla
  pg.display.flip()  
  print(volumen_actual)
pg.quit()
  