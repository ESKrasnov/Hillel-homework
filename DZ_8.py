"""
prerequisites  = https://www.google.com.ua/imghp?hl=ru&ogbl
0. start docker container
1. open URL
2. fill "Flowers" in search field
3. click the search button
4. verify that element == Flower - Wikipedia
5. stop docker container
"""
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def create_docker_container():
    os.system("docker run -d -p 4444:4444 -p 5900:5900 --shm-size=2g "
              "--name web-test_chrome selenium/standalone-chrome-debug")

    time.sleep(2)

def remove_docker_container():
    os.system("docker stop web-test_chrome")
    os.system("docker rm /web-test_chrome")


create_docker_container()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors=yes')

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          options=options)



uri_variable = "Flowers"

url = ["https://www.google.com.ua/imghp?hl=ru&ogbl"]

driver.get(url[0])

search_field = '//*[@id="sbtc"]/div/div[2]/input'
element = driver.find_element(By.XPATH, search_field)

element.send_keys(uri_variable)

button = '//*[@id="sbtc"]/button'

element_button = driver.find_element(By.XPATH, button)

element_button.click()

expected_element_path = '//*[@id="islrg"]/div[1]/div[4]/a[2]/span'

expected_element = driver.find_element(By.XPATH, expected_element_path)

if expected_element.text == 'Flower - Wikipedia':
    print("successful")
else:
    print("Failed")


remove_docker_container()