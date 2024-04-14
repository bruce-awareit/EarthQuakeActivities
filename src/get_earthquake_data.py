# -*- coding: utf-8 -*-

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os



# Set the desired download folder (replace with your path)
download_folder = "../data/"

# Set the desired filename
new_filename = "earthquake_data.csv"

# 設定 Chrome 下載選項
options = Options()
options.add_argument("--headless")  # 隱藏瀏覽器視窗
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("prefs", {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)

# Open the target URL
driver.get("https://scweb.cwa.gov.tw/zh-tw/earthquake/data")

# Wait for the download button to be clickable
wait = WebDriverWait(driver, 10)
download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='BaSet csv' and @href='javascript:' and @title='匯出地震資料 (地震活動彙整.csv)' and @onclick='exportCSV()']")))


# Click the download button
download_button.click()

# Wait for the download to complete
time.sleep(5)  # Adjust this wait time based on your internet speed and file size

# 取得下載的檔案路徑和名稱
downloaded_file = os.path.join(download_folder, os.listdir(download_folder)[0])

# 指定新的檔案名稱
new_filename = "earthquake_data.csv"

# 重新命名下載的檔案
os.rename(downloaded_file, os.path.join(download_folder, new_filename))

# Close the browser
driver.quit()


print(f"CSV 檔案下載完成，儲存於 {new_filename}")
