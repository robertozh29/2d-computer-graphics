from tkinter import *
import customtkinter
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Modules
from sidebar_module import SideBarFrame

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
        self.main_frame = MainFrame(self, "linea_DDA")

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

"""
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

        self.button6 = customtkinter.CTkButton(self, text="Parabola", command=root.parabola)
        self.button6.grid(column=0, row=6, padx=30, pady=7, ipadx=52)

        self.button7 = customtkinter.CTkButton(self, text="Clear all", command=root.destroy, fg_color="red", hover_color="#b20101")
        self.button7.grid(column=0, row=7, padx=30, pady=(7,25), ipadx=52, sticky="S")
        self.rowconfigure(7, weight=1)
"""

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
        

class Algorithm():
    def __init__(self):
        super().__init__()
    
    def lineDDA(self, x0, y0, x1, y1):
        points = [] # Lista para almacenar los puntos de la línea
        dx = x1 - x0 # Diferencia en x
        dy = y1 - y0 # Diferencia en y

        # Determinar el número de pasos basado en la diferencia más grande entre x y y
        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)

        Xinc = dx / steps # Incremento en x
        Yinc = dy / steps # Incremento en y

        X = x0 # Valor inicial de x
        Y = y0 # Valor inicial de y

        points.append((round(X), round(Y))) # Agregar el primer punto

        # Loop para calcular los puntos de la línea
        for _ in range(steps):
            X += Xinc
            Y += Yinc
            points.append((round(X), round(Y)))

        return points

    # Función para dibujar una línea usando el algoritmo de Bresenham
    def lineBresenham(x0, y0, x1, y1):
        points = [] # Lista para almacenar los puntos de la línea
        dx = abs(x1 - x0) # Diferencia absoluta en x
        dy = abs(y1 - y0) # Diferencia absoluta en y

        # Determinar la dirección de los incrementos en x y y
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1

        err = dx - dy

        # Loop para calcular los puntos de la línea
        while True:
            points.append((x0, y0))
            if x0 == x1 and y0 == y1:
                break

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

        return points

    # Función para dibujar un círculo usando el algoritmo DDA
    def circleDDA(xc, yc, r):
        points = [] # Lista para almacenar los puntos del círculo
        X = r
        Y = 0

        # Agregar puntos iniciales en los ejes
        points.append((xc + X, yc + Y))
        points.append((xc - X, yc - Y))
        points.append((xc + Y, yc + X))
        points.append((xc - Y, yc + X))

        P = 1 - r # Parámetro inicial

        # Loop para calcular los puntos del círculo en el primer octante
        while X > Y:
            Y += 1
            if P <= 0:
                P = P + 2 * Y + 1
            else:
                X -= 1
                P = P + 2 * Y - 2 * X + 1

            # Agregar puntos en todos los octantes
            points.append((xc + X, yc + Y))
            points.append((xc - X, yc + Y))
            points.append((xc + X, yc - Y))
            points.append((xc - X, yc - Y))
            points.append((xc + Y, yc + X))
            points.append((xc - Y, yc + X))
            points.append((xc + Y, yc - X))
            points.append((xc - Y, yc - X))

        return points

    # Función para dibujar un círculo usando el algoritmo de punto medio
    def circleMidPoint(xc, yc, r):
        points = [] # Lista para almacenar los puntos del círculo
        x = 0
        y = r
        P = 1 - r # Parámetro inicial

        # Agregar puntos iniciales en los ejes
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))
        points.append((xc + y, yc + x))
        points.append((xc - y, yc + x))
        points.append((xc + y, yc - x))
        points.append((xc - y, yc - x))

        # Loop para calcular los puntos del círculo en el primer octante
        while x < y:
            x += 1
            if P < 0:
                P = P + 2 * x + 1
            else:
                y -= 1
                P = P + 2 * x - 2 * y + 1

            # Agregar puntos en todos los octantes
            points.append((xc + x, yc + y))
            points.append((xc - x, yc + y))
            points.append((xc + x, yc - y))
            points.append((xc - x, yc - y))
            points.append((xc + y, yc + x))
            points.append((xc - y, yc + x))
            points.append((xc + y, yc - x))
            points.append((xc - y, yc - x))

        return points

    # Función para dibujar una elipse usando el algoritmo de punto medio
    def ellipseMidPoint(xc, yc, rx, ry):
        points = [] # Lista para almacenar los puntos de la elipse
        x = 0
        y = ry
        P1 = (ry * ry) - (rx * rx * ry) + (0.25 * rx * rx) # Parámetro inicial en la región 1
        dx = 2 * ry * ry * x
        dy = 2 * rx * rx * y

        # Loop para calcular los puntos de la elipse en la región 1
        while dx < dy:
            points.append((xc + x, yc + y))
            points.append((xc - x, yc + y))
            points.append((xc + x, yc - y))
            points.append((xc - x, yc - y))

            if P1 < 0:
                x += 1
                dx = dx + (2 * ry * ry)
                P1 = P1 + dx + (ry * ry)
            else:
                x += 1
                y -= 1
                dx = dx + (2 * ry * ry)
                dy = dy - (2 * rx * rx)
                P1 = P1 + dx - dy + (ry * ry)

        P2 = ((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry) # Parámetro inicial en la región 2

        # Loop para calcular los puntos de la elipse en la región 2
        while y >= 0:
            points.append((xc + x, yc + y))
            points.append((xc - x, yc + y))
            points.append((xc + x, yc - y))
            points.append((xc - x, yc - y))

            if P2 > 0:
                y -= 1
                dy = dy - (2 * rx * rx)
                P2 = P2 + (rx * rx) - dy
            else:
                y -= 1
                x += 1
                dx = dx + (2 * ry * ry)
                dy = dy - (2 * rx * rx)
                P2 = P2 + dx - dy + (rx * rx)

        return points

    # Calcular coordenadas parabola
    def parabola(x0, y0, x1, y1):
        points = [] # Lista para almacenar los puntos de la parábola
        dx = x1 - x0 # Diferencia en x
        dy = y1 - y0 # Diferencia en y
        y = y0
        p = dy - dx / 2 # Parámetro inicial

        # Loop para calcular los puntos de la parábola
        while y <= y1:
            points.append((x0, y))
            if p < 0:
                x0 += 1
                p = p + dy
            else:
                x0 += 1
                y += 1
                p = p + dy - dx

        return points


ventana = Root()
ventana.mainloop()