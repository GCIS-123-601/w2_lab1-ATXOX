import turtle
def my_turtle():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50,50)
    turtle.down()
    turtle.home()
    turtle.circle(25)
def turtle_state():
    print(turtle.isdown())
    print(turtle.heading())
    print(turtle.xcor(),turtle.ycor())
def main():
    turtle_state()
    my_turtle()
    turtle_state()
    input("press enter to continue...")
main()
