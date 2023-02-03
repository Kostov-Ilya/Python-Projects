import turtle

turtle.shape('turtle')

turtle.speed(5)

turtle.pensize(5)

for i in range(10):

 turtle.pencolor('red')
 
 turtle.circle(60)

 turtle.circle(-60)

 turtle.pencolor('blue')
 
 turtle.left(60)

 turtle.right(-60)

 turtle.pencolor('pink')
 
 turtle.circle(80)

 turtle.circle(-80)

 turtle.pencolor('purple')
 
 turtle.circle(90)

 turtle.circle(-90)

 turtle.pencolor('green')
 
 turtle.circle(100)

 turtle.circle(-100)

 turtle.pencolor('yellow')
 
 turtle.circle(200)

 turtle.circle(-200)

 turtle.pencolor('grey')
 
 turtle.circle(300)

 turtle.circle(-300)

turtle.exitonclick()