import math
from math import sqrt
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox, colorchooser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Función para dibujar una línea usando el algoritmo DDA
def lineDDA(x0, y0, x1, y1):
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

    print(points)
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

# Función para dibujar una parábola
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

# Función para pedir al usuario los parámetros necesarios para dibujar la figura seleccionada
def ask_parameters(option):
    color = colorchooser.askcolor(title ="Elige un color")[1] # Pedir al usuario que seleccione un color
    if color is None:  # Si el usuario cancela la selección de color, se utilizará el color azul por defecto.
        color = 'blue'

    # Solicitar los parámetros según la opción seleccionada
    if option == 1:
        x0 = simpledialog.askinteger("Input", "Ingrese el valor de X inicial:")
        y0 = simpledialog.askinteger("Input", "Ingrese el valor de Y inicial:")
        x1 = simpledialog.askinteger("Input", "Ingrese el valor de X final:")
        y1 = simpledialog.askinteger("Input", "Ingrese el valor de Y final:")
        return lineDDA(x0, y0, x1, y1), color
    elif option == 2:
        x0 = simpledialog.askinteger("Input", "Ingrese el valor de X inicial:")
        y0 = simpledialog.askinteger("Input", "Ingrese el valor de Y inicial:")
        x1 = simpledialog.askinteger("Input", "Ingrese el valor de X final:")
        y1 = simpledialog.askinteger("Input", "Ingrese el valor de Y final:")
        return lineBresenham(x0, y0, x1, y1), color
    elif option == 3:
        r = simpledialog.askinteger("Input", "Ingrese el valor del radio:")
        xc = simpledialog.askinteger("Input", "Ingrese el valor de X central:")
        yc = simpledialog.askinteger("Input", "Ingrese el valor de Y central:")
        return circleDDA(xc, yc, r), color
    elif option == 4:
        r = simpledialog.askinteger("Input", "Ingrese el valor del radio:")
        xc = simpledialog.askinteger("Input", "Ingrese el valor de X central:")
        yc = simpledialog.askinteger("Input", "Ingrese el valor del Y central:")
        return circleMidPoint(xc, yc, r), color
    elif option == 5:
        rx = simpledialog.askinteger("Input", "Ingrese el valor del radio en X:")
        ry = simpledialog.askinteger("Input", "Ingrese el valor del radio en Y:")
        xc = simpledialog.askinteger("Input", "Ingrese el valor de X central:")
        yc = simpledialog.askinteger("Input", "Ingrese el valor de Y central:")
        return ellipseMidPoint(xc, yc, rx, ry), color
    elif option == 6:
        x0 = simpledialog.askinteger("Input", "Ingrese el valor de X inicial:")
        y0 = simpledialog.askinteger("Input", "Ingrese el valor de Y inicial:")
        x1 = simpledialog.askinteger("Input", "Ingrese el valor de X final:")
        y1 = simpledialog.askinteger("Input", "Ingrese el valor de Y final:")
        return parabola(x0, y0, x1, y1), color

# Función para dibujar la figura seleccionada
def draw(option, root):
    if option == 7: # Si se selecciona la opción 7, salir del programa
        root.quit()
    else:
        points_color = ask_parameters(option) # Obtener los puntos y color para la figura seleccionada
        if points_color is not None:
            points, color = points_color
            root.withdraw() # Ocultar la ventana principal

            new_window = tk.Toplevel(root) # Crear una nueva ventana
            new_window.wm_title("Gráfica")

            fig = Figure(figsize=(5, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(*zip(*points), 'o', color=color) # Graficar los puntos en la nueva ventana

            canvas = FigureCanvasTkAgg(fig, master=new_window) # Agregar el gráfico de Matplotlib a la ventana
            canvas.draw()
            canvas.get_tk_widget().pack()

            # Botón para regresar al menú principal
            button = tk.Button(new_window, text="Regresar al menú", command=lambda: [new_window.destroy(), root.deiconify()])
            button.pack()

            # Botón para salir del programa
            exit_button = tk.Button(new_window, text="Salir del programa", command=root.quit)
            exit_button.pack()

# Función principal para ejecutar la aplicación
def main():
    root = tk.Tk()

    # Opciones del menú principal
    options = [
        ("1. Dibujar línea con DDA", 1),
        ("2. Dibujar línea con Bresenham", 2),
        ("3. Dibujar círculo con DDA", 3),
        ("4. Dibujar círculo con punto medio", 4),
        ("5. Dibujar elipse con punto medio", 5),
        ("6. Dibujar parábola", 6),
        ("7. Salir del programa", 7)
    ]

    # Agregar los botones para cada opción en el menú principal
    for text, value in options:
        button = tk.Button(root, text=text, command=lambda value=value: draw(value, root))
        button.pack()

    root.mainloop() # Iniciar el loop principal de la aplicación

if __name__ == "__main__":
    main() # Ejecutar la función principal



