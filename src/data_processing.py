
#-*- coding: utf-8 -*-

import pandas as pd

def read_csv(file_path):
    try:
        # 讀取 CSV 檔案，跳過第一列，並解析日期時間格式
        df = pd.read_csv(file_path, skiprows=1, parse_dates=['地震時間'])
        df['地震時間'] = pd.to_datetime(df['地震時間'], format='%Y-%m-%d %H:%M:%S')
        return df
    except FileNotFoundError:
        print("找不到指定的 CSV 檔案。")
        return None
    except pd.errors.ParserError:
        print("日期時間格式解析錯誤。")
        return None
    except Exception as e:
        print(f"發生未知錯誤：{e}")
        return None

def filter_data(df, keyword):
    # 選擇欄位包含特定字串的列
    condition = df['位置'].str.contains(keyword)

    # 留下符合條件的列
    df_filtered = df[condition].reset_index(drop=True)

    return df_filtered
