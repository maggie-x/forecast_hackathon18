import selenium
import time
import os

from selenium import webdriver



def search_name(company_name):
    input_place = driver.find_element_by_name('search_api_views_fulltext')
    input_place.send_keys(company_name)
    time.sleep(1)
    search_button = driver.find_element_by_id('edit-submit-registrations-search')
    search_button.click()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.handbook.unsw.edu.au/undergraduate/specialisations/2019/compa1")
    time.sleep(1)
    same = []
    same = driver.find_elements_by_xpath("//*[contains(text(), 'Course')]")
    same[1].click()