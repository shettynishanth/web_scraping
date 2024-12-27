from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import uuid
import time


CONNECTION_STRING = "mongodb+srv://nnm23mc087:nnm23mc087@cluster0.rafbw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(CONNECTION_STRING)
db = client.get_database("stir_tech_db")
collection = db["myCollection"]

def setup_selenium():
   
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def scrape_trending_topics(driver):
    driver.get("https://x.com/explore")
    trends = []

    try:
        trending_section = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Trending now"]'))
        )
        
      
        trending_items = trending_section.find_elements(By.TAG_NAME, 'span')
        
       
        trends = [item.text for item in trending_items[:5]]
    except Exception as e:
        print(f"Error scraping trending topics: {e}")
    finally:
        driver.quit()
    
    return trends

def store_trends_in_db(trends, ip_address):
    unique_id = str(uuid.uuid4())
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    trend_data = {
        "_id": unique_id,
        "timestamp": timestamp,
        "ip_address": ip_address
    }

   
    for i, trend in enumerate(trends):
        trend_data[f"nameoftrend{i+1}"] = trend

    
    collection.insert_one(trend_data)
    return trend_data

def run_selenium_script():
    
    driver = setup_selenium()
    trends = scrape_trending_topics(driver)
    
    ip_address = "XXX.XXX.XXX.XXX"
    
    trend_data = store_trends_in_db(trends, ip_address)
    print(trend_data)
