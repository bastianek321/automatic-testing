from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# https://www.zalando.pl/
# test 1
def zalando_cart_test(driver):
    try:
        driver.find_element_by_xpath('//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div[3]/a').click()
        print('Test passed (enter cart test)')
    except Exception:
        print('Test failed (enter cart test)')

# test 2
def zalando_login_inputs_test(driver):
    try:
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/z-grid/z-grid-item[2]/z-grid/z-grid-item[1]/button').click()
        login_field = driver.find_element_by_xpath('//*[@id="login.email"]')
        login_field.send_keys('testlogin')
        password_field = driver.find_element_by_xpath('//*[@id="login.password"]')
        password_field.send_keys('testpassword')
        login_input = login_field.get_attribute('value')
        password_input = password_field.get_attribute('value')
        print(f'Test passed (given inputs: {login_input} {password_input})')
    except Exception:
        print('Test failed (login test with input getter)')

# test3
def zalando_mobile_or_desktop_test(driver):
    try:
        driver.find_element_by_class_name('z-coast-ui-header_logo').click()
        driver.set_window_size(400, 600)
        menu = driver.find_element_by_xpath('//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[1]/a')
        if(menu):
            print('Test passed (this is a mobile version)')
        else:
            print('Test passed (this is a desktop version)')
    except Exception:
        print('Test failed (mobile or desktop)')

def zalando_tests_compiled(driver):
    driver.get('https://www.zalando.pl/')
    zalando_cart_test(driver)
    zalando_login_inputs_test(driver)
    zalando_mobile_or_desktop_test(driver)
    driver.close()

def run_zalando_tests():
    print('ZALANDO.PL TESTS\n')
    zalando_tests_compiled(webdriver.Chrome(executable_path='./drivers/chromedriver.exe'))
    firefox_options = Options()
    firefox_options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
    zalando_tests_compiled(webdriver.Firefox(executable_path='./drivers/geckodriver.exe', options=firefox_options))
    zalando_tests_compiled(webdriver.Edge(executable_path='./drivers/msedgedriver.exe'))
    print('Zalando tests finished \n\n')
