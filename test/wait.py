# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.get("https://www.baidu.com")
WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id("kw"))
driver.find_element(By.ID, "kw").click()