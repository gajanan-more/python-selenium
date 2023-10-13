from selenium import webdriver
from selenium.webdriver.chrome.options import Options


"""
We have kept the chromedriver in the system's path so Selenium will then search
for the chromedriver in the system's PATH. 
Make sure the chromedriver executable is in a directory listed in your system's PATH for this to work.
"""

# Initialize Chrome WebDriver
driver_chrome = webdriver.Chrome(options=Options())


#If you know the PATH or kept the driver in custom PATH, you have to follow:

#chromedriver_path = '/Users/gajanan/chromedriver-mac-x64/chromedriver'

# Initialize Firefox WebDriver
#driver_chrome = webdriver.Chrome(executable_path=chromedriver_path)


# Open Google.com in Chrome Browser
driver_chrome.get("https://www.google.com")

# Close the Chrome Browser
driver_chrome.quit()

