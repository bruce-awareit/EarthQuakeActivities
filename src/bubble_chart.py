# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import math

def read_csv():
    # 讀取 CSV 檔案，跳過第一列
    df = pd.read_csv('data/earthquake_data.csv', skiprows=1, parse_dates=['地震時間'], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S'))

    # print(df.head())

    # 選擇欄位包含特定字串的列
    condition = df['位置'].str.contains('花蓮縣')

    # 留下符合條件的列
    df = df[condition].reset_index(drop=True)

    # 提取 X、Y 和 Value 欄位的資料
    x = df['地震時間']
    y = df['規模']
    values = df['規模']

    point_sizes=[(i-3)/6*800 for i in values]

    return x, y, values, point_sizes

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

def main():
    x, y, values, point_sizes = read_csv()

    draw_plot(x, y, values, point_sizes)

if __name__ == '__main__':
    main()