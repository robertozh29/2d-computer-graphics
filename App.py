from tkinter import * 
import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Root import Root

class DefaultFrame(Root):
    def __init__(self):
        super().__init__()
        main_frame = customtkinter.CTkFrame(self)
        main_frame.grid(column=1, row=0, sticky="NSEW", padx=(15,0))
        

# ventana = App()
# ventana.mainloop()