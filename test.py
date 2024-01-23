# 控制Courant数
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

nx = 100  # 空间网格数
dx = 2 / (nx - 1)  # 空间网格尺寸
nt = 20  # 时间步数
# dt = 0.025  # 时间步长
sigma = 0.5
dt = sigma * dx
u = np.ones(nx)
u[int(0.6 / dx):int(1 / dx + 1)] = 2
u_init = u.copy()

fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(0, 2.5)
line, = ax.plot(np.linspace(0, 2, nx), u_init, 'g--', lw=3, label='init')
line2, = ax.plot(np.linspace(0, 2, nx), u, 'r', lw=3, label='current')
ax.legend()

def update(frame):
    global u
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i - 1])
    line.set_ydata(u_init)  # 更新初始波形
    line2.set_ydata(u)
    return line, line2

ani = FuncAnimation(fig, update, frames=nt, blit=True, interval=200)
plt.show()