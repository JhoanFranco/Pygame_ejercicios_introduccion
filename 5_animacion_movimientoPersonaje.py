
import pygame as pg

# Incializar
pg.init()

# Pantalla (ventana)
ancho, altura = 1000, 600
pantalla = pg.display.set_mode((ancho, altura))
pg.display.set_caption("exterminador")
#aqui icono pero se necesita imagen 32*32px

# Fondo del juego 
fondo = pg.image.load("imagenes/fondo_desierto_noche.JPEG")

quieto_imagenes = [pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_1.png")     
         ]

correr_derecha_imagenes = [pg.image.load("imagenes/exterminador/Gunner_Blue_Run_1.png"),
                  pg.image.load("imagenes/exterminador/Gunner_Blue_Run_2.png"),
                  pg.image.load("imagenes/exterminador/Gunner_Blue_Run_3.png"),
                  pg.image.load("imagenes/exterminador/Gunner_Blue_Run_4.png"),
                  pg.image.load("imagenes/exterminador/Gunner_Blue_Run_5.png"),
                  pg.image.load("imagenes/exterminador/Gunner_Blue_Run_6.png")
                 ]

correr_izquierda_imagenes = [pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_1.png"),
                    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_2.png"),
                    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_3.png"),
                    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_4.png"),
                    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_5.png"),
                    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_6.png")
                    ]

salto_imagenes = [pg.image.load("imagenes/exterminador/Gunner_Blue_Jump_1.png"),
        pg.image.load("imagenes/exterminador/Gunner_Blue_Jump_2.png")
        ]

agacharse_imagenes = [pg.image.load("imagenes/exterminador/Gunner_Blue_Crouch_1.png"),
             pg.image.load("imagenes/exterminador/Gunner_Blue_Crouch_2.png"),
             pg.image.load("imagenes/exterminador/Gunner_Blue_Crouch_3.png")
            ]


x = 0 # para el contador de movimiento del fondo
px = 50
py = 200
ancho_x = 40
velocidad=  10

#control de FPS 
reloj = pg.time.Clock()

#variable salto
salto = False
bajar = False
contadorSalto = 10

# variables direccion
izquierda = False
derecha = False
cuentaSalto = 0
cuentaPasos = 0

# movimiento
def recargaPantalla():
    global cuentaPasos
    global cuentaSalto
    global x

    # fondo en movimiento

    x_relativa = x % fondo.get_rect().width
    pantalla.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < ancho:
        pantalla.blit(fondo, (x_relativa, 0))
    x -= 5

    #contador de pasos #SON  IF PORQUE SE REPRODUCEN EN BUCLE
    if cuentaPasos + 1 >=6: # como las animaciones son 6
        cuentaPasos = 0
    if cuentaSalto + 1 >= 2:
        cuentaSalto = 0
        cuentaPasos = 0
    # movimiento derecha
    if derecha == True:
        # pantalla.blit(fondo, bordes) 
        pantalla.blit(correr_derecha_imagenes[cuentaPasos], (int(px), int(py)))
        cuentaPasos += 1
    # movimiento izquierda
    elif izquierda == True:
        pantalla.blit(correr_izquierda_imagenes[cuentaPasos] ,(int(px), int(py)))
        cuentaPasos += 1
    # para saltos
    elif salto == True:
        pantalla.blit(salto_imagenes[cuentaSalto], (int(px), int(py)))
        cuentaSalto += 1
    # cuando no hace ningun movimiento
    else:
        pantalla.blit(quieto_imagenes[0],(int(px), int(py)) )


ejecuta = True
while ejecuta:
    #controlo FPS
    reloj.tick(18)

    #Bucle Juego
    for event in pg.event.get():
        if event.type == pg.QUIT:
            ejecuta = False

    #opcion tecla pulsada
    keys = pg.key.get_pressed()

    # cuando presiona a - izquierda
    if keys[pg.K_a] and px > velocidad:# px > 10
        px -= velocidad
        izquierda = True
        derecha = False
        # print("izquierda ", px, py)
    # cuando presiona d - derecha
    elif keys[pg.K_d] and px < 900 - velocidad - ancho_x: # px < 850
        px += velocidad
        izquierda = False
        derecha = True
        # print("derecha ", px, py)
    # cuando presiona w-  hacia arriba
    elif keys[pg.K_w] and py > 100: # py comienza en 300 y va bajando
        py -= velocidad # al poner borde negativo la imagen sube
        salto = True
        # print("arriba", px, py)
    # cuando presiona s hacia abajo
    elif keys[pg.K_s] and py < 300: # py no puede  ser mayor que 300 
        py += velocidad # al poner borde positivo la imagen baja
        salto = False
        # print("abajo", px , py)
    else: #personaje quieto
        izquierda = False
        derecha = False
        salto = False
        # print("quieto", px, py)

    # Actualización de la ventana
    pg.display.update()
    # llamar la actualizacion de la ventana
    recargaPantalla()

pg.quit()

