from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'favourite scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'favourite scenario - login as bot_3')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username3"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'favourite scenario - go to timeline and wait')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'favourite scenario - favourite post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.favourite).click()
    sleep(3)

@then(u'favourite scenario - validating favourite post active')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.stats).is_displayed()
    sleep(2)

@then(u'favourite scenario - cancel fav post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.unfavourite).click()
    sleep(3)

@then(u'favourite scenario - validating post back to default')
def step_impl(context):
    try:
        context.browser.find_element(By.XPATH,locator.stats)
        status = False
    except:
        status = True
    assert_that(status, equal_to(True))

    #card_1 = card[0].text
    #component = find_element_by_tag_name("class").get_attribute("img-stats__wrapper")
    #print(dir(card))
    #assert_that(card_1, is_not(equal_to(database.userdata["vote_up_cls"])))
    sleep(2)

@when(u'favourite scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'favourite scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
