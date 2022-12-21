from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import re

#
driver_path = Service(r"chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)
driver.implicitly_wait(10)
driver.get("https://www.amazon.de/gp/new-releases/automotive/ref=zg_bsnr_nav_0")
init_elements = driver.find_elements(By.XPATH,
                                     """//*[@class='_p13n-zg-nav-tree-all_style_zg-browse-root__-jwNv'] """)
first_menu = ''
two_menu = {}
for i in init_elements:
    first_menu = i.text

print(first_menu)

# 获取url
href_elements = driver.find_elements(By.XPATH,
                                     """//*[@class='_p13n-zg-nav-tree-all_style_zg-browse-root__-jwNv']/[@href]""")
for i in href_elements:
    print(i.text)

input("-" * 6 + "点击回车后结束" + "-" * 6)
