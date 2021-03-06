# INSTALLING ALL DEPENDENCIES
# ENSURE THAT YOU HAVE SELENIUM INSTALLED, PYTHON INSTALLED, AND CHROMEDRIVER STORED IN "C:\webdrivers/chromedriver"

import time
from selenium import webdriver
import smtplib
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

################################################

# Declaring email adress and password for the email adress that is being sued to send email to your personal email.
# In order for this to work, you need to setup a gmail account that can send email autonomously.
EMAIL_ADDRESS = "******"
EMAIL_PASSWORD = "****"
subject = "Card is open"
body = "Time to try to buy"
msg = f'Subject : {subject}\n\n{body}'

subject2 = "The item has been bought, check your computer now"
body2 = "complete."
msg2 = f'Subject : {subject2}\n\n{body2}'

# enter the file location of your chromedriver
browser = "C:\webdrivers/chromedriver"

options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("window-size=1200x600")

driver = webdriver.Chrome(browser, options=options)
# 1660 super page (out of stock)
# driver.get("https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-video-card/15530046")

# safe page (in stock button)
driver.get("https://www.bestbuy.ca/en-ca/product/logitech-g305-12000-dpi-wireless-optical-gaming-mouse-black/12642295")

# driver.get("https://www.bestbuy.ca/en-ca/product/insignia-43-1080p-hd-led-tv-ns-43d420na20-only-at-best-buy/14500009")

buybutton = False
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    while not buybutton:
        # check if the button is available via searching for class name
        TheButtonItself = driver.find_element_by_xpath("//*[@id=\"test\"]/button").is_enabled()
        if not TheButtonItself:
            # button is not ready
            print("button is not ready yet")

            # refresh
            time.sleep(3)
            driver.refresh()

        elif TheButtonItself:

            # smtp.sendmail(EMAIL_ADDRESS, "bartekkowalski465@gmail.com", msg)  # send email as a notification
            addToCartButton = addButton = driver.find_element_by_xpath("//*[@id=\"test\"]/button")
            addToCartButton.click()
            print("The button was clicked")
            buybutton = True

            # 5 second delay for catch up
            time.sleep(4.5)

            cart = driver.find_element_by_class_name("basketIcon_1lhg2")
            cart.click()

            time.sleep(4.67)

            checkout = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/div[4]/div[2]/div/section/div/main/section/section[2]/div[2]/div/a/span")
            checkout.click()

            time.sleep(2.3)

            username = driver.find_element_by_xpath("//*[@id=\"username\"]")

            password = driver.find_element_by_xpath("//*[@id=\"password\"]")

            username.send_keys("***************")
            time.sleep(1.6)
            password.send_keys("***********")
            time.sleep(1.4)
            sign_in = driver.find_element_by_xpath("//*[@id=\"signIn\"]/div/button/span")
            sign_in.click()
            time.sleep(10)

            num = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/section[2]/main/section/di"
                                               "v[2]/form/div/div/div/div[2]/div[1]/div/fieldset")
            num.click()
            time.sleep(1)

            cvv = driver.find_element_by_xpath("//*[@id=\"cvv\"]")
            cvv.send_keys("***")
            cvv.send_keys(Keys.ENTER)

            time.sleep(10)

            placeOrderBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                            "/html/body/div[1]/div["
                                                                                            "6]/div["
                                                                                            "2]/div/div/div/section["
                                                                                            "2]/main/div["
                                                                                            "2]/section/section["
                                                                                            "1]/button")))
            placeOrderBtn.click()
