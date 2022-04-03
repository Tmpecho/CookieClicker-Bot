from ssl import Options
import time
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.keys import Keys
import os

# open cookie clicker in chrome browser
driver = webdriver.Chrome( executable_path=r"./drivers/chromedriver")
driver.get("https://orteil.dashnet.org/cookieclicker/")

def accept_cookies(): # accept cookies
    accept_button = driver.find_element_by_class_name("cc_btn_accept_all")
    accept_button.click()

def close_achievments(): # close new achievments
    try:
        close_achievments_button = driver.find_element_by_class_name("framed.close.sidenote")
        close_achievments_button.click()
    except:
        pass

def click_cookie(): # click the cookie
    cookie_button = driver.find_element_by_id("bigCookie")
    cookie_button.click()

def buy_upgrades(): # buy the first upgrade
    try:
        upgrades = driver.find_elements_by_class_name("upgrade.enabled")
        if len(upgrades) > 0:
            for upgrade in upgrades:
                upgrade.click()
    except:
        pass

def buy_products(): # buy the biggest product
    try:
        products = driver.find_elements_by_class_name("product.enabled")
        if len(products) > 0:
            for product in products[::-1]:
                product.click()
    except:
        pass

def upgrade(): # check for upgrades and buy them
    global counter
    should_upgrade = False
    if counter < time_bewteen_upgrade:
        counter += 1
    elif counter >= time_bewteen_upgrade:
        counter = 0
        should_upgrade = True
    
    if should_upgrade == True:
        buy_products()
    
def check_golden(): # check for golden cookie and click it
    try:
        shimmers = driver.find_elements_by_class_name("shimmer")
        for shimmer in shimmers:
            shimmer.click()
    except:
        pass

# global variables
tic = 0.001
counter = 0
time_bewteen_upgrade = 400

# setup
time.sleep(3) # wait for the page to load

driver.execute_script("window.open("");") # open new tab

accept_cookies() # accept cookies

# Run the bot
while True:
    click_cookie()
    upgrade()
    check_golden()
    close_achievments()
    buy_upgrades()

    time.sleep(tic)