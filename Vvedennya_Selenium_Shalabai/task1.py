from selenium import webdriver 

driver = webdriver.Chrome()  
driver.get ('https://www.selenium.dev/')
assert "Selenium" in driver.title

print ()
print (driver.title) 
driver.quit()