from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class Functions:
    
    def ifPasswordAndNameisNull():  
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()        
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        while True:
            continue

    def ifPasswordIsNull():
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        input=driver.find_element(By.ID,"user-name")
        input.send_keys("1")        
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        while True:
            continue

    def lockedOut():
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        userName=driver.find_element(By.ID,"user-name")
        userName.send_keys("locked_out_user")  
        password=driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        while True:
            continue

    def clickX():
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        xButton=driver.find_element(By.CLASS_NAME,"error-button")
        xButton.click()
        while True:
            continue
        
    def goToInventory():
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        userName=driver.find_element(By.ID,"user-name")
        userName.send_keys("standard_user")
        password=driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        while True:
            continue

    def showProductPiece():
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        userName=driver.find_element(By.ID,"user-name")
        userName.send_keys("standard_user")
        password=driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        item=driver.find_elements(By.CLASS_NAME,"inventory_item")
        listItems=(f"Toplam ürün sayısı: {len(item)}")
        print(listItems)
        while True:
            continue

Functions.showProductPiece()        

# Functions.goToInventory()
# Functions.clickX()
# Functions.lockedOut()
# Functions.ifPasswordIsNull()         
# Functions.ifPasswordAndNameisNull()


