from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


# driver_path = './chromedriver'
# options = webdriver.ChromeOptions
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def scrape_web(url):
    driver.get(url)
    response = driver.page_source
    print(response)
    print('scraping completed')
    return response

# scrape_web('https://www.docupharm.ca')

def clean_html_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    for tag in soup(["script", "style"]):
        tag.decompose()  
    body_content = soup.body.get_text(separator="\n", strip=True)
    return body_content
    
