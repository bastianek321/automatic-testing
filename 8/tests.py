from selenium import webdriver
from selenium.common.exceptions import TimeoutException

def zalando_test():
    try:
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver.set_window_size(1600, 1000)
        driver.get('https://www.zalando.pl/')
        driver.find_element_by_xpath('//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div[3]/a').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/z-grid/z-grid-item[2]/z-grid/z-grid-item[1]/button').click()
        login_field = driver.find_element_by_xpath('//*[@id="login.email"]')
        login_field.send_keys('testlogin')
        password_field = driver.find_element_by_xpath('//*[@id="login.password"]')
        password_field.send_keys('testpassword')
        login_input = login_field.get_attribute('value')
        password_input = password_field.get_attribute('value')
    except Exception:
        print('Test failed')

def stackoverflow_test():
    try:
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver.set_window_size(1600, 1000)
        driver.get('https://stackoverflow.com')
        driver.find_element_by_xpath('/html/body/header/div/ol[1]/li[1]/a').click()
        driver.find_element_by_xpath('//*[@id="product-lob-nav"]/nav/a[2]').click()
        driver.find_element_by_xpath('//*[@id="product-main-nav"]/nav[1]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="wrapper"]/footer/div/div/div[2]/a[2]').click()
    except Exception:
        print('Test failed')