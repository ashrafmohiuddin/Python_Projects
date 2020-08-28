from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
# credentials is a python file which contains Email id, Password as email_id ,pwd
from credentials import email_id, pwd


PATH = "C:\Program Files (x86)\chromedriver.exe"
# To open the instagram login page
# mobile_emulation = {"deviceName": "iPhone X"}
# chrome_options = Options()
# chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--auto-open-devtools-for-tabs")
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(executable_path=PATH)

driver.get("https://www.instagram.com/accounts/login/")

try:
    # This below code waits until the page is loaded then locates the input field of username
    user_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    user_id.send_keys(email_id)
    # This locates the password input field
    password = driver.find_element_by_name("password")
    password.send_keys(pwd)
    password.send_keys(Keys.RETURN)

    # A dialog pops up in the browser. We wait till page is loaded and press Not-now
    not_now_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button"))
        )
    not_now_button.click()
    not_now_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))
    )
    not_now_button.click()

    profile = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[1]/a")
    profile.click()
    # This clicks the followers button on the profile page.
    followers = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"))
    )
    followers.click()

    # This scrolls the page also waits till reload.
    time.sleep(2)
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(1)
        ht = driver.execute_script("""
                    arguments[0].scrollTo(0, arguments[0].scrollHeight);
                    return arguments[0].scrollHeight;
                    """, scroll_box)
    time.sleep(2)
    links = scroll_box.find_elements_by_tag_name('a')
    # followers_names is the list of people following you.
    followers_names = [name.text for name in links if name.text != '']
    print(len(followers_names))

    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
    time.sleep(2)

    following = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a"))
    )
    following.click()
    time.sleep(2)
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(1)
        ht = driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight);
                        return arguments[0].scrollHeight;
                        """, scroll_box)
    time.sleep(2)
    links = scroll_box.find_elements_by_tag_name('a')
    # following_names is the list of people followed by you.
    following_names = [name.text for name in links if name.text != '']
    print(len(following_names))

    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()

    time.sleep(2)

    names = [x for x in following_names if x not in followers_names]
    print(len(names))
    print("\n".join(x for x in names))

finally:
    driver.close()



