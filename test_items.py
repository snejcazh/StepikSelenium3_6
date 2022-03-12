# import time
from selenium.webdriver.common.by import By


def test_add_to_cart_button_on_page(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    # time.sleep(30)
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), "Button not found"