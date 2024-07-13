from radish import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time
import io
import re

#defining a chrome_options object for configuring Chrome WebDriver options
chrome_options = Options()

#runs the browser in headless mode
chrome_options.add_argument("--headless")

#disables the sandboxing feature as we are running in headless mode
chrome_options.add_argument("--no-sandbox")

#disables GPU acceleration, improves performance
chrome_options.add_argument("--disable-gpu")

#initializes a Chrome WebDriver instance with specific options
driver = webdriver.Chrome(options=chrome_options)

#runs before each scenario
@before.each_scenario
def wait_time(step):
    #sleep for 1 second
    time.sleep(1)

@given("User enters visual user Username and Password")
def user_enters_visual_username_and_password(step):
    #get url for web shopp
    nav_url()
    type_usr_name().send_keys("visual_user")
    type_passwd().send_keys("secret_sauce")

    #click on login button
    login_btn().click()

@given("User should navigate to login page")
def user_should_navigate_to_login_page(step):
    #additional sleep for 2 seconds
    time.sleep(1)
    nav_url()

@when("User enters the empty Username and Password")
def user_enters_the_empty_username_and_password(step):
    #entering empty username and password
    type_usr_name().send_keys("")
    type_passwd().send_keys("")

    #after entering username and password, click on login button
    login_btn().click()

@when("User enters correct Username and Password")
def user_enters_correct_username_and_password(step):
    #entering correct username and password
    type_usr_name().send_keys("standard_user")
    type_passwd().send_keys("secret_sauce")

    #after entering username and password, click on login button
    login_btn().click()

@when("User enters Username and no Password")
def user_enters_username_and_no_password(step):
    #entering empty password
    type_usr_name().send_keys("standard_user")
    type_passwd().send_keys("")

    #after entering username and password, click on login button
    login_btn().click()

@then("User should see the correct error message")
def user_should_see_the_correct_error_message(step):
    #fetching error message
    errmsg = err_msg().get_attribute("innerText")
    if (errmsg == "Epic sadface: Username is required"):
        print("Error message is correct: " + errmsg)
    else:
        print("Error message is wrong: " + errmsg)

@then("User should see the Password is required error message")
def user_should_see_the_correct_error_message(step):
    #fetching error message
    errmsg = err_msg().get_attribute("innerText")
    if (errmsg == "Epic sadface: Password is required"):
        print("Error message is correct: " + errmsg)
    else:
        print("Error message is wrong: " + errmsg)

@when("Navigate user to left sidebar")
def navigate_user_to_left_sidebar(step):
    side_nav_button().click()

    #additional sleep for 2 seconds
    time.sleep(2)

    #click on logout button
    click_on_logout().click()

@then("Logout user from web shop")
def logout_user_from_swag_labs(step):
    if login_btn().is_displayed():
        print("Logout successfully")
    else:
        print("Unable to logout")

@then("Navigate user to shop home page")
def navigate_user_to_shop_home_page(step):
    if app_logo().is_displayed():
        print("Navigated Successfully")
        time.sleep(2)
    else:
        print("Not navigated")

@when("User clicks add to cart button")
def user_clicks_add_to_cart_btn(step):
    click_add_to_cart_btn()

@then("User should see the updated cart icon")
def user_should_see_the_updated_cart_icon(step):
    #fetch number of items added to the cart
    numOfitems = cart_icon_container().get_attribute("innerText")
    if (numOfitems) == "1":
        print("Cart badge is updated successfully")
    else:
        print("Fail to update")

@then("User finds the cart items added to cart")
def user_finds_the_cart_items(step):
    cart_icon_container().click()
    cartItemNames = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    if int(cart_qn()[0].text) > 0:
        print("Add to cart successfully")
    else:
        print("Fail to add to cart")

@then("User is now checked out")
def user_is_now_checked_out(step):
    #click on the cart icon
    cart_icon_container().click()

    #click on checkout button
    checkout_btn().click()

    #checks if title page is loaded successfully
    if title_page().is_displayed():
        print("Navigated successfully")
    else:
        print("Not navigated")

def side_nav_button():
    return driver.find_element(By.XPATH, "//*[@id=\"react-burger-menu-btn\"]")

def click_on_logout():
    return driver.find_element(By.XPATH, "//*[@id=\"logout_sidebar_link\"]")

def login_btn():
    return driver.find_element(By.XPATH, "//*[@id=\"login-button\"]")

def title_page():
    return driver.find_element(By.XPATH, "//span[@class='title']")

def checkout_btn():
    return driver.find_element(By.XPATH, "//button[@id='checkout']")

def cart_icon_container():
    return driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    #return driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a/span")

def cart_qn():
    return driver.find_elements(By.CLASS_NAME, "cart_quantity")

def nav_url():
    #url for the web shop
    url = "https://www.saucedemo.com/"
    driver.get(url)

def app_logo():
    return driver.find_element(By.CLASS_NAME, "app_logo")

def err_msg():
    return driver.find_element(By.CLASS_NAME, "error-message-container")

def login_btn():
    return driver.find_element(By.NAME, "login-button")

def type_usr_name():
    return driver.find_element(By.NAME, "user-name")

def type_passwd():
    return driver.find_element(By.NAME, "password")

def click_add_to_cart_btn():
    element = driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()