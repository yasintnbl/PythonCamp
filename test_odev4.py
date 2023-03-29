from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date


class Test_Functions:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator))

    def test_ifPasswordAndNameisNull(self):
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.driver.save_screenshot(
            f"{self.folderPath}/{self.test_ifPasswordAndNameisNull.__name__}.png")

    @pytest.mark.parametrize("username", [("1"), ("2"), ("3")])
    def test_ifPasswordIsNull(self, username):
        self.waitForElementVisible((By.ID, "user-name"))
        input = self.driver.find_element(By.ID, "user-name")
        input.send_keys(username)
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.driver.save_screenshot(
            f"{self.folderPath}/{self.test_ifPasswordIsNull.__name__}-user-name-{username}.png")

    @pytest.mark.parametrize("username,password", [("locked_out_user", "secret_sauce")])
    def test_lockedOut(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userName = self.driver.find_element(By.ID, "user-name")
        userName.send_keys(username)
        self.waitForElementVisible((By.ID, "password"))
        passWord = self.driver.find_element(By.ID, "password")
        passWord.send_keys(password)
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.driver.save_screenshot(
            f"{self.folderPath}/{self.test_lockedOut.__name__}-user-name-{username}-password-{password}.png")

    def test_clickX(self):
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.waitForElementVisible((By.CLASS_NAME, "error-button"))
        xButton = self.driver.find_element(By.CLASS_NAME, "error-button")
        xButton.click()
        self.driver.save_screenshot(
            f"{self.folderPath}/{self.test_clickX.__name__}.png")

    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_goToInventory(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userName = self.driver.find_element(By.ID, "user-name")
        userName.send_keys(username)
        self.waitForElementVisible((By.ID, "password"))
        passWord = self.driver.find_element(By.ID, "password")
        passWord.send_keys(password)
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.driver.save_screenshot(
            f"{self.folderPath}/{self.test_goToInventory.__name__}-username-{username}-password-{password}.png")

    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_showProductPieces(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userName = self.driver.find_element(By.ID, "user-name")
        userName.send_keys(username)
        self.waitForElementVisible((By.ID, "password"))
        passWord = self.driver.find_element(By.ID, "password")
        passWord.send_keys(password)
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.waitForElementVisible((By.CLASS_NAME, "inventory_item"))
        item = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(
            f"{self.folderPath}/{self.test_showProductPieces.__name__}-{len(item)}.png")
        
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_addToCart(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userName = self.driver.find_element(By.ID, "user-name")
        userName.send_keys(username)
        self.waitForElementVisible((By.ID, "password"))
        passWord = self.driver.find_element(By.ID, "password")
        passWord.send_keys(password)
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.waitForElementVisible(
            (By.ID, "add-to-cart-sauce-labs-bike-light"))
        addToCartButton = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bike-light")
        addToCartButton.click()
        self.driver.save_screenshot(
            f"{self.folderPath}/{self.test_addToCart.__name__}.png")

    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_shoppingCardButton(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userName = self.driver.find_element(By.ID, "user-name")
        userName.send_keys(username)
        self.waitForElementVisible((By.ID, "password"))
        passWord = self.driver.find_element(By.ID, "password")
        passWord.send_keys(password)
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.waitForElementVisible(
            (By.ID, "add-to-cart-sauce-labs-bike-light"))
        addToCartButton = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bike-light")
        addToCartButton.click()
        self.waitForElementVisible((By.CLASS_NAME, "shopping_cart_link"))
        shoppingCardButton = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        shoppingCardButton.click()
        self.driver.save_screenshot(
            f"{self.folderPath}/{self.test_shoppingCardButton.__name__}.png")

    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_removeButton(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userName = self.driver.find_element(By.ID, "user-name")
        userName.send_keys(username)
        self.waitForElementVisible((By.ID, "password"))
        passWord = self.driver.find_element(By.ID, "password")
        passWord.send_keys(password)
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.waitForElementVisible(
            (By.ID, "add-to-cart-sauce-labs-bike-light"))
        addToCartButton = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bike-light")
        addToCartButton.click()
        self.waitForElementVisible((By.CLASS_NAME, "shopping_cart_link"))
        shoppingCardButton = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        shoppingCardButton.click()
        self.waitForElementVisible((By.ID, "remove-sauce-labs-bike-light"))
        removeButton = self.driver.find_element(
            By.ID, "remove-sauce-labs-bike-light")
        removeButton.click()
        self.driver.save_screenshot(
            f"{self.folderPath}/{self.test_removeButton.__name__}.png")
