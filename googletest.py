
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.wait import WebDriverWait #显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time #强制等待
import xlrd #读取excel


# 方法A：如果chromedriver.exe就在项目根目录，不需要配置环境变量，也不需要指定路径（新版本Selenium推荐写法）
#service = Service()
# Selenium 4 及以上推荐使用 Service 对象
#driver = webdriver.Chrome(service=service)

# 方法B：如果你把chromedriver.exe放在了其他位置，需要指定路径
service = Service(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Bin\chromedriver.exe')
# 例如： service = Service(r'你的chromedriver.exe的绝对路径')
browser = webdriver.Chrome(service=service)
# 浏览器最大化
browser.maximize_window()

#输入用户名密码
exlpath = r"C:\Users\Administrator\Desktop\testcase.xls"
xlBook = xlrd.open_workbook(exlpath)
xltable = xlBook.sheets()[0]
exlrow =xltable.nrows
exlcol =xltable.ncols

for i in range(1,exlrow):
    # 打开一个网页
    browser.get("https://app.zhixiangchengshi.com/")
    # 等待登录字样
    wait = WebDriverWait(browser, timeout=10, poll_frequency=1)
    search_login = wait.until(EC.visibility_of_element_located((By.ID, "showLoginDialogBtn")))
    # 点击登录
    login_bth = browser.find_element(by=By.ID, value="showLoginDialogBtn")
    login_bth.click()
    time.sleep(2)
    Username =xltable.cell_value(i,1)
    Password =xltable.cell_value(i,2)
    print(f"用户名：{Username}，密码：{Password}")
    suername_box = browser.find_element(by=By.ID,value="usercode")
    suername_box.send_keys(f"{Username}")
    pwd_box = browser.find_element(by=By.ID,value="password")
    pwd_box.send_keys(f"{Password}")
    time.sleep(2)
    #点击登录
    login2_bth =browser.find_element(by=By.ID,value ="login")
    login2_bth.click()
    Search_logo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "layui-layer-content")))
    print(Search_logo)
    time.sleep(2)


browser.close()
# 关闭浏览器
browser.quit()
