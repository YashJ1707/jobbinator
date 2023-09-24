from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from services.driver_service import getWebDriver
from scrapers.indeed_scraper.scrape_logic import scrapeJobs

def scrapeIndeedJobs():
    jobs=["Flutter","Backend","Frontend","Cloud"]
    driver=getWebDriver()
    for job in jobs:
        driver.get("https://uk.indeed.com")
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="text-input-what"]')))
            search_field=driver.find_element(By.XPATH,'//*[@id="text-input-what"]')
            search_button=driver.find_element(By.XPATH,'//button[@class="yosegi-InlineWhatWhere-primaryButton"]')
            sleep(0.5)
            search_field.send_keys(job)
            sleep(1)
            search_button.click()
            sleep(1)
            scrapeJobs(driver)
        except:
            driver.save_screenshot("screenshot.png")

        
    