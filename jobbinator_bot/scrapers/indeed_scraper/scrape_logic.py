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

def scrapeJobs(driver):
    try:
        scrapedData=[]
        #Get driver and webpage
        # driver=getWebDriver()
        # driver.get(url)
        driver.maximize_window()
        jobNumber=1

        # Get number of pages for pagination
        nav=driver.find_element(By.CLASS_NAME, 'jobsearch-LeftPane').find_element(By.TAG_NAME, 'nav')
        pages: int=int(len(nav.find_elements(By.TAG_NAME, 'div'))-1)

        while(pages>0):

            sleep(0.1)

            # Scrape each job
            jobList=driver.find_elements(by=By.XPATH, value='//*[@id="mosaic-provider-jobcards"]/ul/li')
            for job in jobList:
                try:
                    # Get basic details
                    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
                    try:
                        jobName=job.find_element(by=By.TAG_NAME, value="a")
                    except Exception as error:
                        # print(error)
                        print(job.text)
                    
                    buttons=getNavButtons(driver)

                    # Click on the job panel
                    driver.execute_script("arguments[0].scrollIntoView();", jobName)
                    driver.execute_script("arguments[0].click();", jobName)

                    # Wait for the job panel to open
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div')))
                    jobDescription=""
                    try:    
                        companyName=driver.find_element(By.XPATH,'//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div/span/a').text
                    except:
                        try:
                            companyName=driver.find_element(By.XPATH,'//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/span/a').text
                        except:
                            print("company name")
                    try:
                        companyLocation=job.find_element(By.XPATH,'//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div').text
                        
                    except Exception as err:
                        try:
                            job.find_element(By.XPATH,'//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div').text
                        except:
                            # print(err)
                            print(companyName)
                            print('location issue')
                    try:
                        datePosted=job.find_element(By.XPATH,'//*[@id="mosaic-provider-jobcards"]/ul/li['+str(jobNumber)+']/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[1]/span[1]').text

                    except Exception as e:
                        print(e)
                        print(companyName)
                    try:
                        jobDescription=driver.find_element(By.XPATH,'//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[2]').text
                    except:
                        try:
                            jobDescription=driver.find_element(By.XPATH,'//*[@id="jobDescriptionText"]').text
                        except:
                            print(jobName.text)

                    salary=""
                    try:
                        salary=driver.find_element(By.XPATH,'//*[@id="jobDetailsSection"]/div[2]/div[2]/span/div/div/div').text
                    except:
                        pass
                    try:   
                        parts=datePosted.partition('\n')
                        date=parts[len(parts)-1]
                    except:
                        pass
                    
                    jobNumber=jobNumber+1
                    description=jobDescription.replace('\n','\\n')
                    expected_tags=getTags(description)
                    tags=""
                    for skills in expected_tags:
                        tags=tags+skills+","
                    tags=tags[:-1]
                    print(tags)
                    scrapedJob=Job(companyName,jobName.text,date,salary,companyLocation,description,jobName.get_attribute('href'),tags)  
                    scrapedData.append(scrapedJob)
                    sleep(1.5)

                except Exception as ex:
                    print(ex)

            # Click next on next job
            driver.execute_script("arguments[0].click();", buttons[len(buttons)-1])
            jobNumber=1

            # Wait for sometime to avoid detection
            sleep(1.5)

            # Check if the pop up for email opens after getting to the next page and close if opened
            try:
                driver.find_element(By.XPATH,'//*[@id="mosaic-desktopserpjapopup"]/div[1]/button').click()
                print("clicked")
                pages=pages-1
                if(pages==0):
                    break
                continue
            except:
                pages=pages-1
                print(pages)
                if pages==0:
                    break
                continue
        # print(len(scrapedData))
        try:
            upsertData(scrapedData)
            print("added data")
        except Exception as err:
            print(err)
            print("error adding data")
    except Exception as ex:
            print(scrapedData)
            print("error")
            print(ex)
    
# Function to get button to go to next page
def getNavButtons(driver: webdriver):
    nav=driver.find_element(By.CLASS_NAME, 'jobsearch-LeftPane').find_element(By.TAG_NAME, 'nav')
    buttons=nav.find_elements(By.CLASS_NAME,"css-akkh0a")
    return buttons

def saveJobDetails(jobDetails):
    print(jobDetails.find_element(By.TAG_NAME, "a").text)