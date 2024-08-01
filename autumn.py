import turtle
import random
import math

# =============== Autumn Tree =============== #

# Code by: Worakrit Kullanatpokin

# Instruction: The result will differ due to randomization in the code.
# Furthermore, it will take a several minute to complete.
# Pure recursion with loops and if-elses.

# This version is sakura modded version.
# Overall, both Sakura and Autumn tree have similar code structure.

# =============== Tree =============== #

def draw_tree(size, level, cr_branch):
  twidth = size / 12
  turtle.width(twidth)
  if level <= 0:
    # 1 in 6 chance that there will be no sakura at the end of the branch.
    if random.randint(1,6) != 6:
      draw_leaves(cr_branch)
      turtle.width(twidth)
      return True  # Prevent drawing 2 leaves/flowers at the end
    return False
  else:
    # randomize value
    dr = random.randint(16, 28)
    dl =  random.randint(16, 28)
    fw =  random.randint(int(size - 2) * 10000, int(size + 2)* 10000) / 10000

    size = size *0.7   
    # shorter branch at the end
    if level == 1:
      turtle.forward(fw * 0.8)
    else:
      turtle.forward(fw)
    
    # draw the next large branch
    # right branches
    turtle.right(dr)
    flower_drawn = draw_tree(size, level - 1, cr_branch - 1)
    turtle.left(dr)
    # left branches
    if not flower_drawn:  # Check if one recursion have reached the end of the branch
      turtle.left(dl)
      draw_tree(size, level - 1, cr_branch - 1)
      turtle.right(dl)
      
    # draw additional branches
    # how it works is start drawing an additional branch from the latest branch to the previous branch
    # you can slow turtle down to have a close look at how it works :D
    if 2 <= level < max_level:
      count = random.choice(possibility) + 1
      right = random.randint(0, 1) # 0 is false, 1 is true
      dr_a = dr * 1.6
      dl_a = dl * 1.6
      for i in range(count - 1):
        turtle.backward(fw / count)

        # Let's say "right" is true
        # How this code works is checking for "right" is true.
        # If the index is even, it will follow the value of "right" and draw the right branch.
        # And if index is odd, draws the opposite(left branch).
        
        # It also draws right branch if variable "right" is false, and the current index is odd. (opposite from above)
        # I'm not good at explaination but hope you get the idea.
        draw_right = (right == 1 and i % 2 == 0) or (right == 0 and i % 2 != 0)
        if draw_right is True: # start with right branch first
            turtle.right(dr_a)
        else:
            turtle.left(dl_a) # start with left branch first
        draw_tree(size, level - 1, cr_branch + 1)
        if draw_right is True:
            turtle.left(dr_a)
        else:
            turtle.right(dl_a)
      turtle.forward(fw - (fw / count))
        
    if level == 1:
      turtle.backward(fw * 0.8)
    else:
      turtle.backward(fw)
    return False 

# ========== Leaves =========== #
def draw_leaves(level):
    turtle.right(90)
    set_color()
    draw_leaf()
    
    turtle.left(90)
    turtle.color(wood_color)

# ========== Leaf =========== #
def draw_leaf():
  for i in range(5):
    turtle.left(30 * i)
    turtle.width(1)
    turtle.circle(7, 50)
    turtle.left(130)
    turtle.circle(7, 50)
    turtle.left(130)
    turtle.right(30 * i)

# ========== Falling Leaves =========== #
# iteration approach will be more efficient

# no wind speed
# def draw_falling_leaves(n):
#   for i in range(n):
#     set_color()
#     x = random.randint(-75, 150)
#     y = random.randint(-150, 0)
#     turtle.goto(x, y)
#     rdh = random.randint(0,360)
#     turtle.setheading(rdh) 
#     turtle.pendown()
#     draw_leaves()
#     turtle.penup()

# with wind speed
def draw_falling_leaves(n):
  turtle.penup()
  for i in range(n):
    wind = random.randint(20, 150)
    angle = random.randint(-90, 90)
    
    turtle.setheading(90) 
    turtle.right(angle)
    turtle.forward(wind)
    
    turtle.pendown()
    set_color()
    rd = random.randint(0,360)
    turtle.left(rd)
    draw_leaf()
    turtle.right(rd)
    turtle.penup()
    
    turtle.backward(wind)


# ========== Color =========== #
def set_color():
  random_color = random.choice(hex_colors)
  turtle.color(random_color)

possibility = [2, 2, 2, 2, 3, 3, 3, 4]
max_level = 6
# max_level = 5
wood_color = '#360d02'
hex_colors = ['#6e352c', '#cf5230', '#f59a44', '#e3c598', '#6e612f', '#f05133', '#f79762', '#f47b20', '#9c5708', '#db5400']

turtle.color(wood_color)
turtle.shape("triangle")
turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.goto(50,-150)
turtle.pendown()
draw_tree(100, max_level, math.ceil(max_level / 2))
draw_falling_leaves(35)

turtle.hideturtle()