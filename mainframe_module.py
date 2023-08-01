from tkinter import *
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

        #incializando Widgets Grafica
        chart_height = self.winfo_screenheight()
        self.figura = Figure(figsize = (chart_height/100 * 1.5, chart_height/100 * 1.5), dpi = 100)
        self.axes = self.figura.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.frame_chart)
        self.plot()  

    def plot(self, coordinates = [(96,96)]):
        self.figura.set_facecolor('#333')
        self.axes .set_facecolor("#212121")
        self.axes .tick_params(axis='both', colors='white')
        self.canvas.get_tk_widget().grid()
        self.axes.clear()
        self.axes.plot(*zip(*coordinates))
        self.canvas.draw()

        if self.plot1 and coordinates != [(96,96)]: 
            for widget in self.frame_logs.winfo_children():
                widget.destroy()
            for idx,n in enumerate(coordinates):
                log = f"{idx}: {n}" 
                l = customtkinter.CTkLabel(self.frame_logs, text = log)
                l.grid()   

        self.plot1 = True

    def plot_circle(self, coordinates = [(96,96)]):
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
            for idx,n in enumerate(coordinates):
                log = f"{idx}: {n}" 
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
            coordinates = algorithm.circleDDA(e1[0], e1[1], e1[2])
        elif opc == "circulo_punto_medio":
            coordinates = algorithm.circleMidPoint(e1[0], e1[1], e1[2])
        elif opc == "elipse_punto_medio":
            coordinates = algorithm.ellipseMidPoint(e1[0], e1[1], e1[2], e1[3])
        elif opc == "parabola":
            coordinates = algorithm.parabola(e1[0], e1[1], e1[2], e1[3])

        return coordinates
        