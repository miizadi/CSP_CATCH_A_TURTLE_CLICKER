# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random 
spo = ["red", "blue","salmon","pink", "goldenrod", "ivory","dark orange"]
sh = ["turtle", "arrow", "circle", "square", "triangle",]
#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
spot_interval = 1000   #1000 represents 1 second
timer_up = False
#-----game configuration----
spot_size = random.randint(2,5)
spot_color = random.choice(spo)
spot_shape = random.choice(sh)
score = 0
timelime = 30
#-----initialize turtle-----
spot = trtl.Turtle()
spot.speed(0)
spot.penup()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

#-----game functions--------
def countdown():
  global timer, timer_up
  spot.clear()
  if timer <= 0:
    spot.write("Time's Up", font=font_setup)
    timer_up = True
    print("Your final score is", score)
    exit()
  else:
    spot.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    spot.getscreen().ontimer(countdown, spot_interval) 
def spot_clicked(x,y):
  global spot_color, spot_shape, score, spot_size
  rendomx = random.randint(-200,200)
  rendomy = random.randint(-200,200)
  spot.setposition(rendomx,rendomy)
  spot_size = random.randint(2,5)
  spot_color = random.choice(spo)
  spot_shape = random.choice(sh)
  spot.shapesize(spot_size)
  spot.shape(spot_shape)
  spot.fillcolor(spot_color)
  score = score + 1

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, spot_interval)
wn.mainloop()