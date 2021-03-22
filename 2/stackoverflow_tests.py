from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# https://stackoverflow.com/
# test 1
def stackoverflow_about_test(driver):
    try:
        driver.find_element_by_xpath('/html/body/header/div/ol[1]/li[1]/a').click()
        print('Test passed (enter cart test)')
    except Exception:
        print('Test failed (enter cart test)')

# test 2
def stackoverflow_login_inputs_test(driver):
    try:
        driver.get('https://stackoverflow.com')
        driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()
        login_field = driver.find_element_by_xpath('//*[@id="email"]')
        login_field.send_keys('testlogin')
        password_field = driver.find_element_by_xpath('//*[@id="password"]')
        password_field.send_keys('testpassword')
        login_input = login_field.get_attribute('value')
        password_input = password_field.get_attribute('value')
        print(f'Test passed (given inputs: {login_input} {password_input})')
    except Exception:
        print('Test failed (login test with input getter)')

# test3
def stackoverflow_mobile_or_desktop_test(driver):
    try:
        driver.get('https://stackoverflow.com')
        driver.set_window_size(400, 600)
        for_teams_button = driver.find_element_by_xpath('/html/body/header/div/ol[1]/li[3]/a')
        if(for_teams_button):
            print('Test passed (this is a mobile version)')
        else:
            print('Test passed (this is a desktop version)')
    except Exception:
        print('Test failed (mobile or desktop)')

def stackoverflow_tests_compiled(driver):
    driver.get('https://stackoverflow.com/')
    stackoverflow_about_test(driver)
    stackoverflow_login_inputs_test(driver)
    stackoverflow_mobile_or_desktop_test(driver)
    driver.close()

def run_stackoverflow_tests():
    print('STACKOVERFLOW TESTS\n')
    stackoverflow_tests_compiled(webdriver.Chrome(executable_path='./drivers/chromedriver.exe'))
    firefox_options = Options()
    firefox_options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
    stackoverflow_tests_compiled(webdriver.Firefox(executable_path='./drivers/geckodriver.exe', options=firefox_options))
    stackoverflow_tests_compiled(webdriver.Edge(executable_path='./drivers/msedgedriver.exe'))
    print('Stackoverflow tests finished\n\n')
