from tkinter import *
import customtkinter
from algorithm_module import Algorithm

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, root, algorithm):
        super().__init__(root)
        self.grid(column=1, row=0, sticky="NSEW", padx=(15,0))
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0,1), weight=1)

        algorithm_frame = AlgorithmFrame(self, algorithm)
        algorithm_frame.grid(column=0, row=0, columnspan=2, sticky="NSEW", padx=2, pady=2)
        
        self.frame_chart = customtkinter.CTkFrame(self, width=300, height=300)
        self.frame_chart.grid(column=0, row=1, sticky="NSEW", padx=2, pady=2)

        self.frame_logs = customtkinter.CTkFrame(self, width=300, height=300)
        self.frame_logs.grid(column=1, row=1, sticky="NSEW", padx=2, pady=2)
    
    def plot(self, coordinates = [(96,96)]):
        self.update()
        chart_height= self.frame_chart.winfo_height()
        fig = Figure(figsize = (chart_height/100, chart_height/100), dpi = 100)
        fig.set_facecolor('#333')
        
        plot1 = fig.add_subplot(111)
        plot1.set_facecolor("#212121")
        plot1.tick_params(axis='both', colors='white')
        plot1.plot(*zip(*coordinates))
    
        self.canvas = FigureCanvasTkAgg(fig, master = self.frame_chart)  
        self.canvas.draw()
        self.canvas.get_tk_widget().grid()

class AlgorithmFrame(customtkinter.CTkFrame):
    def __init__(self,parentFrame, algorithm):
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

            graph = customtkinter.CTkButton(self, text="Graficar", command= lambda: self.get_values(parentFrame, entries))
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

            graph = customtkinter.CTkButton(self, text="Graficar", command=self.destroy)
            graph.grid(column=0, row=2, padx=20, pady=(10,25), columnspan=4, sticky="WE")

        elif(algorithm == "circulo_DDA"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Circulo por DDA", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=3, pady=20, sticky="WE")

            radio = customtkinter.CTkEntry(self, placeholder_text="Radio")
            radio.grid(column=0, row=1, padx=20, pady=(20,10), sticky="WE")

            Xc = customtkinter.CTkEntry(self, placeholder_text="X Central")
            Xc.grid(column=1, row=1, padx=10, pady=(20,10), sticky="WE")
            
            Yc = customtkinter.CTkEntry(self, placeholder_text="Y Central")
            Yc.grid(column=2, row=1, padx=10, pady=(20,10), sticky="WE")

            graph = customtkinter.CTkButton(self, text="Graficar", command=self.destroy)
            graph.grid(column=0, row=2, padx=15, pady=(10,25), columnspan=3, sticky="WE")

        elif(algorithm == "circulo_punto_medio"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Circulo por punto medio", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=3, pady=20, sticky="WE")

            radio = customtkinter.CTkEntry(self, placeholder_text="Radio")
            radio.grid(column=0, row=1, padx=20, pady=(20,10), sticky="WE")

            Xc = customtkinter.CTkEntry(self, placeholder_text="X Central")
            Xc.grid(column=1, row=1, padx=10, pady=(20,10), sticky="WE")
            
            Yc = customtkinter.CTkEntry(self, placeholder_text="Y Central")
            Yc.grid(column=2, row=1, padx=10, pady=(20,10), sticky="WE")

            graph = customtkinter.CTkButton(self, text="Graficar", command=self.destroy)
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

            graph = customtkinter.CTkButton(self, text="Graficar", command=self.destroy)
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

            graph = customtkinter.CTkButton(self, text="Graficar", command=self.destroy)
            graph.grid(column=0, row=2, padx=20, pady=(10,25), columnspan=4, sticky="WE")
            
    def get_values(self, parentFrame, entries):
        algorithm = Algorithm()
        e1 = [int(value.get()) for value in entries]
        coordinates = algorithm.lineDDA(e1[0], e1[1], e1[2], e1[3])
        
        print(coordinates)
        parentFrame.plot(coordinates)
        