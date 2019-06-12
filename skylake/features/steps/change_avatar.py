from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from pathlib import Path
from database import*

@given(u'avatar scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'avatar scenario - login using bot_one')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'avatar scenario - go to setting and change avatar')
def step_impl(context):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    project_dir = Path(ROOT_DIR).parent.parent
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar_sett).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar_up).send_keys(os.path.join(project_dir, 'resource/bot_one.jpg'))
    #context.browser.find_element(By.XPATH,locator.avatar_up).send_keys(os.path.join(project_dir, 'resource/husky.jpg'))
    context.browser.find_element(By.XPATH,locator.save_avatar).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.save_prof).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.save_prof).send_keys(Keys.UP + Keys.UP + Keys.UP)
    sleep(5)
    context.browser.find_element(By.XPATH,locator.sebangsa_home).click()
    sleep(5)

@When(u'avatar scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'avatar scenario - direct to sebangsa landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
