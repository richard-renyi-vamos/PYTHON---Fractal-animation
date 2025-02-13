import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    fractal = np.empty((height, width))
    
    for i in range(height):
        for j in range(width):
            fractal[i, j] = mandelbrot(complex(x[j], y[i]), max_iter)
    
    return fractal

def update(frame):
    global zoom_factor, ax, canvas
    zoom_factor *= 0.9  # Zoom in each frame
    xmin, xmax = -2.0 / zoom_factor, 2.0 / zoom_factor
    ymin, ymax = -1.5 / zoom_factor, 1.5 / zoom_factor
    
    fractal = generate_fractal(xmin, xmax, ymin, ymax, width.get(), height.get(), max_iter.get())
    ax.clear()
    ax.imshow(fractal, extent=[xmin, xmax, ymin, ymax], cmap='magma')
    ax.set_xticks([])
    ax.set_yticks([])
    canvas.draw()

def start_animation():
    global ani
    ani = animation.FuncAnimation(fig, update, frames=50, interval=100)
    canvas.draw()

def stop_animation():
    global ani
    if ani:
        ani.event_source.stop()

def update_params():
    global ax, canvas
    xmin, xmax = -2.0, 2.0
    ymin, ymax = -1.5, 1.5
    fractal = generate_fractal(xmin, xmax, ymin, ymax, width.get(), height.get(), max_iter.get())
    ax.clear()
    ax.imshow(fractal, extent=[xmin, xmax, ymin, ymax], cmap='magma')
    ax.set_xticks([])
    ax.set_yticks([])
    canvas.draw()

# Tkinter GUI setup
root = tk.Tk()
root.title("Mandelbrot Fractal Viewer")

frame = ttk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

global zoom_factor
zoom_factor = 1.0

controls = ttk.Frame(root)
controls.pack(side=tk.RIGHT, fill=tk.Y)

# Resolution controls
width = tk.IntVar(value=400)
height = tk.IntVar(value=300)
max_iter = tk.IntVar(value=100)

ttk.Label(controls, text="Width:").pack()
ttk.Entry(controls, textvariable=width).pack()

ttk.Label(controls, text="Height:").pack()
ttk.Entry(controls, textvariable=height).pack()

ttk.Label(controls, text="Max Iterations:").pack()
ttk.Entry(controls, textvariable=max_iter).pack()

# Buttons
ttk.Button(controls, text="Update", command=update_params).pack()
ttk.Button(controls, text="Start Animation", command=start_animation).pack()
ttk.Button(controls, text="Stop Animation", command=stop_animation).pack()

update_params()
root.mainloop()
