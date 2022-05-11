
# SF - 1/606.4      ###     SF - 1/6093440    ### Speed SF - 3/47000
# Mercury – 2.5 pixels, 
# Venus – 6.2 pixels,
# Earth – 6.53 pixels, 
# Mars – 3.47 pixels, 
# Jupiter – 71.64 pixels, 
# Saturn – 59.67 pixels, 
# Uranus – 25.9877968338 pixels, 
# Neptune – 25.2292216359 pixels,

# SF - 5/28846
# Sun - 432,690 mi; 75 pixels
import turtle
t = turtle.Turtle()
Mercury = turtle.Turtle()
Venus = turtle.Turtle()
Earth = turtle.Turtle()
Mars = turtle.Turtle()
Jupiter = turtle.Turtle()
Saturn = turtle.Turtle()
Uranus = turtle.Turtle()
Neptune = turtle.Turtle()
ring = turtle.Turtle()
Mercury.speed(0)
Venus.speed(0)
Earth.speed(0)
Mars.speed(0)
Jupiter.speed(0)
Saturn.speed(0)
Uranus.speed(0)
Neptune.speed(0)
ring.speed(0)
s = turtle.Screen()
s.bgcolor("black")
s.screensize(2000,2000)
t.speed(0)
t.pencolor("white")
t.pu()
t.setposition(700, 800)
style = ('Courier', 16, 'italic')
t.pd()
t.write("Planet Size SF - 1/606.4 \n Planet Orbital distance SF - 1/9280000 \n Planet Speed SF - 3/47000 \n Sun SF - 5/28846", font = style, align = "center")
class sunCreate:
  t.pu()
  t.setposition(0,-75)
  t.pd()
  t.color("yellow")
  t.begin_fill()
  t.circle(75)
  t.end_fill()
sunCreate()
class setPlanet:
  def __init__(self, name, radius, color, orbit_radius, strName, speed, degree):
    self.name = name
    self.radius = radius
    self.color = color
    self.orbit_radius = orbit_radius
    self.degree = degree
    self.strName = strName
    self.speed = speed
    self.name.shape("circle")
    self.name.shapesize(self.radius/10)
    self.name.color(self.color)
    self.name.pu()
    self.name.setposition(0, -self.orbit_radius - 75)
    self.name.pd()
    self.name.write(str(self.strName))
    self.name.circle(self.orbit_radius+75, 361)
    self.name.circle(self.orbit_radius+75, self.degree)
    self.name.pu()
  def movePlan(self):
    self.name.pd()
    self.name.color(self.color)
    self.name.circle(self.orbit_radius+75, self.speed)
    self.name.pu()
    

Me = setPlanet(Mercury, 2.5, "orange", 25/4, "Mercury", 6.0, 10)

Ve = setPlanet(Venus, 6.2, "#FFFFF6", 78.6/4, "Venus", 4.46808510638, 300)

Ea = setPlanet(Earth, 6.53, "blue", 108.3/4, "Earth", 3.80425531914, 350)

Ma = setPlanet(Mars, 3.87, "red", 159.3/4, "Mars", 3.07659574468, 0)

Ju = setPlanet(Jupiter, 71.64, "#bcafb2", 543.52/4, "Jupiter", 1.67234042552, 75)

Sa = setPlanet(Saturn, 59.67, "#ab604a", 1079/4, "Saturn", 1.23829787232, 50)

Ur = setPlanet(Uranus, 25.9877968338, "#4FD0E7", 2150.2/4, "Uranus", 0.86808510638, 150)

Ne = setPlanet(Neptune, 25.2292216359, "#4b70dd", 3263.3/4, "Neptune", 0.68936170212, 95)
counter = 0
while True:
  counter +=1
  Me.movePlan()
  Ve.movePlan()
  Ea.movePlan()
  Ma.movePlan()
  Ju.movePlan()
  Sa.movePlan()
  corsat = Saturn.pos()
  if counter != 1:
    ring.pencolor("#000000")
    ring.circle(79.67)
  ring.pu()
  ring.setposition(corsat[0], corsat[1]-80)
  ring.pd()
  ring.pencolor("#ab604a")
  ring.circle(79.67)
  Ur.movePlan()
  Ne.movePlan()