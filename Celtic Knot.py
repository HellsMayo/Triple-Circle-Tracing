import tkinter
import math


def create_circle(canvas, c, r, f=None, cross=False, width=0, height=0):
    canvas.create_oval(c[0]-r, c[1]-r, c[0]+r, c[1]+r, fill=f)
    if cross:
        canvas.create_line(0, c[1], width, c[1])
        canvas.create_line(c[0], 0, c[0], height)


def create_arc(canvas, c, r, start, end, f=None):
    canvas.create_arc(c[0]-r, c[1]-r, c[0]+r, c[1]+r, start=(start*180/math.pi), extent=(end*180/math.pi)-(start*180/math.pi), style='arc', fill=f)


# create application window
window = tkinter.Tk()

# define size and center of the window and canvas
myWidth = 2048
myHeight = 2048
origin = [myWidth/2, myHeight/2]

# create canvas
myCanvas = tkinter.Canvas(window, width=myWidth, height=myHeight)

# define size and values of the circles
radius = 850/2
distance_ratio = 0.365242199
center_circle_ratio = 1
edge_length = radius*(1 + distance_ratio)

# calculate the center of every circle
# calculate the center of circles 0 to 2
x0 = origin[0]-edge_length/2
y0 = origin[1]-(math.sqrt(3)/6)*edge_length
x1 = origin[0]+edge_length/2
# y1 = y0
x2 = origin[0]
y2 = origin[1]+(math.sqrt(3)/3)*edge_length

# calculate the center of the center circle
xC = origin[0]
yC = origin[1]

# calculate the coordinates of where each of the arcs intersect
intersection_distance = (math.sqrt(3) / 6) * edge_length + (radius * math.sin(math.acos(edge_length / (2 * radius))))
xI0 = origin[0]
yI0 = yC - intersection_distance
xI1 = origin[0] + intersection_distance * math.cos(math.pi/6)
yI1 = yC + intersection_distance * math.sin(math.pi/6)
xI2 = origin[0] - intersection_distance * math.cos(math.pi/6)
# yI2 = yI1

def coordinate_percentage(x, y, w, h, r):
    x = (x-r)/w
    y = (y-r)/h
    return (x, y)

# create circles 0 to 2 equidistant apart
create_arc(myCanvas, (x0, y0), radius, math.atan2(-(yI1-y0), xI2-x0), math.atan2(-(yI0-y0), xI0-x0))
print("circle 0 coordinates: (%f, %f)" % coordinate_percentage(x0, y0, myWidth, myHeight, radius))
#create_circle(myCanvas, (x0, y0), radius)#, cross=True, width=myWidth, height=myHeight)
create_arc(myCanvas, (x1, y0), radius, math.atan2(-(yI0-y0), xI0-x1), 2*math.pi+math.atan2(-(yI1-y0), xI1-x1))
print("circle 1 coordinates: (%f, %f)" % coordinate_percentage(x1, y0, myWidth, myHeight, radius))
#create_circle(myCanvas, (x1, y0), radius)#, cross=True, width=myWidth, height=myHeight)
create_arc(myCanvas, (x2, y2), radius, math.atan2(-(yI1-y2), xI1-x2), math.atan2(-(yI1-y2), xI2-x2))
print("circle 2 coordinates: (%f, %f)" % coordinate_percentage(x2, y2, myWidth, myHeight, radius))
#create_circle(myCanvas, (x2, y2), radius)#, cross=True, width=myWidth, height=myHeight)

# create center circle with adjusted ratio
create_circle(myCanvas, (xC, yC), center_circle_ratio*radius)#, cross=True, width=myWidth, height=myHeight)

#create_circle(myCanvas, (xI0, yI0), 10)
#create_circle(myCanvas, (xI1, yI1), 10)
#create_circle(myCanvas, (xI2, yI1), 10)


#create_circle(myCanvas,
#              (origin[0],
#               origin[1] - ((math.sqrt(3)/4)*edge_length + radius*math.sin(math.acos(edge_length/2/radius)))),
#              10)

# create an equilateral triangle between circles 0 to 2
#triangle_points = [x0, y0, x1, y0, x2, y2, x0, y0]
#myCanvas.create_line(triangle_points)
#myCanvas.create_line(0, origin[1], myWidth, origin[1])
#myCanvas.create_line(origin[0], 0, origin[0], myHeight)

myCanvas.pack()
window.mainloop()
