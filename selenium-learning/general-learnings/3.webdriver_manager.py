"""
Typically we install the webdriver which matches the version of the browser and the browser version
keep on updating every now and then. So with each browser version, we have to download the new driver
for that version and this tedious manual task we have to do for each version.
That's why we have a library "webdriver manager" available which can be used to manage the browser driver dependencies.
"""

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


#Chrome
# chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# chrome_driver.get("https://google.com")
#
# print(chrome_driver.title)
#
# chrome_driver.maximize_window()
#
# chrome_driver.minimize_window()
#
# chrome_driver.quit()


#Firefox

firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

firefox_driver.get("https://google.com")

print(firefox_driver.title)

firefox_driver.maximize_window()

firefox_driver.minimize_window()

firefox_driver.quit()
