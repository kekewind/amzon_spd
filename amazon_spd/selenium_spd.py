from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

"""
    Author:Ozzie
    Creat_time:2022-11-13
"""

# def test():

"""
初始化selenium，设置超时的时常响应时间为10s
由指定的浏览器驱动请求网址，根据Xpath匹配需要
的元素
这里抓取了amazon站点中的类目和类目下a标签内的
href，按下F12查看网络元素，此处可自行更改匹配
"""

first_menu = []
two_menu = []
driver_path = Service(r"chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)
driver.implicitly_wait(10)
driver.get("https://www.amazon.de/gp/new-releases/automotive/ref=zg_bsnr_nav_0")
init_elements = driver.find_elements(By.XPATH,
                                     """//*[@class='_p13n-zg-nav-tree-all_style_zg-browse-root__-jwNv'] """)

for i in init_elements:
    first_menu.append(i.text)

# 获取url
href_elements = driver.find_elements(By.XPATH,
                                     """//*[@class="_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8"]/*""")
for i in href_elements:
    two_menu.append(i.get_attribute('href'))

# 获取三级类目
three_menu = []
for i in two_menu:
    if i is None:
        pass
    else:
        driver.get(i)
        element = driver.find_elements(By.XPATH,
                                       """//*[@class="_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8"]/*""")
        for x in element:
            three_menu.append(x.get_attribute('href'))

print(three_menu)
# # 获取四级类目
# four_menu = []
# for i in three_menu:
#     if i is None:
#         pass
#     else:
#         driver.get(i)
#         element = driver.find_elements(By.XPATH,
#                                        """//*[@class="_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8"]/*""")
#         for x in element:
#             four_menu = x.get_attribute('href')

