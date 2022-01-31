#Import
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def get_html_incidents():

    # Go to sign in page
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
    driver.get("https://servicecenter.connectmaster.com/en-US/support/")
    driver.find_element_by_xpath('//*[@id="navbar"]/div[1]/ul/li[9]/a').click()

    # Insert user/pass and login
    username = driver.find_element_by_id('Email')
    password = driver.find_element_by_id('PasswordValue')
    username.send_keys('support.cm@netconamericas.com')
    password.send_keys('Netcon.2019')
    driver.find_element_by_xpath('//*[@id="submit-signin-local"]').click()

    #Wait for page to load
    time.sleep(10)

    # Get Open Incidents Page HTML
    html_incidents = driver.page_source

    # Parser HTML page
    html_incidents = BeautifulSoup(html_incidents, 'html.parser')

    return html_incidents

if __name__ == "__main__":
    get_html_incidents()