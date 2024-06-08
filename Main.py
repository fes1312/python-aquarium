import turtle as t
import random as rand

t.title("Acquario")


t.speed(35)
def sfondo(colore):

    t.bgcolor("light blue")
    t.fillcolor(colore)
    t.begin_fill()
    t.penup()
    t.goto(-1000,-150)
    t.forward(2000)
    t.right(90)
    t.forward(550)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(550)
    t.end_fill()   
    def bolle(y):
        t.penup()
        t.goto(1000,y)
        t.pendown()
        t.pensize(3)
        t.color("blue")
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.circle(60,180)
        t.right(180)
        t.setheading(90)
        t.penup()
    bolle(300)
    bolle(150)
    bolle(0)
def genera_sassi():
    raggio = rand.randint(120,140)
    steps = rand.randint(5,10)
    colori = ["gray", "light gray", "darkgray"]
    colore = rand.randint(0,3)

    t.fillcolor("gray")
    t.begin_fill()
    t.circle(raggio,180,steps)
    t.end_fill()

def posizione_sassi():
    for i in range(3):
        
        x = rand.randint(-1000,1000)    
        #y = rand.randint(-150,-200)
        t.goto(x,-150)
        
        genera_sassi()
        t.left(180)

def pesce_rettangolo():
    t.setheading(90)
    x = rand.randint(-800,800)
    y = rand.randint(-150,400)
    t.penup()
    t.goto(x,y)
    t.fillcolor("indianred1")
    t.begin_fill()
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.end_fill()
    t.fillcolor("aquamarine3")
    t.begin_fill()
    t.penup()
    t.right(180)
    t.forward(25)
    t.pendown()
    t.right(45)
    t.forward(60)
    t.right(315)
    t.left(180)
    t.forward(84)
    t.right(135)
    t.forward(60)
    t.end_fill()
    t.setheading(180)
    t.left(180)
    t.penup()
    t.forward(130)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(7)
    t.end_fill()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

def stelle_marine():
    x = rand.randint(-1000,1000) 
    y = rand.randint(-500,-400)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow1")
    t.begin_fill()
    t.setheading(rand.randint(45,100))
    
    for i in range(5):
        
        t.forward(200)
        t.left(144)
    t.end_fill()

def genera_pesci():
    pesce_rettangolo()
    pesce_rettangolo()
    pesce_rettangolo()
    pesce_rettangolo()
    

def alga():
    x = rand.randint(-700, 700)
    y = rand.randint(-180,-150)
    t.color("green")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.left(rand.randint(85,110))
    t.pensize(20)
    t.forward(200)
    t.right(rand.randint(75,105))
    t.forward(60)
    t.undo
    t.right(rand.randint(35,105))
    t.forward(60)
    t.color("green")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.left(rand.randint(34,230))
    t.pensize(20)
    t.forward(200)
    t.left(rand.randint(35,105))
    t.forward(60)
    t.undo
    t.right(rand.randint(35,105))
    t.forward(60)
    t.color("green")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.left(rand.randint(85,110))
    t.pensize(10)
    t.forward(200)
    t.right(rand.randint(35,105))
    t.forward(60)
    t.undo
    t.right(rand.randint(35,105))
    t.forward(60)
    t.color("green")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.left(rand.randint(85,110))
    t.pensize(10)
    t.forward(200)
    t.right(rand.randint(35,105))
    t.forward(60)
    t.undo
    t.right(rand.randint(35,105))
    t.forward(60)





    t.color("black")
    t.pensize(1)





def main():
    sfondo("antiquewhite3")
    posizione_sassi()
    
    alga()
    alga()
    alga()
    stelle_marine()
    stelle_marine()
    genera_pesci()

    
    
main()

t.mainloop()