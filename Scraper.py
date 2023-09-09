from selenium import webdriver  # for web automation
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys #for search bar


import time


facebook_account_gmail = "shirigaya3545@gmail.com"
facebook_account_password = "RonJoshua@3545"

involve_asia_account_gmail = "ronquirap3545@gmail.com"
involve_asia_account_pass  = "RonJoshua@3545"

shopee_url = "https://shopee.ph/"
lazada_url = "https://www.lazada.com.ph"
amazon_url = "https://www.amazon.com"

selected_url = shopee_url   

top_selling_niches = {
                "soap", "skin care", 
                "eye glass", "eyeglass anti radiation", 
                "perfume", "wireless earphone",
                "wireless keyboard", "wireless mouse",
                "mechanical keyboard", "headphone",
                "soldering iron", "electronics"
            }



options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--no-sandbox')
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                            options = options)

driver.get(selected_url)

if selected_url == shopee_url:
    try:
        time.sleep(2)
        close_btn = driver.execute_script('return document.querySelector("#main shopee-banner-popup-stateful").shadowRoot.querySelector("div.home-popup__close-area div.shopee-popup__close-btn")')
        close_btn.click()
        print("click successful")
    except Exception as e:
        print('Could not clicked')
        pass

search = driver.find_element(By.XPATH, '//*[@id="main"]/div/header/div[2]/div/div[1]/div[1]/div/form/input')
search.send_keys("soap")
search.send_keys(Keys.ENTER)

