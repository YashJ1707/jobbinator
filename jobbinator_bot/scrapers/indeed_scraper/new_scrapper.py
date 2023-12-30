from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from services.driver_service import getWebDriver
from selenium import webdriver
from models.job_model import Job
from services.db_services.pg_service import upsertData
from services.tags_extraction.tags import getTags

def scrapeIndeedJob(driver: webdriver):
    scrapedData=[]