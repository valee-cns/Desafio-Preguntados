import pygame
from cosas import *
from datos import *

preguntas = []
respuestas_a = []
respuestas_b = []
respuestas_c = []
respuestas_correcta = []
posicion = 0
posicion_respuestas = 0
mensaje = "Cliquee el botón Pregunta :)"
mensaje2 = "Incorrecto, no suma score :("
puntos = 0
mostrar_pregunta = False
error = 0


for dato in lista:
    preguntas.append(dato["pregunta"])
    respuestas_a.append(dato["a"])
    respuestas_b.append(dato["b"])
    respuestas_c.append(dato["c"])
    respuestas_correcta.append(dato["correcta"])

pygame.init()

# Defino la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
pygame.display.set_caption("Preguntados")

# Defino la imágen
imagen_logo = pygame.image.load("logo.png")
imagen_logo = pygame.transform.scale(imagen_logo, (TAMAÑO_LOGO,TAMAÑO_LOGO))

# Defino el texto
fuente = pygame.font.SysFont("Sitka", 30)
fuente2 = pygame.font.SysFont("Sitka", 22)
la_pregunta = fuente2.render("", True, NEGRO)
rta_a = fuente.render("", True, NEGRO)
rta_b = fuente.render("", True, NEGRO)
rta_c = fuente.render("", True, NEGRO)
comenzar = fuente2.render(mensaje, True,NEGRO)
score = fuente.render(str("Score: {0}".format(puntos)), True,NEGRO)
incorrecto = fuente2.render("", True,NEGRO)

run = True

