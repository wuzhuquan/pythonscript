import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('http://192.168.1.100:9880/spa-manager/')
driver.maximize_window()
#输入用户名，密码，记住登录
driver.find_element_by_id('user-name').send_keys('wzq2')
driver.find_element_by_id('user-pw').send_keys('123456')

#点击登录
driver.find_element_by_xpath('//*[@id="login-dialog"]/form/input[2]').click()
time.sleep(1)
print("登录成功")
#打开营销活动
driver.find_element_by_xpath('//*[@id="menu"]/div[2]/div').click()
time.sleep(1)
#打开优惠券
driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[2]/a').click()
#handles = driver.window_handles
# driver.switch_to.window(handles[1])
time.sleep(1)
for i in range (1,1010):
	#选择现金券
	driver.find_element_by_xpath('//*[@id="ordinaryCouponSellPage"]/div[1]/div[2]/div[1]/a').click()
	print('ID测试第'+str(i)+'轮')
	time.sleep(1)
	driver.find_element_by_id('couponName').send_keys('ID测试'+str(i))
	driver.find_element_by_id('actValueOfCashOriAmount').send_keys('100')
	driver.find_element_by_id('actValueOfCashAmount').send_keys('10')
	print("输入...")
	#time.sleep(1)
	#点击保存
	driver.find_element_by_xpath('//*[@id="editOrdinaryCouponPage"]/div[1]/div[1]/div/a[2]').click()
	time.sleep(1)
	#获取ID
	COUPON_ID = driver.find_element_by_xpath('//*[@id="dataListTable"]/table/tbody/tr[1]/td[2]').text
	print("成功创建现金券,ID :"+COUPON_ID)
	time.sleep(1)
	#点击删除
	driver.find_element_by_xpath('//*[@id="dataListTable"]/table/tbody/tr[1]/td[14]/a[2]').click()
	time.sleep(1)
	#确定删除
	driver.find_element_by_xpath('//*[@id="confirmModal"]/div/div[2]/a[1]').click()
	time.sleep(1)
	print("---券已删除---")
	

time.sleep(2)
print("测试结束")
driver.close()
