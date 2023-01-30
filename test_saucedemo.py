# pip install playwright
# pip install pytest-playwright
# to start testing use command : pytest


def test_login_fail(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('//input[@placeholder="Username"]', 'standard_user')
    page.click("#login-button")
    assert page.inner_text('[data-test="error"]') == "Epic sadface: Password is required"


def test_login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('//input[@placeholder="Username"]', 'standard_user')
    page.fill('//input[@placeholder="Password"]', 'secret_sauce')
    page.click("#login-button")
    assert page.inner_text('[class="title"]') == "PRODUCTS"

def test_ad_to_card(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('//input[@placeholder="Username"]', 'standard_user')
    page.fill('//input[@placeholder="Password"]', 'secret_sauce')
    page.click("#login-button")

    page.click("[class='inventory_item_name']")
    page.click('#add-to-cart-sauce-labs-backpack')
    assert page.inner_text('[class="btn btn_secondary btn_small btn_inventory"]') == "REMOVE"

