CHATGPT CONVERSATION

*******

create a python fractal animation
ChatGPT said:
ChatGPT
Here's a Python script to generate an animated fractal using Matplotlib and NumPy. It creates a Mandelbrot set animation by zooming into the fractal dynamically.

Fractal Animation

Answer in chat instead
This script generates an animated zoom-in effect on the Mandelbrot fractal. It progressively zooms into the fractal while updating the plot dynamically. Let me know if you want modifications! 🚀🎨





---------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
    global zoom_factor
    zoom_factor *= 0.9  # Zoom in each frame
    xmin, xmax = -2.0 / zoom_factor, 2.0 / zoom_factor
    ymin, ymax = -1.5 / zoom_factor, 1.5 / zoom_factor
    
    fractal = generate_fractal(xmin, xmax, ymin, ymax, 400, 300, 100)
    ax.clear()
    ax.imshow(fractal, extent=[xmin, xmax, ymin, ymax], cmap='magma')
    ax.set_xticks([])
    ax.set_yticks([])

global zoom_factor
zoom_factor = 1.0
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=50, interval=100)
plt.show()

