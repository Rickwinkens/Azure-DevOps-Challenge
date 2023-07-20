from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/petclinic")

time.sleep(2)

driver.get("http://localhost:8080/petclinic/owners/find")

time.sleep (2)

search_bar = driver.find_element(By.NAME, "lastName")
search_bar.clear()
search_bar.send_keys("Franklin")
time.sleep(1)
search_bar.submit()

time.sleep(2)

driver.get("http://localhost:8080/petclinic/vets")

time.sleep(2)

driver.get("http://localhost:8080/petclinic/oups")

time.sleep(3)

driver.quit()

