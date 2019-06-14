import time
import base64
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


url = "https://github.com/login"
driver = webdriver.Chrome(executable_path= 'C:/Users/reckonsys/anshuman-work/product-analysis/productanalysis/chromedriver.exe')
driver.get(url)

try:
    try:
        emailid=driver.find_element_by_id("login_field")
        emailid.send_keys("ans2human")
        passw=driver.find_element_by_id("password")
        pwd = base64.b64decode('your encoded password').decode("utf-8")
        passw.send_keys(pwd)
        signin=driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[4]')
        signin.click()
    except driver.find_element_by_xpath('//*[@id="js-flash-container"]/div').text:
        print("Couldn't login!! Check the credentials")
        driver.close()

    dropdwn = driver.find_element_by_xpath('/html/body/div[1]/header/div[8]/details/summary/img')
    dropdwn.click()
    profile = driver.find_element_by_xpath('/html/body/div[1]/header/div[8]/details/details-menu/a[1]')
    profile.click()
    time.sleep(5)


    uname = driver.find_element_by_xpath('//h1[@class="vcard-names"]/span').text
    repos = driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div[2]/nav/a[2]/span').text
    usrnme = driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[1]/div[2]/div[2]/div[2]/h1/span[2]').text
    position = driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[1]/div[2]/div[2]/div[5]/div/div[2]/div').text
    company = driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[1]/div[2]/div[2]/div[5]/div/ul/li[1]/span').text
    city = driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[1]/div[2]/div[2]/div[5]/div/ul/li[2]/span').text
    

    datal = list(zip([usrnme],  [uname], [repos], [position], [company], [city]))
    dt = pd.DataFrame(datal, columns = ['Username', 'Name', 'Repositories', 'Position', 'Company', 'City'])
    print(dt)
    driver.close()

except NoSuchElementException:
    print("Couldn't login!! Check the credential")
    driver.close()

