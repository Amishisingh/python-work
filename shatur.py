import turtle
turtle.title("ten")
turtle.Screen().bgcolor("black")
c=["deepPink","BROWN1","aqua","pink","blue","orange","purple","PINK"]

a=turtle.Turtle()
a.speed('fastest')
for r in range(4):
   a.pencolor(c[r%8])
   a.forward(200)
   a.left(90)

# these didnt work
turtle.up
turtle.goto(-90,3)
turtle.shape("circle")
a.fillcolor("yellow")
turtle.down
# 

a=turtle.Turtle()
a.speed('fastest')
i=1
while i<9000:
    a.pencolor(c[i%8])
    a.forward(i)
    a.left(120)
    i+=1
turtle.done()

