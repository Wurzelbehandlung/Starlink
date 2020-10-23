from tkinter import *

HEIGHT = 1000
WIDTH = 1200
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2

G = 6.67430e-11        # m^3 kg^-1 s^-2, in Exponential-Schreibweise lesbarer


class SpaceObject:
    def __init__(self, canvas, m, x,  y):
        self.canvas = canvas
        if (int(m)) <= 1000:
            color = "grey"
            radius = (int(m)) / 10
        if (int(m)) > 1000:
            color = "brown"
            radius = (int(m)) / 100
        if (int(m)) > 100000:
            color = "green"
            radius = (int(m)) / 10000
        if (int(m)) > 10000000:
            color = "orange"
            radius = (int(m)) / 100000
        if (int(m)) > 1000000000:
            color = "red"
            radius = (int(m)) / 1000000
        if (int(m)) > 100000000000:
            color = "yellow"
            radius = (int(m)) / 10000000
        if (int(m)) > 10000000000000:
            color = "red"
            radius = (int(m)) / 100000000
        if (int(m)) > 1000000000000000:
            color = "blue"
            radius = (int(m)) / 1000000000
        self.radius = radius    
        self.id = canvas.create_oval(0, 0, self.radius * 2, self.radius * 2, fill=color)
        self.canvas.move(self.id, x - self.radius, y - radius)
        self.velocity = [0, 0]

    def draw(self):
        self.canvas.move(self.id, self.velocity[0], self.velocity[1])
        self.canvas.after(1, self.draw)
        self.velocity = [0, 0]

    def bounce(self):
        pos = self.canvas.coords(self.id)
        if (pos[0] > WIDTH - self.radius) or (pos[0] < 0):
            self.velocity[0] = -self.velocity[0]
        if (pos[1] > HEIGHT - self.radius) or (pos[1] < 0):
            self.velocity[1] = -self.velocity[1]
            self.canvas.after(1, self.bounce)

    def gravity(self):
        self.velocity[1] = self.velocity[1] + 0.01
        self.canvas.after(1, self.gravity)


class FG:
    def __init__(self, canvas,   f,  dist,  m1,  m2):
        self.canas = canvas
        self.f = f
        self.dist = dist
        self.m_1 = m_1
        self.m_2 = m_2
        self.canvas.create_line(y, -100, y, 100 )
        k = 10
        i = 1
        if f > k:
            f = f / 10
            k = k * 10
            i = i * 10


window = Tk()
window.title("Gravitationssimulation")


def click_berechnen_button():
    m1 = lm1.get()
    m2 = lm2.get()
    
    dist = ldist.get()
    f = (G * (int(m1)) * (int(m2)) / (int(dist)) ** 2)
    m2 = 0 - (int(m2))
    disp_txt = 'Fg = {:3.3e}'.format(f)
    ergebnis_fg.set(disp_txt)
    a = SpaceObject(c, m1,  (MID_X + 100), MID_Y)
    b = SpaceObject(c,  m2, (MID_X - 100), MID_Y)
    # z = FG(c,  f, dist,  m1,  m2)


frame = Frame(window)
frame.pack(side=LEFT)
s_m1 = StringVar()
s_m2 = StringVar()
s_dist = StringVar()

mass1 = Label(frame, text="Masse 1 [kg]")
mass1.pack(side=TOP)
lm1 = Entry(frame, textvariable=s_m1)
lm1.pack(side=TOP)

mass2 = Label(frame, text="Masse 2 [kg]")
mass2.pack(side=TOP)
lm2 = Entry(frame, textvariable=s_m2)
lm2.pack(side=TOP)
sdist = Label(frame, text="Abstand [m]")
sdist.pack(side=TOP)
ldist = Entry(frame, textvariable=s_dist)
ldist.pack(side=TOP)

ergebnis_fg = StringVar()

l_kraft = Label(frame, textvariable=ergebnis_fg)
l_kraft.pack(side=BOTTOM)

b_rechnen = Button(frame, text="Berechnen", command=click_berechnen_button)
b_rechnen.pack(side=BOTTOM)

c = Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
c.pack()

window.mainloop()
