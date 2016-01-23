import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# Create a default figure and subplot
fig, ax = plt.subplots()
# Specify x - y axes' range respectively
ax.axis([0,6,0,6])
# set background colour
ax.set_axis_bgcolor('grey')
# Draw a two-dimensional point of circle shape with specific characteristics
circle_point, = ax.plot(3, 3, 'o', markerfacecolor='w', markeredgecolor='red', markersize=3,
 markeredgewidth = 3)
# Draw first frame
def init():
 return circle_point,
 # Draw frame
def animate(i):
  if i < 100:
      j = 0
  else:
      j = i - 97
  if i < 200:
      k = 0
  else:
      k = i - 197
  if i < 300:
      l = 0
  else:
      l = i - 297
  if i < 400:
      m = 0
  else:
      m = i - 397
  if i < 500:
      p = 0
  else:
      p = i - 497
  if i < 600:
      n = 0
  else:
      n = i - 597
  if i < 700:
      f = 0
  else:
      f = i - 697
  
  # Update circle point's position
  circle_point,=ax.plot(3, 3, 'o', markerfacecolor='red', markeredgecolor = 'red', markersize = i, markeredgewidth = 3 )
  circle_point1,=ax.plot(3, 3, 'o', markerfacecolor='orange', markeredgecolor = 'orange', markersize = j, markeredgewidth = 3 )
  circle_point2,=ax.plot(3, 3, 'o', markerfacecolor='yellow', markeredgecolor = 'yellow', markersize = k, markeredgewidth = 3 )
  circle_point3,=ax.plot(3, 3, 'o', markerfacecolor='green', markeredgecolor = 'green', markersize = l, markeredgewidth = 3 )
  circle_point4,=ax.plot(3, 3, 'o', markerfacecolor='blue', markeredgecolor = 'blue', markersize = m, markeredgewidth = 3 )
  circle_point5,=ax.plot(3, 3, 'o', markerfacecolor='indigo', markeredgecolor = 'indigo', markersize = p, markeredgewidth = 3 )
  circle_point6,=ax.plot(3, 3, 'o', markerfacecolor='violet', markeredgecolor = 'violet', markersize = n, markeredgewidth = 3 )
  circle_point7,=ax.plot(3, 3, 'o', markerfacecolor='grey', markeredgecolor = 'grey', markersize = f, markeredgewidth = 3 )
  return [circle_point, circle_point1,circle_point2,circle_point3, circle_point4,circle_point5,circle_point6, circle_point7,]
   # Interval draws a new frame every given milliseconds
ani = animation.FuncAnimation(fig, animate, np.arange(3, 800),
init_func=init, interval=25)
ani.save("kukloi.mp4", fps=40)