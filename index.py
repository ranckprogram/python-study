from selenium import webdriver
import login
import time


driver = webdriver.Chrome(executable_path='./chromedriver.exe')


loginUrl = 'https://localhost:8082/#/login'

login.login(driver, loginUrl)


print(driver)

time.sleep(1)


url = 'https://localhost:8082/#/address/ipam/assets?current=1'
driver.get(url)#打开浏览器预设网址
print('Hello, world')

time.sleep(1)
openCreateBtn = driver.find_element_by_id("openCreatebtn")
openCreateBtn.click()

time.sleep(1)

driver.get(url)#打开浏览器预设网址


def executeOperate(driver,times):
  count = 0
  while (count < times):
    count = count + 1
    print(count)
    
    

executeOperate(driver, 100)