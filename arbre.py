import turtle
import dessinMSDA
def dessin_arbre():
    turtle.up()
    turtle.goto(0,-130)
    turtle.down()
    turtle.begin_fill()
    dessinMSDA.dessin_rectangle(20,100,'saddlebrown')
    turtle.end_fill()
    turtle.up()
    turtle.goto(-35,-30)
    turtle.down()
    turtle.begin_fill()
    dessinMSDA.dessin_triangle_rectangle(90,'lightgreen')
    turtle.end_fill()
    turtle.up()
    turtle.goto(-30,10)
    turtle.down()
    turtle.begin_fill()
    dessinMSDA.dessin_triangle_rectangle(80,'lightgreen')
    turtle.end_fill()
    turtle.up()
    turtle.goto(-25,45)
    turtle.down()
    turtle.begin_fill()
    dessinMSDA.dessin_triangle_rectangle(70,'lightgreen')
    turtle.end_fill()
    turtle.up()
    turtle.goto(-20,80)
    turtle.down()
    turtle.begin_fill()
    dessinMSDA.dessin_triangle_rectangle(60,'lightgreen')
    turtle.end_fill()
    turtle.hideturtle()