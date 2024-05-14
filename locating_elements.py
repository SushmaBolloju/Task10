import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

paths = r"C:\Users\chand\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options=Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open the Instagram profile
driver.get("https://www.instagram.com/guviofficial/")
driver.maximize_window()
time.sleep(3)

# Finding follower count element
follower_count_element = driver.find_element(By.XPATH,'//*[@id="mount_0_0_ix"]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span')

# Extracting the follower count text
follower_count_text = follower_count_element.get_attribute('title')


# Finding following count element using relative XPATH
following_count_element = driver.find_element(By.XPATH,'//*[@id="mount_0_0_ix"]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span')
# Extracting the following count text
following_count_text = following_count_element.text

print("Total number of followers:", follower_count_text)
print("Total number of following:", following_count_text)

# Close the browser
driver.quit()














