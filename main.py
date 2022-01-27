from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import creds

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
opt.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })
driver = webdriver.Chrome(creds.path,options=opt)
driver.get(creds.url)

def login():
    print("Login Initiated ... ")
    time.sleep(5)
    email = driver.find_element_by_xpath('//*[@id="i0116"]')
    email.click()
    email.send_keys(creds.email)
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(5)
    password = driver.find_element_by_xpath('//*[@id="i0118"]')
    password.click()
    password.send_keys(creds.passwd)
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    print("Email entered ...")
    time.sleep(30)

login()
time.sleep(10)
driver.quit()