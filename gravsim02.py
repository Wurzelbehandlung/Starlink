from tkinter import *

# m1 = input("wie schwer?(kg)")
# m2 = input("wie schwer?(zweite masse)(kg)")
# r = input ("wie weit ausseinander?(m)")

m1 = 1.0e6   # in kg
m2 = 2.0e9   # in kg
r = 1e6      # in m

HEIGHT = 500
WIDTH = 800
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2

window = Tk()
window.title("Gravitationssimulation")


def click_berechnen_button():
    # Das hier soll passieren, wenn man auf den Button klickt.
    # Hier sollte eigentlich die Berechnung gemacht werden. Wird sie aber noch nicht. ;)

    # Mit s_mass1.get() krieg ich raus, was drin steht,
    # und mit float(...) wirds in eine Zahl umgewandelt.
    m = float(s_mass1.get())
    # mit 'blah blahb blah {...}'.format(m) wirds hübsch formatiert.
    # Das hier heißt genaugenommen:
    # "Schreib 'Fg = ' davor, und schreib dann die Zahl in m mit 3 Nachkommastellen in Exponential-Schreibweise hin.
    disp_txt = 'Fg = {:3.3e}'.format(m)
    # Und hier wirds jetzt eeeeendlich angezeigt:
    ergebnis_fg.set(disp_txt)


# Alles mit  Benutzer-Oberfläche ab hier:
frame = Frame(window)
frame.pack(side=LEFT)

# Die sind dazu da, damit man die Werte von den Text-Feldern auslesen kann.
s_mass1 = StringVar()
s_mass2 = StringVar()
s_dist = StringVar()

# Label ist einfach eine Text-Anzeige
l_mass1 = Label(frame, text="Masse 1 [kg]")
l_mass1.pack(side=TOP)
# Entry ist eine Text-Eingabe
e_mass1 = Entry(frame, textvariable=s_mass1)
e_mass1.pack(side=TOP)

l_mass2 = Label(frame, text="Masse 2 [kg]")
l_mass2.pack(side=TOP)
e_mass2 = Entry(frame, textvariable=s_mass2)
e_mass2.pack(side=TOP)

l_dist = Label(frame, text="Abstand [m]")
l_dist.pack(side=TOP)
e_dist = Entry(frame, textvariable=s_dist)
e_dist.pack(side=TOP)

ergebnis_fg = StringVar()

# Wieder ein Label, aber diesmal hat sie nicht "text" sondern "textvariable", d.h. wir können ändern, was drin steht.
l_kraft = Label(frame, textvariable=ergebnis_fg)
l_kraft.pack(side=BOTTOM)

# Button ist.. na was wohl, ein Button. :D
b_rechnen = Button(frame, text="Berechnen", command=click_berechnen_button)
b_rechnen.pack(side=BOTTOM)

# Yeah, und wie schon vorher, das Canvas, auf dem wir alles zeichnen können, was wir wollen.
c = Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
c.pack()

pl_1 = c.create_oval(0, 0, 30, 30, fill="blue")
G = 0.00000000006674
c.create_text(50, 30, text="Vorschläge(kg):", fill="white")
pl_m = ["Sonne_199e28", "Merkur_3301e20", "Mars_6417e20", "Erde_59724e20",
        "Venus_4875e21", "Jupiter_1899e24", "Saturn_5683e26", "Uranus_8681e22",
        "Neptun_1024e23"]
c.create_text(400, 50, text=str(pl_m), fill="white", font=("Calibri", 8))
c.move(pl_1, MID_X+200, MID_Y)

dx = 0.1
dy = 0.1


class SpaceObject:
    def __init__(self, canvas, color, radius):
        self.canvas = canvas
        self.radius = radius
        self.id = canvas.create_oval(0, 0, radius, radius, fill=color)
        self.canvas.move(self.id, MID_X+100, MID_Y+50)
        self.velocity = [0, 0]

    def draw(self):
        self.canvas.move(self.id, self.velocity[0], self.velocity[1])
        self.canvas.after(1, self.draw)

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


f = (G * (int(m1)) * (int(m2)) / (int(r)) ** 2)

s = 'Fg = {:3.3e}'.format(f)
ergebnis_fg.set(s)

sun = SpaceObject(c, "red", 50)
sun.velocity = [0.2, -2]
sun.draw()
sun.bounce()
sun.gravity()
# Das hier macht, dass das tkinter-Fenster angezeigt wird:
window.mainloop()
