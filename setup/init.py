from page_objects.objectHandler import ObjectHandler
from playwright.sync_api import sync_playwright
# from configData import CONFIG_DATA

def ob_init(context):
    po_handler = ObjectHandler(context.page)
    return po_handler

# def get_browser_type():