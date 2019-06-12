from selenium import webdriver
from behave import*
import os
from pathlib import Path

def before_all(context):
	ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
	project_dir = Path(ROOT_DIR).parent
	chromedriver = (os.path.join(project_dir, 'resource/chromedriver'))
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	#options.add_argument('--incognito')
	options.add_argument('--start-maximized')
	options.add_argument('--disable-gpu')
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--window-size=1920,1080')
	#options.add_argument('log-level=3')
	context.browser = webdriver.Chrome(executable_path=chromedriver,chrome_options=options)
	BASE_URL = os.environ["BASE_URL"]
	context.browser.get(BASE_URL)
	context.browser.maximize_window()
	context.browser.implicitly_wait(15)

def after_all(context):
    context.browser.quit()
