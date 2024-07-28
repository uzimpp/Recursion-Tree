import turtle
import random

# =============== Lemon Tree =============== #

# Code by: Worakrit Kullanatpokin

# Instruction: The result will differ due to randomization in the code.
# Pure recursion with loops and if-elses.

# Well, fruits must be pulled by a gravity just like an apple right?



#   Anyway, here is the hook lyrics of the song named "Lemon tree" by Fools Garden.

#   “I wonder how, I wonder why
#   Yesterday, you told me 'bout the blue, blue sky
#   And all that I can see is just a yellow lemon tree
#   I'm turnin' my head up and down
#   I'm turnin', turnin', turnin', turnin', turnin' around
#   And all that I can see is just another lemon tree”

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
    if current_branch < 1:
      turtle.forward(size * 0.9)
    else:
        turtle.forward(size)
    
    # draw lemon
    if (random.randint(1,7) == 3) and (1 <= level <= 4):
      # not every branch has fruits right?
      draw_lemon(size, level)
    
    # draw the next large branch
    # left branches
    turtle.left(dr)
    draw_tree(size * 0.7, level - 1, current_branch - 1)
    turtle.right(dr)
    #right branches
    turtle.right(dl)
    draw_tree(size * 0.7, level - 1, current_branch - 1)
    turtle.left(dl)
    
    # draw small branches
    if 3 <= level < 6:
      turtle.backward(size  / 3)
      turtle.right(dr * 1.6)
      draw_tree(size * 0.7, level - 1, current_branch + 1)
      turtle.left(dr * 1.6)
      turtle.backward(size / 3)
      turtle.left(dl * 1.6)
      draw_tree(size * 0.7, level - 1, current_branch + 1)
      turtle.right(dl * 1.6)
      turtle.forward((2 * size) / 3)
    
    if current_branch < 1:
      turtle.backward(size * 0.9)
    else:
      turtle.backward(size)

def draw_leaf(level):
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

def draw_lemon(size, level):
    turtle.backward(size / 2)
    # set turtle heading as the gravity pull it :)
    original_heading = turtle.heading()
    turtle.setheading(270)
    
    # draw a branch for lemon
    set_color(level)
    turtle.width(2)
    turtle.forward(7)
    
    # lemon!!
    turtle.color('#f5ea53')
    turtle.width(6)
    turtle.right(90)
    turtle.circle(2)
    turtle.left(90)
    
    set_color(level)
    turtle.width(2)
    turtle.backward(7)
    
    # reset values to its orignal
    turtle.color('#330000')
    twidth = size / 8
    turtle.width(twidth)
    turtle.setheading(original_heading)
    turtle.forward(size / 2)

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
    
turtle.color('#330000')
turtle.shape("triangle")
turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.backward(100)
turtle.pendown()
draw_tree(75, 6, 1)

turtle.hideturtle()