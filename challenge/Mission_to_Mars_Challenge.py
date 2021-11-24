# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

html = browser.html
soup_img = soup(html, 'html.parser')


img_cerberus = soup_img.find('a', 'itemLink product-item').get('href')

img_schia = soup_img.find_all('a', 'itemLink product-item')[2].get('href')

img_syrt = soup_img.find_all('a', 'itemLink product-item')[4].get('href')

img_valles = soup_img.find_all('a', 'itemLink product-item')[6].get('href')

url = 'https://marshemispheres.com/'
browser.visit(url)

url_list = []
links = browser.find_by_css('a.product-item img')

for i in range(len(links)):
    hemisphere = {}
    browser.find_by_css('a.product-item img')[i].click()
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    hemisphere['title'] = browser.find_by_css('h2.title').text
    url_list.append(hemisphere)
    browser.back()

browser.quit()





