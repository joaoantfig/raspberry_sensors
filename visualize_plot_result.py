
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#plt.style.use('fivethirtyeight')
plt.style.use('dark_background')
    
#def animate(i):
    #x_vals.append(next(index))
    #y_vals.append(random.randint(0, 5))
    
data = pd.read_csv('data.csv')
x = data['x_value']
y1 = data['voltage_1']
y2 = data['voltage_2']
y3 = data['voltage_3']

plt.cla()

plt.plot(x, y1, label='V_POT')
plt.plot(x, y2, label='V_BUTT')
plt.plot(x, y3, label='V_REF')

plt.legend(loc='upper left')
plt.tight_layout()


#ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()

