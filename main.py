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
    print("Login Initiated ...\n\n\n\n\n\n")
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
    print("Login Succeded ...\n\n\n\n\n")
    time.sleep(30)
    joinclass()

def joinclass():
    OB_class = driver.find_element_by_xpath('//*[@id="favorite-teams-panel"]/div/div[1]/div[3]/div[5]')
    OB_class.click()
    print("Clicked.............")
    time.sleep(5)
    joinbtn = driver.find_element_by_class_name("ts-calling-join-button")
    joinbtn.click()
    time.sleep(4)
    webcam = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
    if(webcam.get_attribute('title')=='Turn camera off'):
        webcam.click()
    time.sleep(1)
    microphone = driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
    if(microphone.get_attribute('title')=='Mute microphone'):
        microphone.click()
    time.sleep(1)
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()


login()
time.sleep(10)
driver.quit()