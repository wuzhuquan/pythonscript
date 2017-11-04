import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
print('------正在打开PC后台管理系统------')
driver.get(URL)
driver.maximize_window()
#输入用户名，密码,点击登录
driver.find_element_by_id('user-name').send_keys('wzq')
driver.find_element_by_id('user-pw').send_keys('123456')
driver.find_element_by_xpath('//*[@id="login-dialog"]/form/input[2]').click()
time.sleep(1)
print("------PC后台管理系统登录成功------")

#用JS打开
js='window.open("http://192.168.1.142/jira/login.jsp");'
driver.execute_script(js)
#打开jira  
time.sleep(1)
print('------正在打开Confluence------')
#转移到新窗口
handles = driver.window_handles
driver.switch_to.window(handles[1])
time.sleep(1)
#输入用户名，密码，登录
driver.find_element_by_id('login-form-username').send_keys('wuzhuquan')
driver.find_element_by_id('login-form-password').send_keys('wuzhuquan')
driver.find_element_by_xpath('//*[@id="home-page"]/div[5]/div[2][@class="pay_act_item"]').click()
time.sleep(1)
print("JIRA登录成功")
#打开问题
driver.find_element_by_id('find_link').click()
time.sleep(1)
#打开分配给我的未解决的问题
driver.find_element_by_id('filter_lnk_my_lnk').click()
time.sleep(1)
print('------成功打开JIRA------')

#用JS打开
js='window.open("http://192.168.1.142:8090/login.action");'
driver.execute_script(js)
#打开Confluence
time.sleep(1)
print('------正在打开Confluence------')
#转移到新窗口
handles = driver.window_handles
driver.switch_to_window(handles[2])
time.sleep(1)
#输入用户名，密码，登录
driver.find_element_by_id('os_username').send_keys('wuzhuquan')
driver.find_element_by_id('os_password').send_keys('wuzhuquan')
driver.find_element_by_id('loginButton').click()
print('------Confluence打开成功------')
time.sleep(1)

time.sleep(2)
print("已经全部打开")

