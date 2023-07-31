from tkinter import *
import customtkinter
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

        # ----- side_bar -----
        self.sidebar = SideBarFrame(self)
        self.sidebar.grid(column=0, row=0, sticky="NS")
        
        # ----- main_frame -----
        self.main_frame = MainFrame(self, "circulo_DDA")
        self.plot(self.main_frame.frame_chart)

    def linea_bresenham(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "linea_bresenham")
        self.plot(self.main_frame.frame_chart)

    def linea_DDA(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "linea_DDA")
        self.plot(self.main_frame.frame_chart)

    def circulo_DDA(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "circulo_DDA")
        self.plot(self.main_frame.frame_chart)

    def circulo_punto_medio(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "circulo_punto_medio")
        self.plot(self.main_frame.frame_chart)

    def elipse_punto_medio(self):
        self.main_frame.destroy()
        self.main_frame = MainFrame(self, "elipse_punto_medio")
        self.plot(self.main_frame.frame_chart)

    def plot(self, frame):
        self.update()
        chart_height= frame.winfo_height()
        fig = Figure(figsize = (chart_height/100, chart_height/100), dpi = 100)
        fig.set_facecolor('#333')
        
        y = [i**2 for i in range(101)]
        plot1 = fig.add_subplot(111)
        plot1.set_facecolor("#212121")
        plot1.tick_params(axis='both', colors='white')
        plot1.plot(y)
    
        canvas = FigureCanvasTkAgg(fig, master = frame)  
        canvas.draw()

        canvas.get_tk_widget().grid()
        canvas.get_tk_widget().grid()
        
    def lineDDA(self, x0, y0, x1, y1):
        points = []
        dx = x1 - x0
        dy = y1 - y0

        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)

        Xinc = dx / steps
        Yinc = dy / steps

        X = x0
        Y = y0

        points.append((round(X), round(Y)))

        for _ in range(steps):
            X += Xinc
            Y += Yinc
            points.append((round(X), round(Y)))

        return points
    
class SideBarFrame(customtkinter.CTkFrame):
    def __init__(self, root: Root):
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

        self.button6 = customtkinter.CTkButton(self, text="Parabola", command=root.destroy)
        self.button6.grid(column=0, row=6, padx=30, pady=7, ipadx=52)

        self.button7 = customtkinter.CTkButton(self, text="Clear all", command=root.destroy, fg_color="red", hover_color="#b20101")
        self.button7.grid(column=0, row=7, padx=30, pady=(7,25), ipadx=52, sticky="S")
        self.rowconfigure(7, weight=1)

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

class AlgorithmFrame(customtkinter.CTkFrame):
    def __init__(self, root, algorithm):
        super().__init__(root)
        
        self.grid_columnconfigure((0,1,2,3), weight=1)

        if(algorithm == "linea_DDA"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Linea por DDA", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=4,  pady=20, sticky="EW")

            x0 = customtkinter.CTkEntry(self, placeholder_text="X0")
            x0.grid(column=0, row=1, padx=(20,10), pady=(20,40), sticky="WE")

            y0 = customtkinter.CTkEntry(self, placeholder_text="Y0")
            y0.grid(column=1, row=1, padx=10, pady=(20,40), sticky="WE")
            
            x1 = customtkinter.CTkEntry(self, placeholder_text="X1")
            x1.grid(column=2, row=1, padx=10, pady=(20,40), sticky="WE")

            y1 = customtkinter.CTkEntry(self, placeholder_text="Y1")
            y1.grid(column=3, row=1, padx=(10,20), pady=(20,40), sticky="WE")

        elif(algorithm == "linea_bresenham"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Linea por Bresenham", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=4,  pady=20, sticky="EW")

            x0 = customtkinter.CTkEntry(self, placeholder_text="X0")
            x0.grid(column=0, row=1, padx=(20,10), pady=(20,40), sticky="WE")

            y0 = customtkinter.CTkEntry(self, placeholder_text="Y0")
            y0.grid(column=1, row=1, padx=10, pady=(20,40), sticky="WE")
            
            x1 = customtkinter.CTkEntry(self, placeholder_text="X1")
            x1.grid(column=2, row=1, padx=10, pady=(20,40), sticky="WE")

            y1 = customtkinter.CTkEntry(self, placeholder_text="Y1")
            y1.grid(column=3, row=1, padx=(10,20), pady=(20,40), sticky="WE")

        elif(algorithm == "circulo_DDA"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Circulo por DDA", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=3, pady=20, sticky="WE")

            radio = customtkinter.CTkEntry(self, placeholder_text="Radio")
            radio.grid(column=0, row=1, padx=20, pady=(20,40), sticky="WE")

            Xc = customtkinter.CTkEntry(self, placeholder_text="X Central")
            Xc.grid(column=1, row=1, padx=10, pady=(20,40), sticky="WE")
            
            Yc = customtkinter.CTkEntry(self, placeholder_text="Y Central")
            Yc.grid(column=2, row=1, padx=10, pady=(20,40), sticky="WE")

        elif(algorithm == "ciruclo_punto_medio"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Circulo por punto medio", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=3, pady=20, sticky="WE")

            radio = customtkinter.CTkEntry(self, placeholder_text="Radio")
            radio.grid(column=0, row=1, padx=20, pady=(20,40), sticky="WE")

            Xc = customtkinter.CTkEntry(self, placeholder_text="X Central")
            Xc.grid(column=1, row=1, padx=10, pady=(20,40), sticky="WE")
            
            Yc = customtkinter.CTkEntry(self, placeholder_text="Y Central")
            Yc.grid(column=2, row=1, padx=10, pady=(20,40), sticky="WE")

        elif(algorithm == "elipse_punto_medio"):
            titulo_inputs = customtkinter.CTkLabel(self, text="Elipse por punto medio", font=("helvetica", 20))
            titulo_inputs.grid(row=0, column=0, columnspan=3, pady=20, sticky="WE")

            Xc = customtkinter.CTkEntry(self, placeholder_text="X Central")
            Xc.grid(column=1, row=1, padx=10, pady=(20,40), sticky="WE")
            
            Yc = customtkinter.CTkEntry(self, placeholder_text="Y Central")
            Yc.grid(column=2, row=1, padx=10, pady=(20,40), sticky="WE")

            Rx = customtkinter.CTkEntry(self, placeholder_text="Radio X")
            Rx.grid(column=1, row=1, padx=10, pady=(20,40), sticky="WE")
            
            Ry = customtkinter.CTkEntry(self, placeholder_text="Radio Y")
            Ry.grid(column=2, row=1, padx=10, pady=(20,40), sticky="WE")



ventana = Root()
ventana.mainloop()