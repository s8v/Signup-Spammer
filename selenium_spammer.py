from selenium import webdriver
import random
import string

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    executable_path="C:\Program Files\chromedriver.exe", chrome_options=chrome_options)
usernamewe =  ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
passwordwe = "Exploitedbymaxlol1"
emailwe = f"exploitedbymaxlol@{''.join(random.choice(string.ascii_lowercase) for _ in range(14))}.net"
submitwe = "Create"
url = "https://pillstress.xyz/register.php"
driver.get(url)
username = driver.find_element_by_name("username")
username.send_keys(usernamewe)
email = driver.find_element_by_name("email")
email.send_keys(emailwe)
driver.find_element_by_name('password').send_keys(passwordwe)
driver.find_element_by_name('cpassword').send_keys(passwordwe)
driver.find_element_by_css_selector(".btn").click()