from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('G:\Downloads\Compressed\chromedriver.exe')
url= "https://www.cowin.gov.in/home"
driver.maximize_window()
driver.get(url)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
driver.find_element_by_css_selector('status-switch').click()

#/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[1]/div/label
#body > app-root > div > app-home > div.maplocationblock.bs-section > div > appointment-table > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > form > div > div > div:nth-child(1) > div > label
#<div _ngcontent-ujk-c68="" data-unchecked="Search By PIN" data-checked="Search By District" class="status-switch"></div>
# price=soup.find("select",{"id":"mat-select-value"})
# options = price.find_all("option")
# options1=[y.text for y in options]
# values = [o.get("value") for o in options]
# for x in range(5):
#     print (options1[x], values[x].encode('utf8'))
# driver.quit()