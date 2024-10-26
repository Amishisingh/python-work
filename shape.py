
# arithmetic operators: +,-,*,/,%,//,**
# variable: var iables are empty container where you can store data
isItRainingOnAmishi = True
# data types

#conditional operators

#import library_name
import turtle
turtle.title("ten")
turtle.Screen().bgcolor("black")
a=turtle.Turtle()
a.speed('fastest')
c=["red","yellow","purple","orange","green","pink","blue"]
i=1
while i<190:
      a.pencolor(c[i%len(c)])
      a.width(2)
      a.forward(600)
      a.left(157)
      i+=1
turtle.done

