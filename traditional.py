import turtle
import random

# =============== Traditional Tree =============== #

# Code by: Worakrit Kullanatpokin

# Instruction: The result will differ due to randomization in the code.
# Also, it will take a several minute to complete.
# Pure recursion with loops and if-elses.

def draw_tree(size, level, current_branch):
  twidth = size / 8
  turtle.width(twidth)
  if level <= 0:
    draw_leaf(current_branch)
    turtle.width(twidth)
    turtle.forward(0)
  else:
    # randomize value
    dr = random.randint(25, 35)
    dl =  random.randint(25, 35)
    size = random.randint(int(size) - 2, int(size) + 2)
    
    # shorter branch at the end
    if current_branch == 3:
      turtle.forward(size * 0.8)
    elif current_branch < 1:
      turtle.forward(size * 0.9)
    else:
        turtle.forward(size)
    
    # draw the next large branch
    # left branches
    turtle.left(dr)
    draw_tree(size * 0.7, level - 1, current_branch - 1)
    turtle.right(dr)
    #right branches
    turtle.right(dl)
    draw_tree(size * 0.7, level - 1, current_branch - 1)
    turtle.left(dl)
    
    # draw smaller branches
    if 2 <= level < 7:
      turtle.backward(size  / 3)
      turtle.right(dr * 1.6)
      draw_tree(size * 0.7, level - 1, current_branch + 1)
      turtle.left(dr * 1.6)
      turtle.backward(size / 3)
      turtle.left(dl * 1.6)
      draw_tree(size * 0.7, level - 1, current_branch + 1)
      turtle.right(dl * 1.6)
      turtle.forward((2 * size) / 3)
        
    if current_branch == 3:
      turtle.backward(size * 0.8)
    elif current_branch < 1:
      turtle.backward(size * 0.9)
    else:
      turtle.backward(size)

# ========== Leaves =========== #
def draw_leaf(level): # look closely it's no only a circle :)
    turtle.width(4)
    turtle.right(180)
    for i in range(1, 5):
      set_color(level)
      turtle.left(45 * i)
      turtle.circle(4, 60)
      turtle.left(120)
      turtle.circle(4, 60)
      turtle.left(120)
      turtle.right(45 * i)
    
    turtle.left(180)
    turtle.color('#330000')

# ========== Color =========== #
def set_color(lvl):
    if lvl < 0:
        hex_colors = ['#61b545', '#699119', '#3a820d']
        random_color = random.choice(hex_colors)
        turtle.color(random_color)
    elif lvl <= 1:
        hex_colors = ['#4d9635', '#48a142', '#49a130']
        random_color = random.choice(hex_colors)
        turtle.color(random_color)
    elif lvl >= 2:
        hex_colors = ['#c1d11f', '#6ec007', '#34a203', '#3d860b', '#00610e']
        random_color = random.choice(hex_colors)
        turtle.color(random_color)

# ========== Root =========== #
def draw_root(size, level): # How a tree doesn't have root?
  if level <= 0:
    turtle.forward(0)
  else:
    # randomize value
    dr = random.randint(20, 30)
    dl =  random.randint(20, 30)
    size = random.randint(int(size) - 2, int(size) + 2)
    
    turtle.width(size/8)
    
    turtle.forward(size/2)
    
    # draw the next large branch
    # left branches
    turtle.left(dr * 1.5)
    draw_root(size * 0.7, level - 1)
    turtle.right(dr * 1.5)
    #right branches
    turtle.right(dl * 1.5)
    draw_root(size * 0.7, level - 1)
    turtle.left(dl * 1.5)
    
    turtle.backward(size/2)
    
turtle.color('#330000')
turtle.shape("triangle")
turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.backward(100)
turtle.pendown()
draw_tree(100, 7, 3)
turtle.forward(50)
turtle.left(180)
draw_root(100, 9)

turtle.hideturtle()