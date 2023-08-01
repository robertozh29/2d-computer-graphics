from tkinter import *
import customtkinter
import matplotlib
from sidebar_module import SideBarFrame
from mainframe_module import MainFrame

matplotlib.rc('font', size=14)
customtkinter.set_appearance_mode("dark")

ROOT_BG = '#212121' # Root background color
TITLE = "Graficacion por computadora"

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.after(10, lambda: self.state('zoomed'))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ----- Title Bar -----
        self.title(TITLE)
        self.config(bg=ROOT_BG)
        self.iconbitmap('D:/Github/2d-computer-graphics/media/grafico.ico')

        # ----- main_frame -----
        self.main_frame = MainFrame(self, "linea_DDA")

        # ----- side_bar -----
        self.sidebar = SideBarFrame(self)
        self.sidebar.grid(column=0, row=0, sticky="NS")
        
    def linea_DDA(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "linea_DDA")
        self.main_frame.plot()

    def linea_bresenham(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "linea_bresenham")
        self.main_frame.plot()

    def circulo_DDA(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "circulo_DDA")
        self.main_frame.plot()

    def circulo_punto_medio(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "circulo_punto_medio")
        self.main_frame.plot()

    def elipse_punto_medio(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "elipse_punto_medio")
        self.main_frame.plot()
    
    def parabola(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "parabola")
        self.main_frame.plot()

ventana = Root()
ventana.mainloop()