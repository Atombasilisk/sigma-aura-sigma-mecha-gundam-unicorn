import tkinter as tk
from cam import Cam
from PIL import ImageTk, Image

import time
from serial.tools import list_ports
import pydobot




            
      
class Dobot_dummy():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def pose(self):
        return self.x,self.y,self.z,0,0,0,0,0

    def move_to(self, x,y,z,r, wait=False):
        if wait:
            time.sleep(0.01)
        self.x = x
        self.y = y
        self.z = z
        return None

class Main(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)

        # Hvis I ikke har noget USB-kamera tilkoblet,
        # skal I formentlig bruge Cam(0) for at få fat i
        # kameraet på jeres skærm.
        # Hvis I sætter et USB-kamera til, skal I
        # formentlig bruge Cam(1)
        self.cam = Cam(0)


        self.create_interface()

        ports = list_ports.comports()

        # Sæt simulate = True hvis I ikke har en robot
        # Sæt simulate = False hvis I har en robot
        simulate = False
        if simulate:
            self.dobot = Dobot_dummy()
        else:
            for i, port in enumerate(ports):
                print(f"{i}: {port.device} ({port.description})")
            #p = int(input("Port: "))
            p = 0
            port = None
            if len(ports) > 0 and len(ports) > p:
                port = ports[p].device

            #device = pydobot.Dobot(port=port, verbose=True)
            self.dobot = pydobot.Dobot(port=port)

        self.update_view()

    

    def get_color(self):
        
        self.megasejfarvethorleif = ("aura")
        xgul = 200
        ygul = 200
    
        col = self.cam.read_color(xgul,ygul)

        r = col[0]
        g = col[1]
        b = col[2]

        if r > 120 and g < 150 and b < 150:
            self.lbl_colour.config(text="Rød")
            self.megasejfarvethorleif = "Rød"
        else:
            pass
        if g > 120 and b < 150 and r < 150:
            self.lbl_colour.config(text="grøn")
            self.megasejfarvethorleif = "grøn"
        else:
            pass
        if b > 120 and r < 150 and g < 150:
            self.lbl_colour.config(text="blå")
            self.megasejfarvethorleif = "blå"
            
        else:
            pass
        if b == 255 and r == 255 and g == 255:
            self.lbl_colour.config(text="hvid")
            self.megasejfarvethorleif = "hvid"
            
        else:
            pass
        if b > 120 and r < 120 and g < 120:
            self.lbl_colour.config(text="gul")
            self.megasejfarvethorleif = "gul"
        
    
        


    def get_red(self):
        if self.megasejfarvethorleif == "Rød":
            print(self.megasejfarvethorleif)
            for xred in [1..16] and yred in [1..16]:
                self.dobot.move_to(self, xred*10+200,yred*10+200,100,90, wait=False)  
        else:
            pass
        
    def get_yellow(self):
        if self.megasejfarvethorleif == "grøn":
            print(self.megasejfarvethorleif)
                
        else:
            pass
    def get_blå(self):
        if self.megasejfarvethorleif == "blå":
            print(self.megasejfarvethorleif)
        
        else:
            pass
    def get_grøn(self):
        if self.megasejfarvethorleif == "gul":
            print(self.megasejfarvethorleif)  
        else:
            pass
    # Denne funktion kører automatisk, og sørger for at vise billedet fra kameraet
    # og farven på en udvalgt pixel.
    def update_view(self):
        self.cam.make_frame()

        frame = self.cam.frame
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lbl_show_frame.imgtk = imgtk
        self.lbl_show_frame.configure(image=imgtk)
        col = self.cam.read_color(240,320)
        self.lbl_indicator.configure(bg=self._from_rgb(col))

        self.after(1, self.update_view)


    # Her oprettes vores brugerinterface.
    # I kan selv tilføje de widgets, I har behov for


    def create_interface(self):
        self.main_frame = tk.Frame(self)

        # Tilføj her


        self.but_color = tk.Button(self.main_frame, text="farvetjek", command=self.get_color)
        self.but_red = tk.Button(self.main_frame, text="Rød", command=self.get_red)
        self.but_yellow = tk.Button(self.main_frame, text="Gul", command=self.get_yellow)
        self.but_grøn = tk.Button(self.main_frame, text="Grøn", command=self.get_grøn)
        self.but_blå = tk.Button(self.main_frame, text="Blå", command=self.get_blå)
        self.lbl_indicator = tk.Label(self.main_frame, width=20, height = 5, text = "")
        self.lbl_show_frame = tk.Label(self.main_frame)
        self.lbl_colour = tk.Label(self.main_frame, text="find a color")
        

        
        self.but_color.grid(row=0,column=0)
        self.lbl_show_frame.grid(row=0,column=1, rowspan=2)
        self.main_frame.pack(padx = 20, pady=10)
        self.lbl_indicator.grid(row=6, column=0)
        self.lbl_colour.grid(row=5,column=0)
        self.pack()
        self.but_blå.grid(row=1,column=0)
        self.but_grøn.grid(row=2,column=0)
        self.but_red.grid(row=3,column=0)
        self.but_yellow.grid(row=4,column=0)

    # Denne lille funktion laver farvekoden fra 
    # kameraet om til et format, som tkinter kan bruge
    def _from_rgb(self,rgb):
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'





root = tk.Tk()
root.title("Dobot")

interface = Main()
interface.mainloop()
