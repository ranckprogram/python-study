def login(driver,urlPath):
  driver.get(urlPath)
  driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[1]/div/div/input').send_keys("admin")
  driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[2]/div/div/input').send_keys("admin")
  driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/button').click()