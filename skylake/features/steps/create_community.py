from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from pathlib import Path
from database import*

@given(u'create comm scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'create comm scenario - login as bot_one')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'create comm scenario - create test_legion1 community')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.create_community)
    context.browser.find_element(By.XPATH,locator.create_community).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.topic).click()
    context.browser.find_element(By.XPATH,locator.topic_button).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.community_name).send_keys(database.userdata["community"])
    sleep(1)

@then(u'create comm scenario - add bio in description')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.community_desc).send_keys(database.userdata["bio"])
    context.browser.find_element(By.XPATH,locator.comm_btn1).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_btn2).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.sett_savebtn).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.skip_invtbtn).click()
    sleep(3)

@then(u'create comm scenario - go to setting and set avatar')
def step_impl(context):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    project_dir = Path(ROOT_DIR).parent.parent

    context.browser.find_element(By.XPATH,locator.comm_settdot).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.comm_settpage).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_avatar).send_keys(os.path.join(project_dir, 'resource/bot_one.jpg'))
    context.browser.find_element(By.XPATH,locator.save_avatarcomm).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.save_commprof).click()
    sleep(10)
    context.browser.find_element(By.XPATH,locator.save_commprof).send_keys(Keys.PAGE_UP)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_home).click()
    sleep(5)

@then(u'create comm scenario - back to profile')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_settdot)

@then(u'create comm scenario - go to setting and delete test_legion1')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_settdot).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_settpage).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.delete_comm_button).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.delete_comm_name).send_keys(database.userdata["community"])
    context.browser.find_element(By.XPATH,locator.delete_comm_exec).click()
    sleep(5)

@when(u'create comm scenario - logout as bot_one')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'create comm scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
