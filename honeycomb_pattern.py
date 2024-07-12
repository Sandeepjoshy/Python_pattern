import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def plot_hexagonal_grid(rows, cols):
    # Generate hexagon coordinates
    hex_height = np.sqrt(3)
    hex_width = 2
    x_spacing = 1.5
    y_spacing = hex_height

    fig, ax = plt.subplots()
    for col in range(cols):
        num_hexagons = rows if col % 2 == 0 else rows - 1  # Alternate between rows and rows-1
        for row in range(num_hexagons):
            x = col * x_spacing
            y = row * y_spacing
            if col % 2 == 1:
                y += hex_height / 2

            hexagon = patches.RegularPolygon((x, y), numVertices=6, radius=1, orientation=np.radians(30), edgecolor='black', facecolor='none')
            ax.add_patch(hexagon)

    ax.set_aspect('equal')
    plt.xlim(-1, cols * x_spacing)
    plt.ylim(-1, rows * y_spacing)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Get user input for number of rows and columns
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    plot_hexagonal_grid(rows, cols)

