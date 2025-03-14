import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D  - not needed since version 3.0
import matplotlib.animation as animation

X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)

Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(8,6))
# fig.add_subplot(nrows=1, ncols=1, index=1)
ax = fig.add_subplot(111, projection="3d")

surf = ax.plot_surface(X, Y, Z, cmap="inferno")
fig.colorbar(surf)
plt.title("3D Surface Plot")
# Function to update rotation angle
def update(angle):
    ax.view_init(elev=30, azim=angle)

# Create animation rotating from 0° to 360°
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

# ax.view_init(elev=30, azim=60) # Elevation/Azimuth -> change the POV of the camera
plt.show()

