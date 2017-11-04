import selenium
import time,os
import configparser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import log_config

logging = log_config.getlogger("")
# 读取config.conf 中的配置
conf = configparser.ConfigParser()
conf.read(os.path.join(os.path.abspath('.'),'config.conf'))

driver = webdriver.Chrome()
logging.info('------正在打开PC后台管理系统------')
driver.get("http://sdcm100:9880/spa-manager/")
driver.maximize_window()
# 输入用户名，密码,点击登录
driver.find_element_by_id('user-name').send_keys(conf.get('manager_account','name'))
driver.find_element_by_id('user-pw').send_keys(conf.get('manager_account','password'))
driver.find_element_by_xpath('//*[@id="login-dialog"]/form/input[2]').click()
time.sleep(1)
logging.info("------PC后台管理系统登录成功------")
try:
    while True:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='homePage']/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[10]/div/p[1]/i")))
        time.sleep(1)
        tr = driver.find_element_by_xpath("//*[@id='homePage']/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[10]/div/p[1]/i")
        logging.info("找到了订单")
        tr.click()
        time.sleep(1)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='confirmFastPayModal']/div/div[2]/a[1]")))
        driver.find_element_by_xpath("//*[@id='confirmFastPayModal']/div/div[2]/a[1]").click()
        logging.info("订单已确认")
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
except TimeoutException:
    logging.error("找不到元素，已经没有新的未处理订单")
