from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import credentials

username = credentials.username
password = credentials.password
course_link = credentials.course_link

# initialize the Chrome driver
driver = webdriver.Chrome("./chromedriver")

driver.get("https://sis.iutoic-dhaka.edu/login")
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div[2]/form/div[1]/input").send_keys(username)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div[2]/form/div[2]/input").send_keys(password)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div[2]/form/div[4]/button").click()


driver.get(course_link)
driver.implicitly_wait(90)

xpaths = []
element_numb = [4, 1, 5, 4, 4, 3, 3, 3] # how many options per section
for idx, elements in enumerate(element_numb):
    for i in range(elements):
        x_string = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[{section}]/div/div[{ele}]/div/div[2]/div/label[5]/input".format(section=str(idx+1), ele=str(i+1))
        xpaths.append(x_string)

for xpath in xpaths:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))))

best_feature_path = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[9]/div/div[1]/div/div[2]/div/textarea"
improve_path = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[9]/div/div[2]/div/div[2]/div/textarea"
co_path = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[9]/div/div[3]/div/div[2]/div/textarea"

driver.find_element_by_xpath(best_feature_path).send_keys("good")
driver.find_element_by_xpath(improve_path).send_keys("good")
driver.find_element_by_xpath(co_path).send_keys("good")

import time
time.sleep(1)

submit_path = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[10]/button"
driver.find_element_by_xpath(submit_path).click()
