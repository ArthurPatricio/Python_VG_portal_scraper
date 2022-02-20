#Import
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

class get_html:

    def __init__(self):
        self.user = '***'
        self.pass_ = '***'

        # Go to sign in page
        self.driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
        self.driver.get("https://servicecenter.connectmaster.com/en-US/support/")
        self.driver.find_element_by_xpath('//*[@id="navbar"]/div[1]/ul/li[9]/a').click()

        # Insert user/pass
        username = self.driver.find_element_by_id('Email')
        password = self.driver.find_element_by_id('PasswordValue')
        username.send_keys(self.user)
        password.send_keys(self.pass_)

        # Login
        self.driver.find_element_by_xpath('//*[@id="submit-signin-local"]').click()

    def get_html_incidents(self):

        # Wait for page to load
        time.sleep(10)

        # Get Open Incidents Page HTML
        html_incidents = self.driver.page_source

        # Parser HTML page
        html_incidents = BeautifulSoup(html_incidents, 'html.parser')

        return html_incidents

    def get_html_help_requests(self):

        # Go to help requests page
        self.driver.find_element_by_xpath('//*[@id="filterDropdownId"]/a/span[3]').click()
        self.driver.find_element_by_xpath('//*[@id="filterDropdownId"]/ul/li[2]/a').click()

        # Wait for page to load
        time.sleep(10)

        # Get Open Incidents Page HTML
        html_help_requests = self.driver.page_source

        # Parser HTML page
        html_help_requests = BeautifulSoup(html_help_requests, 'html.parser')

        return html_help_requests