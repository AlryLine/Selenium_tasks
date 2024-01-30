from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome ()
driver.get ('https://www.easemytrip.com/')
assert "EaseMyTrip" in driver.title

form = driver.find_element (By.ID, "frmHome")
frm = driver.find_element (By.ID, "FromSector_show")
to = driver.find_element (By.ID, "Editbox13_show")

frm.click ()
srch_field1 = driver.find_element (By.ID, "a_FromSector_show")
srch_field1.send_keys ("Singapore")

to.click ()
srch_field2 = driver.find_element (By.ID, "a_Editbox13_show")
srch_field2.send_keys ("Dubai")

dep_date = driver.find_element (By.ID, "ddate")
dep_date.click()
calendar = driver.find_element (By.ID, "dvcalendar")
dep_day = driver.find_element (By.ID, "trd_5_15/09/2023")
dep_day.click ()

srch = driver.find_element (By.XPATH, "//div[7]/button")
srch.click ()

WebDriverWait (driver, 30).until (EC.visibility_of_element_located ((By.ID, "ResultDiv")))

tickets = driver.find_elements (By.CLASS_NAME, "lis")
assert "Flight Tickets" in driver.title
assert "Modify Search & Try Again" not in driver.page_source

count = 0
for lis in tickets:
    count += 1
print (f"Flights count: {count}")

driver.close ()
