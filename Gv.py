from tkinter import *
from math import log
HEIGHT = 1000
WIDTH = 1200
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2

G = 6.67430e-11        # m^3 kg^-1 s^-2, in Exponential-Schreibweise lesbarer


class SpaceObject:
    def __init__(self, canvas, m, x,  y, b_offset):
        self.canvas = canvas
        if (int(m)) <= 1e3:
            color = "grey"
        if (int(m)) > 1e3:
            color = "brown"
        if (int(m)) > 1e6:
            color = "green"
        if (int(m)) > 1e8:
            color = "orange"
        if (int(m)) > 1e9:
            color = "red"
        if (int(m)) > 1e11:
            color = "yellow"
        if (int(m)) > 1e13:
            color = "red"
        if (int(m)) > 1e15:
            color = "blue"
        self.radius = 30 + log(float(m)) * 3
        self.id = canvas.create_oval(0, 0, self.radius * 2, self.radius * 2, fill=color)
        if b_offset == True:
            self.canvas.move(self.id, x, y - self.radius)
        else:
            self.canvas.move(self.id, x - (2 * self.radius), y - self.radius)
        self.velocity = [0, 0.1]

    def draw(self):
        self.canvas.move(self.id, self.velocity[0], self.velocity[1])
        self.canvas.after(1, self.draw)

    def bounce(self):
        pos = self.canvas.coords(self.id)
        if (pos[0] > (WIDTH - 2 * self.radius)) or (pos[0] < 0):
            self.velocity[0] = -self.velocity[0]
        if (pos[1] > (HEIGHT - 2 * self.radius)) or (pos[1] < 0):
            self.velocity[1] = -self.velocity[1]
        self.canvas.after(1, self.bounce)

    def gravity(self):
        self.velocity[1] = self.velocity[1] + 0.01
        self.canvas.after(1, self.gravity)


