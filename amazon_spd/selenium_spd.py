from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def test():
    driver_path = Service(r"chromedriver.exe")
    driver = webdriver.Chrome(service=driver_path)
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.de/gp/new-releases/automotive/ref=zg_bsnr_nav_0")
    elements = driver.find_elements(By.XPATH,
                                    """//*[@class='_p13n-zg-nav-tree-all_style_zg-browse-root__-jwNv'] """)
    return elements