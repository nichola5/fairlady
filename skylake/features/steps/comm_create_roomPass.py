from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from database import*
from hamcrest import*

@given(u'create private room scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'create private room scenario - login as community owner')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'create private room scenario - go to community tab and find community')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_north_tab).click()
    sleep(4)

@then(u'create private room scenario - create private room and validating new room')
def step_impl(context):

    context.browser.find_element(By.XPATH,locator.comm_sett_gear).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_room_sidebar).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_room_add).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_room_name).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_room_name).send_keys(database.userdata["room_name"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_room_pass).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_room_pass).send_keys(database.userdata["room_pass"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_room_hint).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_room_hint).send_keys(database.userdata["room_hint"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_room_save_wpass).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_home).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_name).send_keys(Keys.PAGE_DOWN)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_room_editorlist).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_room_list).is_displayed()

    room = context.browser.find_elements(By.XPATH,locator.comm_room_list)
    sets = room[0].find_elements(By.CLASS_NAME, "list-object__item")
    assert_that(sets, has_length(equal_to(2)))


@then(u'create private room scenario - create and delete post in new room')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_room_name2).send_keys(Keys.PAGE_UP)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.button_newpost).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_editor)
    context.browser.find_element(By.XPATH,locator.comm_room_pop_editorlist).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_room_pop_editorname).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_editor).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_editor).send_keys(database.userdata["text"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_editorexec).click()
    sleep(6)
    context.browser.find_element(By.XPATH,locator.comm_name).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_name).send_keys(Keys.PAGE_DOWN)
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_editor_option).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_editor_option).send_keys(Keys.PAGE_DOWN)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_post_delete).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    sleep(5)

@then(u'create private room scenario - delete room')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.PAGE_UP)
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_sett_gear).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_room_sidebar).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_room_option).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_room_delete).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.popup).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.yes_button)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.yes_button).click()
    sleep(5)


@then(u'create private room scenario - validating deleted room')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_home).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_name).send_keys(Keys.PAGE_DOWN)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_room_editorlist).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_room_list).is_displayed()

    room = context.browser.find_elements(By.XPATH,locator.comm_room_list)
    sets = room[0].find_elements(By.CLASS_NAME, "list-object__item")
    assert_that(sets, has_length(equal_to(1)))


@then(u'create private room scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.PAGE_UP)
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'create private room scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing).is_displayed()
