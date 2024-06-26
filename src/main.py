# -*- coding: utf-8 -*-

try:
    from data_processing import read_csv, filter_data
    from plotting import draw_plot
    import sys
    import re
except ImportError as e:
    print(f"Import error: {e}\n")
    print("Please make sure the required modules are installed and their paths are correctly set.\n")
    print("You can use 'pip install pandas matplotlib' to install the required modules.\n")
    exit()

# Regular Expression
pattern = r'^[A-Za-z\u4e00-\u9fa5][A-Za-z_/\.\u4e00-\u9fa5\d]{7,}$'

def check_string(s):
    return re.match(pattern, s) is not None

def main():
    # 讀取 CSV 檔案並處理資料
    file_path = 'data/earthquake_data.csv'

    if len(sys.argv) == 2 and check_string(sys.argv[1]):
        file_path = sys.argv[1]

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

