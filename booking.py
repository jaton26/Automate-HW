from selenium import webdriver
import time     # Only used for testing purposes. 

def sign_in(driver):
    username = driver.find_element_by_id('okta-signin-username')
    username.send_keys("")

    password = driver.find_element_by_id('okta-signin-password')
    password.send_keys("")

    button = driver.find_element_by_id('okta-signin-submit')
    button.click()

    return driver

if __name__ == "__main__":
    # Using chrome to access the web
    driver = webdriver.Chrome()

    # Open the website
    driver.get('https://sjsu.okta.com/login/login.htm?fromURI=%2Fapp%2Fsanjosestateuniversity_devshibbolethsp_1%2Fexka0rxhebkgWRJIt0x7%2Fsso%2Fsaml%3FSAMLRequest%3DfVJNU8IwEP0rndxpQlqgZCgzKAdxUBlAnfHCpGWxgTap2RTh39uCnwc57%252FvY93YHKIu8FKPKZXoObxWg8w5FrlGcBjGprBZGokKhZQEoXCoWo7up4D4TpTXOpCYn3ggRrFNGXxuNVQF2AXavUnicT2OSOVeioFStS9b2cYuVD%252BuKLjKVJCYHl%252FmIhjaqnM4eFkvijes1lJaN4A%252F9RDQ7J%252F3UFFSWJUWptwZrrHRQabUHi8odV2vY47c2lqs2hcNOMnvIINm9Ps9vJ44derQxbUISbzKOyYqxDYeIh0E%252FCoIk4rzTj%252FgmCqEXhkGnm9QwxAomurbTLiaccdZivMX7S9YVQShY74V4s89KrpReK%252F16ub%252FkDEJxs1zOWufoT02IJnYNIMNBs6A4Gdtfd7ksK7%252BOQYb%252FVP9Tz4D%252BcjjbleK%252BlpyMZyZX6dEb5bl5v7ZQdxyTNqHDM%252BXvzww%252FAA%253D%253D%26RelayState%3Dss%253Amem%253A4cfdbe30d61eb7cf8021e3a1328c959c5740b66a7813822f48d4d8f14c071824')
    sign_in(driver)

    driver.close()
