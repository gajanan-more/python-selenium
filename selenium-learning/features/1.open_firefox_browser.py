from selenium import webdriver
from selenium.webdriver.firefox.options import Options


"""
We have kept the geckodriver in the system's path so Selenium will then search
for the geckodriver in the system's PATH. 
Make sure the geckodriver executable is in a directory listed in your system's PATH for this to work.
"""

# Initialize Firefox WebDriver
driver_firefox = webdriver.Firefox(options=Options())

"""
If you know the PATH or kept the driver in custom PATH, you have to follow:

geckodriver_path = 'path/to/geckodriver'

# Initialize Firefox WebDriver
driver_firefox = webdriver.Firefox(executable_path=geckodriver_path)
"""

# Open Google.com in Firefox Browser
driver_firefox.get("https://www.google.com")

# Close the Firefox Browser
driver_firefox.quit()