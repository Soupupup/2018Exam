from numpy import *
import matplotlib.pyplot as plt
%matplotlib inline
fig_height = 200
fig_width = 300
x_compress = 1.5
y_compress = 1.0
zoom = 0.5
scale = 1


def pixel_coord(compression, pixel_value, fig_length, zoom, scale):
    pix_coord = compression * \
        (pixel_value - fig_length / 2) / (zoom * scale * fig_length)
    return pix_coord
A = zeros([fig_height, fig_width])
for pixel_x in range(fig_width):
    for pixel_y in range(fig_height):
        zx = pixel_coord(x_compress, pixel_x, fig_width, zoom, scale)
        zy = pixel_coord(y_compress, pixel_y, fig_height, zoom, scale)
        iteration = 255
        t = True
        while t == True:
            if zx * zx + zy * zy >= 4:
                t = False
            if iteration <= 1:
                t = False
            zx_temp = zx * zx - zy * zy - 0.7
            zy = 2.0 * zx * zy + 0.27015
            zx = zx_temp
            iteration = iteration - 1
        A[pixel_y][pixel_x] = iteration
plt.imshow(A)
plt.show()
