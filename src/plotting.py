#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def draw_plot(x, y, values, point_sizes):
    # 設置背景為黑色的風格
    plt.style.use('dark_background')

    # 繪製散點圖
    plt.rcParams['font.sans-serif'] = ['TW-Kai'] 
    plt.scatter(x, y, s=point_sizes, c=values, cmap='tab20c', alpha=0.75)
    plt.colorbar(label='Value')
    plt.xlabel('地震時間')
    plt.ylabel('規模')
    plt.title('地震活動')

    plt.minorticks_on()
    plt.tick_params(which='minor', direction='in')
    plt.grid(False)

    plt.show()
