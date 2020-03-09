import tkinter
import math


def create_circle(canvas, c, r, f=None):
    canvas.create_oval(c[0]-r, c[1]-r, c[0]+r, c[1]+r, fill=f)


window = tkinter.Tk()

height = 500
width = 500
origin = [width/2, height/2]

center = [origin[0], origin[1]]
radius = 100
distance_ratio = .5
distance = distance_ratio * radius
center_circle_ratio = .1

triangle_points = []

myCanvas = tkinter.Canvas(window, height=height, width=width)

#myCanvas.create_line(origin[0], 0, origin[0], height)
#myCanvas.create_line(0, origin[1], width, origin[1])
#create_circle(myCanvas, origin, 100)

ring_y_offset = ((radius+distance)/4)*(math.tan(math.pi/3))

center[0] -= (radius+distance)/2
center[1] -= ring_y_offset
triangle_points.append(center[0])
triangle_points.append(center[1])
create_circle(myCanvas, center, radius)
center = [origin[0], origin[1]]

center[0] += (radius+distance)/2
center[1] -= ring_y_offset
triangle_points.append(center[0])
triangle_points.append(center[1])
create_circle(myCanvas, center, radius)
center = [origin[0], origin[1]]

center[1] += ((radius+distance)/2)*(math.tan(math.pi/3))
center[1] -= ring_y_offset
triangle_points.append(center[0])
triangle_points.append(center[1])
create_circle(myCanvas, center, radius)
center = [origin[0], origin[1]]

#center[1] = (triangle_points[1]+triangle_points[5])/2
#create_circle(myCanvas, center, radius*center_circle_ratio)
#create_circle(myCanvas, center, 0)
#center = [origin[0], origin[1]]

triangle_points.append(triangle_points[0])
triangle_points.append(triangle_points[1])
myCanvas.create_line(triangle_points)



myCanvas.pack()
window.mainloop()
