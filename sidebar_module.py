from tkinter import *
import customtkinter

class SideBarFrame(customtkinter.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        titulo = customtkinter.CTkLabel(self, text="Selecciona Algorithmo")
        titulo.grid(row=0, column=0, padx=5, pady=15)

        self.button1 = customtkinter.CTkButton(self, text="Linea por DDA", command=root.linea_DDA)
        self.button1.grid(column=0, row=1, padx=30, pady=7, ipadx=50)

        self.button2 = customtkinter.CTkButton(self, text="Linea por Bresenham", command=root.linea_bresenham)
        self.button2.grid(column=0, row=2, padx=30, pady=7, ipadx=50)

        self.button3 = customtkinter.CTkButton(self, text="Circulo por DDA", command=root.circulo_DDA)
        self.button3.grid(column=0, row=3, padx=30, pady=7, ipadx=50)

        self.button4 = customtkinter.CTkButton(self, text="Circulo por punto medio", command=root.circulo_punto_medio)
        self.button4.grid(column=0, row=4, padx=30, pady=7, ipadx=40)

        self.button5 = customtkinter.CTkButton(self, text="Elipse por punto medio", command=root.elipse_punto_medio)
        self.button5.grid(column=0, row=5, padx=30, pady=7, ipadx=46)

        self.button6 = customtkinter.CTkButton(self, text="Parabola", command=root.parabola)
        self.button6.grid(column=0, row=6, padx=30, pady=7, ipadx=52)

        self.button7 = customtkinter.CTkButton(self, text="Clear all", command=root.destroy, fg_color="red", hover_color="#b20101")
        self.button7.grid(column=0, row=7, padx=30, pady=(7,25), ipadx=52, sticky="S")
        self.rowconfigure(7, weight=1)

    def h(self):
        pass