from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import getpass 

# Set up ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser maximized
chrome_service = Service("path/to/chromedriver")  # Replace with your ChromeDriver path
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


driver.get("https://x.com/login")
time.sleep(5)  


username = driver.find_element(By.NAME, "text")  # Find username/email field
email_or_username = input("Enter your Twitter email/username: ")
username.send_keys(email_or_username)  # Enter the username dynamically
username.send_keys(Keys.RETURN)
time.sleep(3)

password = driver.find_element(By.NAME, "password")  # Find password field
password_input = getpass.getpass("Enter your Twitter password: ")  # Secure password input
password.send_keys(password_input)  # Enter the password dynamically
password.send_keys(Keys.RETURN)
time.sleep(5)

try:
    trends_section = driver.find_element(By.XPATH, "//section[contains(@aria-labelledby, 'accessible-list')]")
    trends = trends_section.find_elements(By.XPATH, ".//span[contains(text(), '#')]")  # Adjust XPath as needed

    # Extract the top 5 trends
    top_trends = [trend.text for trend in trends[:5]]
    print("Top 5 Trends:")
    for idx, trend in enumerate(top_trends, 1):
        print(f"{idx}. {trend}")
except Exception as e:
    print(f"Error occurred: {e}")


driver.quit()
