#-*- coding: utf-8 -*-

try:
    import matplotlib.pyplot as plt
except ImportError as e:
    print(f"Import error: {e}\n")
    print("Please make sure the required modules are installed and their paths are correctly set.\n")
    print("You can use 'pip install pandas matplotlib' to install the required modules.\n")
    exit()

def draw_plot(x, y, values, point_sizes):
    try:
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
    except Exception as e:
        print(f"Error while drawing plot: {e}\n")