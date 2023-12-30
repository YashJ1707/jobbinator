from selenium import webdriver 

def getWebDriver():
    options = webdriver.ChromeOptions()

    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    # options.headless=True
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    options.add_argument('--no-proxy-server')
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument(f'user-agent={user_agent}')

    chrome_driver_binary = "/Users/yashjaybhaye/Programming/Spring/Spring Boot/jobbinator.io/chromedriver"
    driver = webdriver.Chrome( options)
    return driver
