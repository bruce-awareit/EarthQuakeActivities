#-*- coding: utf-8 -*-

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import chardet

# Set the desired download folder (replace with your path)
download_folder = os.path.join(os.getcwd(), "data")

# 檢查資料夾是否存在，若不存在則建立資料夾
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Set the desired filename
new_filename = "earthquake_data.csv"

def set_chrome_options():
    options = Options()
    options.add_argument("--headless")  # 隱藏瀏覽器視窗
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option('prefs', {
    "download.default_directory": download_folder,  # 自動下載路徑
    "download.prompt_for_download": False,       # 不顯示下載視窗
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True                 # 允許下載
})
    return options

def handle_import_error(package_name):
    print(f"無法匯入套件: {package_name}")
    print("請確保所需的套件已安裝。您可以使用以下指令安裝缺失的套件：")
    print(f"pip install {package_name}")

def download_data():
    try:
        driver = webdriver.Chrome(options=set_chrome_options())

        # Open the target URL
        driver.get("https://scweb.cwa.gov.tw/zh-tw/earthquake/data")

        # Wait for the download button to be clickable
        # wait = WebDriverWait(driver, 10)
        download_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='CSV']"))
        )
        # Click the download button
        try:
            download_button.click()

            # 檢查下載是否完成
            downloaded_files = os.listdir(download_folder)
            if any(file.endswith('.csv') for file in downloaded_files):
                print("CSV 檔案下載成功")
            else:
                print("CSV 檔案下載失敗")

        except Exception as e:
            raise Exception(f"無法點擊下載按鈕: {e}")

        # Wait for the download to complete
        time.sleep(5)  # Adjust this wait time based on your internet speed and file size

        # Get the latest downloaded file
        downloaded_files = [os.path.join(download_folder, file) for file in os.listdir(download_folder)]
        latest_file = max(downloaded_files, key=os.path.getctime)

        # Rename the latest downloaded file
        renamed_file = os.path.join(download_folder, new_filename)
        os.rename(latest_file, renamed_file)

        # Convert file encoding to UTF-8 and save
        try:
            with open(renamed_file, "rb") as f:
                rawdata = f.read()
                encoding = chardet.detect(rawdata)['encoding']
                data = rawdata.decode(encoding, errors='ignore')

            with open(renamed_file, "w", encoding="utf-8") as f:
                f.write(data)
        except Exception as e:
            print(f"轉檔錯誤: {e}")

        print(f"CSV 檔案下載完成，並重新命名為 {new_filename}，並轉碼成 UTF-8 存檔")

    except ImportError as e:
        handle_import_error(e.name)

    except Exception as e:
        print(f"錯誤發生: {e}")

    finally:
        if driver is not None:
            # Close the browser
            driver.quit()

if __name__ == "__main__":
    download_data()
