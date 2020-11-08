import turtle
import tkinter
import math

def drawTriangle(points,triangleTurtle):
    triangleTurtle.up()
    triangleTurtle.goto(points[0][0],points[0][1])
    triangleTurtle.down()
    triangleTurtle.goto(points[1][0],points[1][1])
    triangleTurtle.goto(points[2][0],points[2][1])
    triangleTurtle.goto(points[0][0],points[0][1])

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinskiTriangle(points,degree,triangleTurtle):
    drawTriangle(points,triangleTurtle)
    if degree > 0:
        sierpinskiTriangle([points[0],getMid(points[0], points[1]),getMid(points[0], points[2])],degree-1, triangleTurtle)
        sierpinskiTriangle([points[1],getMid(points[0], points[1]),getMid(points[1], points[2])],degree-1, triangleTurtle)
        sierpinskiTriangle([points[2],getMid(points[2], points[1]),getMid(points[0], points[2])],degree-1, triangleTurtle)

def main(): 
   triangleTurtle = turtle.Turtle()
   triangleWindow = turtle.Screen()
   triangleInitPoints = [[-200,-100],[0,200],[200,-100]]
   sierpinskiTriangle(triangleInitPoints,4,triangleTurtle)
   triangleWindow.exitonclick()


main()
