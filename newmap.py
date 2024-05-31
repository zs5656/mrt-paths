import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Function to handle click events
def on_map_click(event):
    # Get the coordinates of the click
    x, y = event.x, event.y
    print(f"Clicked at coordinates: ({x}, {y})")

# Create the main application window
root = tk.Tk()
root.title("Clickable Map Example")

# Load the map image using PIL
image_path = "map.png"
pil_image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(pil_image)

# Create a canvas to display the map
canvas = tk.Canvas(root, width=pil_image.width, height=pil_image.height)
canvas.pack()

# Add the image to the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

# Bind the click event to the on_map_click function
canvas.bind("<Button-1>", on_map_click)

# Start the Tkinter event loop
root.mainloop()