#-*- coding: utf-8 -*-

from data_processing import read_csv, filter_data
from plotting import draw_plot

def main():
    # 讀取 CSV 檔案並處理資料
    file_path = 'data/earthquake_data.csv'
    df = read_csv(file_path)
    if df is not None:
        keyword = '花蓮縣'
        df_filtered = filter_data(df, keyword)

        # 提取 X、Y 和 Value 欄位的資料
        x = df_filtered['地震時間']
        y = df_filtered['規模']
        values = df_filtered['規模']
        point_sizes = [(i - 3) / 6 * 800 for i in values]

        # 繪製散點圖
        draw_plot(x, y, values, point_sizes)

if __name__ == '__main__':
    main()
