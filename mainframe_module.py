from tkinter import *
from tkinter import ttk
import customtkinter
from algorithm_module import Algorithm
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, root, algorithm):
        super().__init__(root)
        self.grid(column=1, row=0, sticky="NSEW", padx=(15,0))
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0,1), weight=1)
        self.plot1 = False

        algorithm_frame = AlgorithmFrame(self, algorithm)
        algorithm_frame.grid(column=0, row=0, columnspan=2, sticky="NSEW", padx=2, pady=2)
        
        self.frame_chart = customtkinter.CTkFrame(self)
        self.frame_chart.grid(column=0, row=1, sticky="NSEW", padx=2, pady=2)
        
        self.frame_logs = customtkinter.CTkScrollableFrame(self, width=300, height=300)
        self.frame_logs.grid(column=1, row=1, sticky="NSEW", padx=2, pady=2)
        self.frame_logs.grid_columnconfigure(0, weight=1)
        self.frame_logs.grid_rowconfigure(0, weight=1)

        #incializando Widgets Grafica
        chart_width = self.winfo_screenwidth()
        self.figura = Figure(figsize = (10, 10), dpi = 100)
        self.axes = self.figura.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.frame_chart)
        self.plot()  

    def show_quadrant_table(self, quadrant_values, quadrant_num):
        print(quadrant_values)
        # Styles para la tabla
        style = ttk.Style(self)
        style.configure("Treeview", background="#333", foreground="white", font=("helvetica", 18), rowheight=100)
        style.configure("Treeview.Heading", font=("helvetica", 20), rowheight=40)

        # Crear y configurar la tabla de cuadrantes
        table = ttk.Treeview(self.frame_logs, columns=("x", "y"), show="headings", selectmode="none")
        table.column("x", width=100, anchor="center")
        table.column("y", width=80, anchor="center")
        table.heading("x", text="Valores de X", anchor="center")
        table.heading("y", text="Valores de Y", anchor="center")

        # Insertar los valores de X e Y en la tabla
        for i, quadrant in enumerate(quadrant_values):
            table.insert("", "end", values=(quadrant[0], quadrant[1]))

        # Mostrar la tabla en el marco especificado
        table.pack(side="left", fill="both", expand=True, padx=5, pady=5)


    def plot(self, coordinates = [(96,96)]):
        self.figura.set_facecolor('#333')
        self.axes .set_facecolor("#212121")
        self.axes .tick_params(axis='both', colors='white')
        self.canvas.get_tk_widget().pack()
        self.axes.clear()
        self.axes.plot(*zip(*coordinates))
        self.canvas.draw()


        if self.plot1 and coordinates != [(96,96)]: 
            # for widget in self.frame_logs.winfo_children():
            #     widget.destroy()

            # l = customtkinter.CTkLabel(self.frame_logs, text = "|    X    |    Y    |")
            # l.grid() 
            # for idx,n in enumerate(coordinates):
            #     if n[0] > 9 or n[1] > 9: 
            #         log = f"(   {n[0]}   ,   {n[1]}   )" 
            #     else: 
            #         log = f"(    {n[0]}    ,    {n[1]}    )" 
            #     l = customtkinter.CTkLabel(self.frame_logs, text = log)
            #     l.grid()   

            self.show_quadrant_table(coordinates, 1)

        self.plot1 = True

    def plot_circle(self, lista_circulo = [(96,96)]):
        coordinates, octantes = lista_circulo
        print(octantes)
        self.figura.set_facecolor('#333')
        self.axes .set_facecolor("#212121")
        self.axes .tick_params(axis='both', colors='white')
        self.canvas.get_tk_widget().grid()
        self.axes.clear()
        self.axes.plot(*zip(*coordinates),'o')
        self.canvas.draw()

        if self.plot1 and coordinates != [(96,96)]: 
            for widget in self.frame_logs.winfo_children():
                widget.destroy()
            i = 0
            for idx,n in enumerate(coordinates):
                print(i)
                if(idx == 0 or i == octantes):
                    o = customtkinter.CTkLabel(self.frame_logs, text = "|      Octante      |")
                    o.grid(pady=(15,0)) 
                    x = customtkinter.CTkLabel(self.frame_logs, text = "|    X    |    Y    |")
                    x.grid() 
                    i = 0
                if n[0] > 9 or n[1] > 9: 
                    log = f"(   {n[0]}   ,   {n[1]}   )" 
                else: 
                    log = f"(    {n[0]}    ,    {n[1]}    )" 

                i= i + 1
                l = customtkinter.CTkLabel(self.frame_logs, text = log)
                l.grid() 

        self.plot1 = True


