# random colors
# maybe a few set center points
# random min and max in set ranges based on centers


import numpy as np
import matplotlib.pyplot as plt
import random


def mandelbrot(n_rows, n_columns, iterations, minimum=-2, maximum=1):
    x_cor = np.linspace(minimum,maximum,n_rows)
    y_cor = np.linspace(minimum,maximum,n_columns)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))
    for i in range(x_len):
        for j in range(y_len):
            c = complex(x_cor[i],y_cor[j])
            z = complex(0, 0)
            count = 0
            for k in range(iterations):
                z = (z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count

    plt.imshow(output.T)
    plt.axis("off")
    plt.show()

minimum = random.uniform(-2, 1)
maximum = random.uniform(-2, 1)
print('Min: ', minimum)
print('Max: ', maximum)

mandelbrot(1000,1000,100, minimum, maximum)

#mandelbrot(1000,1000,100)
