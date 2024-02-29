from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def GetPublicComments(post_url):
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/p/Cp0MhKUOTq4/')
    time.sleep(5)

    Wait = True

    while Wait:
        try:
            cont = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        except:
            cont= None
        if cont:
            cont.click()
            Wait = False

    time.sleep(10)
    comments = []
    elements = driver.find_elements(By.CLASS_NAME,'_a9zs')
    for element in elements:
        if elements.index(element) > 0:
            element.find_element(By.TAG_NAME, 'span')
            comments.append(element.text)
    # element_list = [element.text for element in elements]

    driver.quit()
    return comments

def GetPrivateComments():
    pass