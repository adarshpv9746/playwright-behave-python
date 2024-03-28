from datetime import datetime
import logging
from setup.init import ob_init

import allure
from playwright.sync_api import sync_playwright


def before_all(context):
    p = sync_playwright().start()
    context.browser = p.chromium.launch(headless=False, slow_mo=1000, channel="chrome")


def after_all(context):
    
    context.browser.close()
    print("\nAfter all Feature")


def before_feature(context, feature):
    
    # Create logger
    context.logger = logging.getLogger('automation_tests')
    context.logger.setLevel(logging.DEBUG)


def after_feature(context, feature):
    
    print("\nAfter Feature")


def before_scenario(context, scenario):
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()
    context.po = ob_init(context)
    print("Before scenario\n")


def after_scenario(context, scenario):
    
    if scenario.status == 'failed':
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        screenshot_path = f'failure_screenshots/{scenario.name}_{timestamp}.png'
        context.page.screenshot(path=screenshot_path)
        screenshot_bytes = context.page.screenshot()
        allure.attach(screenshot_bytes, name=f'failed{scenario.name}_{timestamp}.png', attachment_type=allure.attachment_type.PNG)
    context.page.close()
    print("After scenario\n")


def before_step(context, step):
    
    print("After step\n")


def after_step(context, step):
    
    print("After step\n")
