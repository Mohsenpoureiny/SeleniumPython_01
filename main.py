from selenium import webdriver
from selenium.webdriver.common.keys import Keys
phrase = input("Enter Phrase: ")
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(phrase+Keys.ENTER)
h3_elements = driver.find_elements_by_tag_name("h3")
[print(i.text) for i in h3_elements]
driver.close()