class AlgorithmFrame(customtkinter.CTkFrame):
    def __init__(self, parentFrame, algorithm):
        super().__init__(parentFrame)
        self.grid_columnconfigure((0,1,2,3), weight=1)

        if(algorithm == "linea_DDA"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Linea por DDA", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=4,  pady=20, sticky="EW")
            
            x0 = customtkinter.CTkEntry(self, placeholder_text="X0")
            x0.grid(column=0, row=1, padx=(20,10), pady=(20,10), sticky="WE")

            y0 = customtkinter.CTkEntry(self, placeholder_text="Y0")
            y0.grid(column=1, row=1, padx=10, pady=(20,10), sticky="WE")
            
            x1 = customtkinter.CTkEntry(self, placeholder_text="X1")
            x1.grid(column=2, row=1, padx=(10,20), pady=(20,10), sticky="WE")

            y1 = customtkinter.CTkEntry(self, placeholder_text="Y1")
            y1.grid(column=3, row=1, padx=(10,20), pady=(20,10), sticky="WE")

            entries = [x0,y0,x1,y1] 
            graph = customtkinter.CTkButton(self, text="Graficar", command=lambda: parentFrame.plot(self.get_coordinates(algorithm, entries)))
            graph.grid(column=0, row=2, padx=20, pady=(10,25), columnspan=4, sticky="WE")

        elif(algorithm == "linea_bresenham"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Linea por Bresenham", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=4,  pady=20, sticky="EW")

            x0 = customtkinter.CTkEntry(self, placeholder_text="X0")
            x0.grid(column=0, row=1, padx=(20,10), pady=(20,10), sticky="WE")

            y0 = customtkinter.CTkEntry(self, placeholder_text="Y0")
            y0.grid(column=1, row=1, padx=10, pady=(20,10), sticky="WE")
            
            x1 = customtkinter.CTkEntry(self, placeholder_text="X1")
            x1.grid(column=2, row=1, padx=10, pady=(20,10), sticky="WE")

            y1 = customtkinter.CTkEntry(self, placeholder_text="Y1")
            y1.grid(column=3, row=1, padx=(10,20), pady=(20,10), sticky="WE")

            entries = [x0,y0,x1,y1] 
            graph = customtkinter.CTkButton(self, text="Graficar", command=lambda: parentFrame.plot(self.get_coordinates(algorithm, entries)))
            graph.grid(column=0, row=2, padx=20, pady=(10,25), columnspan=4, sticky="WE")

        elif(algorithm == "circulo_DDA"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Circulo por DDA", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=3, pady=20, sticky="WE")

            Xc = customtkinter.CTkEntry(self, placeholder_text="X Central")
            Xc.grid(column=1, row=1, padx=10, pady=(20,10), sticky="WE")
            
            Yc = customtkinter.CTkEntry(self, placeholder_text="Y Central")
            Yc.grid(column=2, row=1, padx=10, pady=(20,10), sticky="WE")

            radio = customtkinter.CTkEntry(self, placeholder_text="Radio")
            radio.grid(column=0, row=1, padx=20, pady=(20,10), sticky="WE")

            entries = [Xc,Yc,radio] 
            graph = customtkinter.CTkButton(self, text="Graficar", command=lambda: parentFrame.plot_circle(self.get_coordinates(algorithm, entries)))
            graph.grid(column=0, row=2, padx=15, pady=(10,25), columnspan=3, sticky="WE")

        elif(algorithm == "circulo_punto_medio"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Circulo por punto medio", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=3, pady=20, sticky="WE")

            Xc = customtkinter.CTkEntry(self, placeholder_text="X Central")
            Xc.grid(column=1, row=1, padx=10, pady=(20,10), sticky="WE")
            
            Yc = customtkinter.CTkEntry(self, placeholder_text="Y Central")
            Yc.grid(column=2, row=1, padx=10, pady=(20,10), sticky="WE")

            radio = customtkinter.CTkEntry(self, placeholder_text="Radio")
            radio.grid(column=0, row=1, padx=20, pady=(20,10), sticky="WE")

            entries = [Xc,Yc,radio] 
            graph = customtkinter.CTkButton(self, text="Graficar", command=lambda: parentFrame.plot_circle(self.get_coordinates(algorithm, entries)))
            graph.grid(column=0, row=2, padx=15, pady=(10,25), columnspan=3, sticky="WE")

        elif(algorithm == "elipse_punto_medio"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Elipse por punto medio", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=4, pady=20, sticky="WE")

            Xc = customtkinter.CTkEntry(self, placeholder_text="X Central")
            Xc.grid(column=0, row=1, padx=10, pady=(20,10), sticky="WE")
            
            Yc = customtkinter.CTkEntry(self, placeholder_text="Y Central")
            Yc.grid(column=1, row=1, padx=10, pady=(20,10), sticky="WE")

            Rx = customtkinter.CTkEntry(self, placeholder_text="Radio X")
            Rx.grid(column=2, row=1, padx=10, pady=(20,10), sticky="WE")
            
            Ry = customtkinter.CTkEntry(self, placeholder_text="Radio Y")
            Ry.grid(column=3, row=1, padx=10, pady=(20,10), sticky="WE")

            entries = [Xc,Yc, Rx, Ry] 
            graph = customtkinter.CTkButton(self, text="Graficar", command=lambda: parentFrame.plot_circle(self.get_coordinates(algorithm, entries)))
            graph.grid(column=0, row=2, padx=20, pady=(10,25), columnspan=4, sticky="WE")

        elif(algorithm == "parabola"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Parabola", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=4,  pady=20, sticky="EW")

            x0 = customtkinter.CTkEntry(self, placeholder_text="X0")
            x0.grid(column=0, row=1, padx=(20,10), pady=(20,10), sticky="WE")

            y0 = customtkinter.CTkEntry(self, placeholder_text="Y0")
            y0.grid(column=1, row=1, padx=10, pady=(20,10), sticky="WE")
            
            x1 = customtkinter.CTkEntry(self, placeholder_text="X1")
            x1.grid(column=2, row=1, padx=10, pady=(20,10), sticky="WE")

            y1 = customtkinter.CTkEntry(self, placeholder_text="Y1")
            y1.grid(column=3, row=1, padx=(10,20), pady=(20,10), sticky="WE")

            entries = [x0,y0,x1,y1] 
            graph = customtkinter.CTkButton(self, text="Graficar", command=lambda: parentFrame.plot_circle(self.get_coordinates(algorithm, entries)))
            graph.grid(column=0, row=2, padx=20, pady=(10,25), columnspan=4, sticky="WE")
            
    def get_coordinates(self, opc, entries):
        algorithm = Algorithm()
        e1 = [int(value.get()) for value in entries]
        if opc == "linea_DDA":
            coordinates = algorithm.lineDDA(e1[0], e1[1], e1[2], e1[3])
        elif opc == "linea_bresenham":
            coordinates = algorithm.lineBresenham(e1[0], e1[1], e1[2], e1[3])
        elif opc == "circulo_DDA":
            coordinates = algorithm.circleDDA2(e1[0], e1[1], e1[2])
        elif opc == "circulo_punto_medio":
            coordinates = algorithm.circleMidPoint(e1[0], e1[1], e1[2])
        elif opc == "elipse_punto_medio":
            coordinates = algorithm.ellipseMidPoint(e1[0], e1[1], e1[2], e1[3])
        elif opc == "parabola":
            coordinates = algorithm.parabola(e1[0], e1[1], e1[2], e1[3])

        return coordinates
        