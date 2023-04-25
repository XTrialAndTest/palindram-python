from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# o = Options()
# o.add_experimental_option('detach', True)
# service = ChromeService(executable_path=ChromeDriverManager().install())

# driver = webdriver.Chrome(service=service)
# # driver = webdriver.Chrome(options=o, service=Service(
# #     ChromeDriverManager().install()))
# driver.get('https://www.jumia.co.ke/')
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# driver.get('https://www.jumia.co.ke/')
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# from selenium import webdriver


# def test_eight_components():
# driver = webdriver.Chrome()

driver.get("https://jiji.co.ke//")

# title = driver.title

# assert title == "Web form"

# driver.implicitly_wait(0.5)

# text_box = driver.find_element(by=By.NAME, value="Supermarket")
links = driver.find_elements(
    by=By.CSS_SELECTOR, value="#__layout > div > div.h-bg-jiji-body.h-min-height-100p.h-width-100p.h-flex > div > div.b-content-wrapper > div > div > div.container > div > div.b-main-page-categories-wrapper.b-main-page-categories-wrapper--desktop > div > div > div > div > div > div > div > div > div > div > div > a>")
# for i in links:

#     print(i)
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# text_box.click()

# message = driver.find_element(by=By.ID, value="message")
# value = message.text
# assert value == "Received!"
for i in links:
    i.click()
    # print(i.get_attribute('innerHTML'))
    # if 'Appliances' in i.get_attribute('innerHTML'):
    #     i.get_attribute('href')
    # break
    # print(i.click())
# print()
# print(len(links))
# driver.quit()
