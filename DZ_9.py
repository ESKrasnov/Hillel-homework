"""
prerequisites  = https://www.aqa.science/
0. start docker container
1. open URL
2. click the login button
4.
5. stop docker container
"""
import os
import time


from selenium import webdriver
from selenium.webdriver.common.by import By


def create_docker_container():
    os.system("docker run -d -p 4141:4444 -p 5900:5900 --shm-size=2g "
              "--name web-test_chrome selenium/standalone-chrome-debug")

    time.sleep(2)

def remove_docker_container():
    os.system("docker stop web-test_chrome")
    os.system("docker rm /web-test_chrome")


create_docker_container()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors=yes')

driver = webdriver.Remote(command_executor='http://localhost:4141/wd/hub',
                          options=options)


url = ["https://www.aqa.science/"]
driver.get(url[0])


                                  ###   Login form



log_button = '/html/body/div/div[1]/div/ul/li/a'
login_button = driver.find_element(By.XPATH, log_button)
login_button.click()

username = 'admin'
password = 'admin123'


username_field = '//*[@id="id_username"]'
password_field = '//*[@id="id_password"]'

element_username = driver.find_element(By.XPATH, username_field)
element_username.send_keys(username)

element_password = driver.find_element(By.XPATH, password_field)
element_password.send_keys(password)

l_button = '//*[@id="submit-id-submit"]'
sumbit_button = driver.find_element(By.XPATH, l_button)
sumbit_button.click()


                               ###  Create user


url = ["https://www.aqa.science/admin/"]

driver.get(url[0])

create_user_button = '//*[@id="content-main"]/div/table/tbody/tr[2]/td[1]/a'
create_user = driver.find_element(By.XPATH, create_user_button)
create_user.click()

username = 'Evgenii.Krasnov'
username_field = '//*[@id="id_username"]'
username_field_create = driver.find_element(By.XPATH, username_field)
username_field_create.send_keys(username)

password = 'esk123456789'
first_password_field = '//*[@id="id_password1"]'
second_password_field = '//*[@id="id_password2"]'

f_password_field = driver.find_element(By.XPATH, first_password_field)
f_password_field.send_keys(password)

s_password_field = driver.find_element(By.XPATH, second_password_field)
s_password_field.send_keys(password)

s_button = '//*[@id="user_form"]/div/div/input[1]'
save_button = driver.find_element(By.XPATH, s_button)
save_button.click()

                       ###    Read user

expected_element_path = '//*[@id="content"]/h2'

expected_element = driver.find_element(By.XPATH, expected_element_path)

assert expected_element.text == 'Evgenii.Krasnov'


                      ###    Update user


first_name = 'Evgenii'
last_name = 'Krasnov'

first_name_field = '//*[@id="id_first_name"]'
last_name_field = '//*[@id="id_last_name"]'

new_first_name = driver.find_element(By.XPATH, first_name_field)
new_first_name.send_keys(first_name)

new_last_name = driver.find_element(By.XPATH, last_name_field)
new_last_name.send_keys(last_name)

s_button = '//*[@id="user_form"]/div/div/input[1]'

save_button = driver.find_element(By.XPATH, s_button)
save_button.click()




                       ### Delete user

user_name = '//*[@id="result_list"]/tbody/tr[2]/th/a'
open_user = driver.find_element(By.XPATH, user_name)
open_user.click()

delete_button = '//*[@id="user_form"]/div/div/p/a'

delete_user = driver.find_element(By.XPATH, delete_button)
delete_user.click()

button ='//*[@id="content"]/form/div/input[2]'
confirmation = driver.find_element(By.XPATH, button)
confirmation.click()

assert user_name != 'Evgenii.Krasnov'


remove_docker_container()