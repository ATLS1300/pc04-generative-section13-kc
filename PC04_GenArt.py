#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:46:17 2021

@author: kcyeneza
This is a generative art piece inspired by 
Meow Wolf, with the bright colors and jagged lines.
There should be lots of lines and paint splatters and circles.
"""
#I used the random library to generate different amounts of lines/circles drawn each time.
#I also used random to vary the pen sizes and the location of the turtle.
import turtle
import math
import random

turtle.colormode(255)

panel= turtle.Screen()
w=800
h=800

panel.setup(width=w, height=h)
panel.bgcolor(35,46,209)

l1=turtle.Turtle()
l1.speed(100)


for i in range(random.randint(3, 10)):
    color1=turtle.pencolor(137,210,220)
    l1.up()
    l1.goto(-800,800)
    l1.down()
    l1.pencolor(137,210,220)
    l1.begin_fill()
    l1.fillcolor(137,210,220)
    l1.goto(random.randint(-800,800),random.randint(-800,800))
    l1.forward(9*10)
    l1.end_fill()
    

l2=turtle.Turtle()
l2.speed(100)
for i in range(random.randint(3, 20)):
    color2=turtle.pencolor(243,116,174)
    l2.up()
    l2.goto(800,-800)
    l2.down()
    l2.width(random.randint(5,10))
    l2.pencolor(243,116,174)
    l2.begin_fill()
    l2.fillcolor(243,116,174)
    l2.goto(random.randint(-800,800),random.randint(-800,800))
    l2.forward(9+2)
    l2.end_fill()
    
    
l3=turtle.Turtle()
l3.speed(1000000)
for i in range (random.randint(50,100)):
    color3=turtle.pencolor(194,232,18)
    l3.up()
    l3.goto(-800,0)
    l3.down()
    l3.pencolor(194,232,18)
    l3.goto(random.randint(-800,800),random.randint(-800,800))
    l3.forward(10+20)
    
l4=turtle.Turtle()
l4.speed(100000)
for i in range(random.randint(5,10)):
    color4=turtle.pencolor(252,159,91)
    l4.up()
    l4.down()
    l4.pencolor(252,159,91)
    l4.begin_fill()
    l4.fillcolor(252,159,91)
    l4.circle(random.randint(100, 200))
    l4.end_fill()
    l4.up()
    l4.goto(random.randint(-800,800),random.randint(-800,800))
    l4.down()
    
for i in range(random.randint(40,100)):
    l4.speed(100000)
    color4=turtle.pencolor(252,159,91)
    l4.up()
    l4.down()
    l4.pencolor(252,159,91)
    l4.begin_fill()
    l4.fillcolor(252,159,91)
    l4.circle(random.randint(1,5))
    l4.end_fill()
    l4.up()
    l4.goto(random.randint(-800,800),random.randint(-800,800))
    l4.down()
    
      
scale=10
radiusX=10
radiusY=5

l5=turtle.Turtle()
l5.speed(1000)    

for i in range(random.randint(2,6)):
    color5=turtle.pencolor(35,46,209)
    l5.up()
    l5.down()
    l5.pencolor(35,46,209)
    l5.begin_fill()
    l5.fillcolor(35,46,209)
    l5.circle(random.randint(100, 200))
    l5.end_fill()
    l5.up()
    l5.goto(random.randint(-800,800),random.randint(-800,800))
    l5.down()
    
    
turtle.done()
