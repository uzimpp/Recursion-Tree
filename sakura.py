import turtle
import random
import math

# =============== Sakura Tree =============== #

# Code by: Worakrit Kullanatpokin

# Instruction: The result will differ due to randomization in the code.
# Furthermore, it will take a several minute to complete.
# Pure recursion with loops and if-elses.

# What a view of the sakura tree.
# It would be nice if I ever had a chance to experience such view.

# =============== Tree =============== #

def draw_tree(size, level, cr_branch):
  twidth = size / 12
  turtle.width(twidth)
  if level <= 0:
    if random.randint(1,6) != 6:
      draw_flower(cr_branch)
      turtle.width(twidth)
    return
  else:
    # randomize value
    dr = random.randint(16, 28)
    dl =  random.randint(16, 28)
    size = random.randint(int(size) - 2, int(size) + 2)
    
    # shorter branch at the end
    fw =  random.randint((size - 2)* 1000, (size + 2)* 1000) / 1000
    if level == 1:
      turtle.forward(fw * 0.8)
    else:
      turtle.forward(fw)
    
    # draw the next large branch
    # left branches
    turtle.left(dr)
    draw_tree(size * 0.7, level - 1, cr_branch -1)
    turtle.right(dr)
    #right branches
    turtle.right(dl)
    draw_tree(size * 0.7, level - 1, cr_branch - 1)
    turtle.left(dl)
    
    # draw additional branches
    if 2 <= level < max_level:
      count = random.choice(possibility) + 1
      rightleft = random.randint(1, 2)
      for i in range(count - 1):
        turtle.backward(fw / count)
        
        if (rightleft == 1 and i % 2 == 0) or (rightleft == 2 and i % 2 != 0):
            turtle.right(dr * 1.6) # start with right branch first
        else:
            turtle.left(dl * 1.6) # start with left branch first
        draw_tree(size * 0.7, level - 1, cr_branch + 1)
        if (rightleft == 1 and i % 2 == 0) or (rightleft == 2 and i % 2 != 0):
            turtle.left(dr * 1.6)
        else:
            turtle.right(dl * 1.6)
      turtle.forward(fw - (fw / count))
        
    if level == 1:
      turtle.backward(fw * 0.8)
    else:
      turtle.backward(fw)

# ========== Flowers =========== #
def draw_flower(level):
    turtle.right(45)
    for i in range(3):
      set_color()
      turtle.left(18 * i)
      turtle.width(1)
      turtle.circle(7, 50)
      turtle.left(130)
      turtle.circle(7, 50)
      turtle.left(130)
      turtle.right(18 * i)
    
    turtle.left(45)
    turtle.color(wood_color)

# ========== Petals =========== #
def draw_petals():
    turtle.width(1)
    turtle.circle(7, 50)
    turtle.left(130)
    turtle.circle(7, 50)
    turtle.left(130)

# ========== Falling Petals =========== #
def draw_falling_petals(n):
  for i in range(n):
    turtle.penup()
    x = random.randint(-75, 150)
    y = random.randint(-150, 0)
    turtle.goto(x, y)
    
    turtle.pendown()
    set_color()
    rd = random.randint(0,360)
    turtle.left(rd)
    draw_petals()
    turtle.right(rd)
    
# def draw_falling_petals(n):
#   turtle.penup()
#   turtle.goto(-75, 0)
#   for i in range(n):
#     wind = random.randint(10, 150)
#     angle = random.randint(0, 66)
    
#     turtle.setheading(0) 
#     turtle.right(angle)
#     turtle.forward(wind)
    
#     turtle.pendown()
#     set_color()
#     rd = random.randint(0,360)
#     turtle.left(rd)
#     draw_petals()
#     turtle.right(rd)
#     turtle.penup()
    
#     turtle.backward(wind)


# ========== Color =========== #
def set_color():
  random_color = random.choice(hex_colors)
  turtle.color(random_color)
  
possibility = [2, 2, 2, 3, 3, 4]
max_level = 6
# max_level = 5
wood_color = '#3d021c'
hex_colors = ['#fac8de', '#f5bad4', '#f5a9ca', '#fcfcd2', '#f799ae', '#f7b2b2', '#e87689', '#e693a1', '#ffe3f0']

turtle.color(wood_color)
turtle.shape("triangle")
turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.goto(50,-150)
turtle.pendown()
draw_tree(100, max_level, math.ceil(max_level / 2))
draw_falling_petals(125)

turtle.hideturtle()