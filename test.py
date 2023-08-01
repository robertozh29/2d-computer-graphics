import tkinter as tk
import numpy as np

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class App:

    def __init__(self):
        self.root = tk.Tk()

        # Contenedor principal
        contenedor_fm = tk.Frame(self.root)
        contenedor_fm.pack(fill='both', expand=1)

        # Frame para valores de entrada
        fm1 = tk.Frame(contenedor_fm)
        fm1.grid(row=0, column=0, padx=5, pady=10)

        # Frame para resultados
        fm2 = tk.Frame(contenedor_fm)
        fm2.grid(row=1, column=0, padx=5, pady=10)

        # Frame para gráficos
        fm3 = tk.Frame(contenedor_fm)
        fm3.grid(row=2, column=0, padx=55, pady=10)

        # Widgets para fm1
        tk.Label(fm1, text='Ingrese base y altura'
            ).grid(row=0, column=0, columnspan=4)
        tk.Label(fm1, text='Base:'
            ).grid(row=1, column=0, sticky='e')
        tk.Label(fm1, text='Altura:'
            ).grid(row=1, column=2, sticky='e')

        # Función para cuando se presione el botón
        def calcular():
            area.set(base.get() * altura.get())

            # Widgets para fm3
            b = np.array([0, base.get(), base.get(), 0, 0])
            a = np.array([0, 0, altura.get(), altura.get(), 0])

            figura = Figure(figsize=(2, 2), dpi=100)
            ax1 = figura.add_subplot(111)
            ax1.plot(b, a)

            canvas = FigureCanvasTkAgg(figura, master=fm3)
            canvas.draw()
            canvas.get_tk_widget().grid(padx=25)

        # Valores dados por el usuario
        base = tk.IntVar(value=0) 
        altura = tk.IntVar(value=0)
        area = tk.IntVar(value=0)

        base_entry = tk.Entry(fm1, textvariable=base, 
            width=5)
        base_entry.grid(row=1, column=1, sticky='w')

        altura_entry = tk.Entry(fm1, textvariable=altura, 
            width=5)
        altura_entry.grid(row=1, column=3)

        # Botón para realizar el cálculo
        calcular_btn = tk.Button(fm1, text='Calcular',
            command=calcular)
        calcular_btn.grid(row=2, column=0, columnspan=4)

        # Widgets para fm2
        tk.Label(fm2, text='El área de polígono es:'
            ).grid(row=0, column=0)
        tk.Label(fm2, textvariable=area).grid(row=0, column=1)

    def mainloop(self):
        self.root.mainloop()

if __name__ == '__main__':
    ejemplo = App()
    ejemplo.mainloop()
