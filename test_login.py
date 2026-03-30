from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import time


def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        page = browser.new_page()

        try:
            login = LoginPage(page)
            login.open()
            login.login("standard_user", "secret_sauce")

            assert "inventory" in page.url
            time.sleep(2)

        except:
            page.screenshot(path="screenshots/fail_valid_login.png")
            raise

        finally:
            browser.close()


def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        page = browser.new_page()

        try:
            login = LoginPage(page)
            login.open()
            login.login("wrong_user", "wrong_pass")

            error = login.get_error_message()
            assert "Username and password do not match" in error
            time.sleep(2)

        except:
            page.screenshot(path="screenshots/fail_invalid_login.png")
            raise

        finally:
            browser.close()


def test_empty_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        page = browser.new_page()

        try:
            login = LoginPage(page)
            login.open()
            login.login("", "")

            assert "saucedemo" in page.url
            time.sleep(2)

        except:
            page.screenshot(path="screenshots/fail_empty_login.png")
            raise

        finally:
            browser.close()


def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        page = browser.new_page()

        try:
            login = LoginPage(page)
            login.open()
            login.login("standard_user", "secret_sauce")

            products = ProductsPage(page)
            products.add_product_to_cart()
            products.open_cart()

            assert "cart" in page.url
            time.sleep(2)

        except:
            page.screenshot(path="screenshots/fail_add_to_cart.png")
            raise

        finally:
            browser.close()