while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
    
        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = list(evento.pos)

            if (click[0] > 600 and click[0] < 750) and (click[1] > 25 and click[1] < 75):
                if posicion >= 17:
                    la_pregunta = fuente2.render("", True, NEGRO)
                    rta_a = fuente.render("", True, NEGRO)
                    rta_b = fuente.render("", True, NEGRO)
                    rta_c = fuente.render("", True, NEGRO)
                    comenzar = fuente2.render(mensaje, True,NEGRO)
                    incorrecto = fuente2.render("", True,NEGRO)
                    mostrar_pregunta = False
                    error = 0
                    posicion_respuestas = 0
                
                else:
                    la_pregunta = fuente2.render(str(preguntas[posicion]), True, NEGRO)
                    rta_a = fuente.render(str(respuestas_a[posicion]), True, NEGRO)
                    rta_b = fuente.render(str(respuestas_b[posicion]), True, NEGRO)
                    rta_c = fuente.render(str(respuestas_c[posicion]), True, NEGRO)
                    comenzar = fuente2.render("", True,NEGRO)
                    incorrecto = fuente2.render("", True,NEGRO)
                    mostrar_pregunta = True
                    error = 0
                
                if (posicion > len(preguntas)):
                    posicion = 0
                    la_pregunta = fuente2.render("", True, NEGRO)
                    rta_a = fuente.render("", True, NEGRO)
                    rta_b = fuente.render("", True, NEGRO)
                    rta_c = fuente.render("", True, NEGRO)
                    comenzar = fuente2.render(mensaje, True,NEGRO)
                    incorrecto = fuente2.render("", True,NEGRO)
                    mostrar_pregunta = False
                    error = 0
                    posicion_respuestas = 0

                else:
                    posicion += 1
                
            if (click[0] > 18 and click[0] < 168) and (click[1] > 425 and click[1] < 475):
                posicion = 0
                puntos = 0
                la_pregunta = fuente2.render("", True, NEGRO)
                rta_a = fuente.render("", True, NEGRO)
                rta_b = fuente.render("", True, NEGRO)
                rta_c = fuente.render("", True, NEGRO)
                comenzar = fuente2.render(mensaje, True,NEGRO)
                score = fuente.render(str("Score: {0}".format(puntos)), True,NEGRO)
                incorrecto = fuente2.render("", True,NEGRO)
                mostrar_pregunta = False
                error = 0
                posicion_respuestas = 0
            
            if mostrar_pregunta:
                if (click[0] > 300 and click[0] < 750) and (click[1] > 237 and click[1] < 287):
                    if 'a' == respuestas_correcta[posicion_respuestas]:
                        la_pregunta = fuente2.render("", True, NEGRO)
                        rta_a = fuente.render("", True, NEGRO)
                        rta_b = fuente.render("", True, NEGRO)
                        rta_c = fuente.render("", True, NEGRO)
                        comenzar = fuente2.render(mensaje, True,NEGRO)
                        puntos = puntos + 10

                        score = fuente.render(str("Score: {0}".format(puntos)), True,NEGRO)
                        posicion_respuestas += 1
                        mostrar_pregunta = False

                    elif 'a' != respuestas_correcta[posicion_respuestas]:
                        if error > 0:
                            rta_a = fuente.render("", True, NEGRO)
                            rta_b = fuente.render("", True, NEGRO)
                            rta_c = fuente.render("", True, NEGRO)
                            incorrecto = fuente2.render(mensaje2, True,NEGRO)
                            mostrar_pregunta = False
                            posicion_respuestas += 1
                        rta_a = fuente.render("", True, NEGRO)
                        error += 1

                if (click[0] > 300 and click[0] < 750) and (click[1] > 317 and click[1] < 367):
                        if 'b' == respuestas_correcta[posicion_respuestas]:
                            la_pregunta = fuente2.render("", True, NEGRO)
                            rta_a = fuente.render("", True, NEGRO)
                            rta_b = fuente.render("", True, NEGRO)
                            rta_c = fuente.render("", True, NEGRO)
                            comenzar = fuente2.render(mensaje, True,NEGRO)
                            puntos = puntos + 10

                            score = fuente.render(str("Score: {0}".format(puntos)), True,NEGRO)
                            posicion_respuestas += 1
                            mostrar_pregunta = False

                        elif 'b' != respuestas_correcta[posicion_respuestas]:
                            if error > 0:
                                rta_a = fuente.render("", True, NEGRO)
                                rta_b = fuente.render("", True, NEGRO)
                                rta_c = fuente.render("", True, NEGRO)
                                incorrecto = fuente2.render(mensaje2, True,NEGRO)
                                mostrar_pregunta = False
                                posicion_respuestas += 1
                            rta_b = fuente.render("", True, NEGRO)
                            error += 1


                if (click[0] > 300 and click[0] < 750) and (click[1] > 397 and click[1] < 447):
                        if 'c' == respuestas_correcta[posicion_respuestas]:
                            la_pregunta = fuente2.render("", True, NEGRO)
                            rta_a = fuente.render("", True, NEGRO)
                            rta_b = fuente.render("", True, NEGRO)
                            rta_c = fuente.render("", True, NEGRO)
                            comenzar = fuente2.render(mensaje, True,NEGRO)
                            puntos = puntos + 10

                            score = fuente.render(str("Score: {0}".format(puntos)), True,NEGRO)
                            posicion_respuestas += 1
                            mostrar_pregunta = False

                        elif 'c' != respuestas_correcta[posicion_respuestas]:
                            if error > 0:
                                rta_a = fuente.render("", True, NEGRO)
                                rta_b = fuente.render("", True, NEGRO)
                                rta_c = fuente.render("", True, NEGRO)
                                incorrecto = fuente2.render(mensaje2, True,NEGRO)
                                mostrar_pregunta = False
                                posicion_respuestas += 1
                            rta_c = fuente.render("", True, NEGRO)
                            error += 1



    pantalla.fill(GRIS_CLARO)
    pygame.draw.rect(pantalla, GRIS_OSCURO, (POSICION_SOMBRA,POSICION_SOMBRA, TAMAÑO_LOGO,TAMAÑO_LOGO))
    pantalla.blit(imagen_logo,POSICION_LOGO,)
    pygame.draw.rect(pantalla, GRIS_OSCURO, SOMBRA_BTN_1)
    pygame.draw.rect(pantalla, VERDE_AGUA, BTN_1)
    pygame.draw.rect(pantalla, GRIS_OSCURO, SOMBRA_BTN_2)
    pygame.draw.rect(pantalla, AMARILLO_OPACO, BTN_2)
    pygame.draw.rect(pantalla, GRIS_OSCURO, SOMBRA_SCORE)
    pygame.draw.rect(pantalla, ROJO_CLARO, SCORE)
    pygame.draw.rect(pantalla, GRIS_OSCURO, SOMBRA_PREGUNTA)
    pygame.draw.rect(pantalla, NARANJA, PREGUNTA)
    pygame.draw.rect(pantalla, GRIS_OSCURO, SOMBRA_RTA_A)
    pygame.draw.rect(pantalla, VIOLETA, RTA_A)
    pygame.draw.rect(pantalla, GRIS_OSCURO, SOMBRA_RTA_B)
    pygame.draw.rect(pantalla, ROSA, RTA_B)
    pygame.draw.rect(pantalla, GRIS_OSCURO, SOMBRA_RTA_C)
    pygame.draw.rect(pantalla, AZUL, RTA_C)
    texto_preg = fuente.render("Pregunta", True, NEGRO)
    texto_reiniciar = fuente.render("Reiniciar", True, NEGRO)
    pantalla.blit(texto_preg, (X_PREG,Y_PREG))
    pantalla.blit(texto_reiniciar, (X_REINICIAR,Y_REINICIAR))
    pantalla.blit(la_pregunta, POS_PREG)
    pantalla.blit(rta_a, POS_A)
    pantalla.blit(rta_b, POS_B)
    pantalla.blit(rta_c, POS_C)
    pantalla.blit(comenzar,(25,270))
    pantalla.blit(score,POS_SCORE)
    pantalla.blit(incorrecto, (25,270))

    pygame.display.flip()

pygame.quit()

