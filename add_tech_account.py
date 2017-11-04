# -*- coding:utf-8 -*-
import configparser
import os
from selenium import webdriver
from xpinyin import Pinyin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import log_config
import time


class AddTechAccount(object):
    def __init__(self):
        logger = log_config.getlogger("")
        self.driver = webdriver.Chrome()

    def add_tech_account(self):
        driver = self.driver
        logger = log_config.getlogger("")
        # 读取config.conf 中的配置
        conf = configparser.ConfigParser()
        conf.read(os.path.join(os.path.abspath('.'), 'config.conf'))
        logger.info('------正在打开PC后台管理系统------')
        driver.get("http://sdcm100:9880/spa-manager/")
        driver.maximize_window()
        # 输入用户名，密码,点击登录
        driver.find_element_by_id('user-name').send_keys(conf.get('manager_account', 'name'))
        driver.find_element_by_id('user-pw').send_keys(conf.get('manager_account', 'password'))
        driver.find_element_by_xpath('//*[@id="login-dialog"]/form/input[2]').click()
        time.sleep(1)
        logger.info("------PC后台管理系统登录成功------")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@text='邮件群组']"))).click()
        time.sleep(2)
        tech_name  = ""

if __name__ == "__main__":
    t = AddTechAccount()
    t.add_tech_account()