class FG:
    def __init__(self, canvas,   f,  dist,  m1,  m2):
        self.canvas = canvas
        self.f = f
        self.dist = dist
        self.m1 = m1
        self.m2 = m2
        self.canvas.create_line(MID_Y - 10, 300, MID_Y - 10, 900 )
        self.f_angabe = 1
        self.f_kleingenug = False
        self.anzahl = self.f
        while self.f_kleingenug == False:
            if self.anzahl >= 10:
                self.f_angabe = self.f_angabe * 10
                self.anzahl = self.anzahl / 10
            else:
                self.f_kleingenug = True
        if self.anzahl == 1:
            self.canvas.create_line(470, 350, 510, 350)
            self.canvas.create_text(520, 350, text = 0)
            self.canvas.create_line(470, 850, 510, 850)
            self.canvas.create_text(520, 850, text = 1 * self.f_angabe)
        elif self.anzahl == 2:
            self.canvas.create_line(470, 350, 510, 350)
            self.canvas.create_text(520, 350, text = 0)
            self.canvas.create_line(470, 600, 510, 600)
            self.canvas.create_text(520, 600, text = 1 * self.f_angabe)
            self.canvas.create_line(470, 850, 510, 850)
            self.canvas.create_text(520, 850, text = 2 * self.f_angabe)
        elif self.anzahl == 3:
            self.canvas.create_line(470, 350, 510, 350)
            self.canvas.create_text(520, 350, text = 0)
            self.canvas.create_line(470, 520, 510, 520)
            self.canvas.create_text(520, 520, text = 1 * self.f_angabe)
            self.canvas.create_line(470, 680, 510, 680)
            self.canvas.create_text(520, 680, text = 2 * self.f_angabe)
            self.canvas.create_line(470, 850, 510, 850)
            self.canvas.create_text(520, 850, text = 3 * self.f_angabe)
        elif self.anzahl == 4:
            self.canvas.create_line(470, 350, 510, 350)
            self.canvas.create_text(520, 350, text = 0)
            self.canvas.create_line(470, 475, 510, 475)
            self.canvas.create_text(520, 475, text = 1 * self.f_angabe)
            self.canvas.create_line(470, 600, 510, 600)
            self.canvas.create_text(520, 600, text = 2 * self.f_angabe)
            self.canvas.create_line(470, 725, 510, 725)
            self.canvas.create_text(520, 725, text = 3 * self.f_angabe)
            self.canvas.create_line(470, 850, 510, 850)
            self.canvas.create_text(520, 350, text = 4 * self.f_angabe)
        elif self.anzahl == 5:
            self.canvas.create_line(470, 350, 510, 350)
            self.canvas.create_text(520, 350, text = 0)
            self.canvas.create_line(470, 450, 510, 450)
            self.canvas.create_text(520, 450, text = 1 * self.f_angabe)
            self.canvas.create_line(470, 550, 510, 550)
            self.canvas.create_text(520, 550, text = 2 * self.f_angabe)
            self.canvas.create_line(470, 650, 510, 650)
            self.canvas.create_text(520, 650, text = 3 * self.f_angabe)
            self.canvas.create_line(470, 750, 510, 750)
            self.canvas.create_text(520, 750, text = 4 * self.f_angabe)
            self.canvas.create_line(470, 850, 510, 850)
            self.canvas.create_text(520, 850, text = 5 * self.f_angabe)
        elif self.anzahl == 6:
            self.canvas.create_line(470, 350, 510, 350)
            self.canvas.create_text(520, 350, text = 0)
            self.canvas.create_line(470, 433, 510, 433)
            self.canvas.create_text(520, 433, text = 1 * self.f_angabe)
            self.canvas.create_line(470, 516, 510, 516)
            self.canvas.create_text(520, 516, text = 2 * self.f_angabe)
            self.canvas.create_line(470, 600, 510, 600)
            self.canvas.create_text(520, 600, text = 3 * self.f_angabe)
            self.canvas.create_line(470, 683, 510,683)
            self.canvas.create_text(520, 683, text = 4 * self.f_angabe)
            self.canvas.create_line(470, 766, 510, 766)
            self.canvas.create_text(520, 766, text = 5 * self.f_angabe)
            self.canvas.create_line(470, 850, 510, 850)
            self.canvas.create_text(520, 850, text = 6 * self.f_angabe)
        elif self.anzahl == 7:
            self.canvas.create_line(470, 350, 510, 350)
            self.canvas.create_text(520, 350, text = 0)
            self.canvas.create_line(470, 421, 510, 421)
            self.canvas.create_text(520, 421, text = 1 * self.f_angabe)
            self.canvas.create_line(470, 492, 510, 492)
            self.canvas.create_text(520, 492, text = 2 * self.f_angabe)
            self.canvas.create_line(470, 564, 510, 564)
            self.canvas.create_text(520, 564, text = 3 * self.f_angabe)
            self.canvas.create_line(470, 635, 510, 635)
            self.canvas.create_text(520, 635, text = 4 * self.f_angabe)
            self.canvas.create_line(470, 707, 510, 707)
            self.canvas.create_text(520, 707, text = 5 * self.f_angabe)
            self.canvas.create_line(470, 778, 510, 778)
            self.canvas.create_text(520, 778, text = 6 * self.f_angabe)
            self.canvas.create_line(470, 850, 510, 850)
            self.canvas.create_text(520, 850, text = 7 * self.f_angabe)
        elif self.anzahl == 8:
            self.canvas.create_line(470, 350, 510, 350)
            self.canvas.create_text(520, 350, text = 0)
            self.canvas.create_line(470, 412, 510, 412)
            self.canvas.create_text(520, 412, text = 1 * self.f_angabe)
            self.canvas.create_line(470, 475, 510, 475)
            self.canvas.create_text(520, 475, text = 2 * self.f_angabe)
            self.canvas.create_line(470, 537, 510, 537)
            self.canvas.create_text(520, 537, text = 3 * self.f_angabe)
            self.canvas.create_line(470, 600, 510, 600)
            self.canvas.create_text(520, 600, text = 4 * self.f_angabe)
            self.canvas.create_line(470, 662, 510, 662)
            self.canvas.create_text(520, 662, text = 5 * self.f_angabe)
            self.canvas.create_line(470, 725, 510, 725)
            self.canvas.create_text(520, 725, text = 6 * self.f_angabe)
            self.canvas.create_line(470, 787, 510, 787)
            self.canvas.create_text(520, 787, text = 7 * self.f_angabe)
            self.canvas.create_line(470, 850, 510, 850)
            self.canvas.create_text(520, 850, text = 8 * self.f_angabe)
        elif self.anzahl == 9:
            self.canvas.create_line(470, 350, 510, 350)
            self.canvas.create_text(520, 350, text = 0)
            self.canvas.create_line(470, 405, 510, 405)
            self.canvas.create_text(520, 405, text = 1 * self.f_angabe)
            self.canvas.create_line(470, 461, 510, 461)
            self.canvas.create_text(520, 461, text = 2 * self.f_angabe)
            self.canvas.create_line(470, 516, 510, 516)
            self.canvas.create_text(520, 516, text = 3 * self.f_angabe)
            self.canvas.create_line(470, 572, 510, 572)
            self.canvas.create_text(520, 572, text = 4 * self.f_angabe)
            self.canvas.create_line(470, 627, 510, 627)
            self.canvas.create_text(520, 627, text = 5 * self.f_angabe)
            self.canvas.create_line(470, 683, 510, 683)
            self.canvas.create_text(520, 683, text = 6 * self.f_angabe)
            self.canvas.create_line(470, 738, 510, 738)
            self.canvas.create_text(520, 738, text = 7 * self.f_angabe)
            self.canvas.create_line(470, 794, 510, 794)
            self.canvas.create_text(520, 794, text = 8 * self.f_angabe)
            self.canvas.create_line(470, 850, 510, 850)
            self.canvas.create_text(520, 850, text = 9 * self.f_angabe)
        self.canvas.create_text(550, 600, text = self.f)
        self.canvas.create_line(MID_Y, 300, MID_Y, 900)
        self.canvas.create_text(MID_Y, 250, text = m2)
        self.canvas.create_text(MID_Y, 950, text = m1)
window = Tk()
window.title("Gravitationssimulation")

a = None
b = None


def click_berechnen_button():
    global a, b
    
    m1 = lm1.get()
    m2 = lm2.get()
    dist = ldist.get()
    f = (G * (float(m1)) * (float(m2)) / (float(dist)) ** 2)
    disp_txt = 'Fg = {:3.3e}'.format(f)
    ergebnis_fg.set(disp_txt)
    if a is None:
        a = SpaceObject(c, m1,  (MID_X + 250), MID_Y, True)
        a.bounce()
        a.draw()
    if b is None:
        b = SpaceObject(c,  m2, (MID_X - 250), MID_Y, False)
        b.bounce()
        b.draw()
    z = FG(c,  f, dist,  m1,  m2)


frame = Frame(window)
frame.pack(side=LEFT)
s_m1 = StringVar()
s_m2 = StringVar()
s_dist = StringVar()

s_m1.set('1000')
s_m2.set('2000')
s_dist.set('10000')

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
