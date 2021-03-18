#importamos random
from random import randrange
#Importamos turtle
from turtle import *
#Importamos Free Games
from freegames import vector

#Definimos las variebles con sus posiciones y velocidades
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#definimos que al hacer un tap con el mouse a la pantalla
#Se responda con posiciónes y velocidades iniciales, tanto en x como en y.
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25
#definimos que todo este dentro del "marco" osea nuestra pantalla.
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Definimos las formas y colores de las pelotas.
#en este caso seria de el "cañon" tanto como de las "naves".
def draw():
    "Draw ball and targets."
    clear()
    
    #para las naves
    for target in targets:
        goto(target.x, target.y)
        #le quise cambiar el color a un turquesa
        dot(20, 'turquoise')
        
    #para el cañon
    if inside(ball):
        goto(ball.x, ball.y)
        #le quise cambiar el color a un naranja
        dot(6, 'orange')
        
    #que se vaya actualizando
    update()

#Definimos que todo el sistema este en movimiento.
def move():
    "Move ball and targets."
    #definimos que las naves vayan saliendo en lugares random al principio.
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        #El valor de la rapidez en "x" la dejamos igual.
        target.x -= 0.5

    if inside(ball):
        # Dismiui la rapidez de la pelota en "y" que originalmente era -0.35, a 0.01
        # para que no perdiera tiempo en "y" y se fuera mas rapido en "x".
        speed.y -= 0.1
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
    draw()
    # En este punto, dismunui el tiempo que originalmente era 50, a 10, para que fuera mas rapido.
    ontimer(move,10)
    
#Borré el return de la función para que el juego no parara al momento de que las esferas tocaran el
#otro lado de nuestro marco, con esto, el juego seguirá y no parará.
#Borramos esto:
#for target in targets:
    #if not inside(target):
        #return
    
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()