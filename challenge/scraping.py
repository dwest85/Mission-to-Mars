# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

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

    # Run all scraping functions and store results in a dictionary
    
    data = {
        "url_title": hemisphere['title'],
        "url_string": hemisphere['img_url'],
        "Hemisphere": url_list
    }

    # Stop webdriver and return data
    browser.quit()
    return data


# def mars_news(browser):

#     # Scrape Mars News
#     # Visit the mars nasa news site
#     url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
#     browser.visit(url)

#     # Optional delay for loading the page
#     browser.is_element_present_by_css('div.list_text', wait_time=1)

#     # Convert the browser html to a soup object and then quit the browser
#     html = browser.html
#     news_soup = soup(html, 'html.parser')

#     # Add try/except for error handling
#     try:
#         slide_elem = news_soup.select_one('div.list_text')
#         # Use the parent element to find the first 'a' tag and save it as 'news_title'
#         news_title = slide_elem.find('div', class_='content_title').get_text()
#         # Use the parent element to find the paragraph text
#         news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

#     except AttributeError:
#         return None, None

#     return news_title, news_p


# def featured_image(browser):
#     # Visit URL
#     url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
#     browser.visit(url)

#     # Find and click the full image button
#     full_image_elem = browser.find_by_tag('button')[1]
#     full_image_elem.click()

#     # Parse the resulting html with soup
#     html = browser.html
#     img_soup = soup(html, 'html.parser')

#     # Add try/except for error handling
#     try:
#         # Find the relative image url
#         img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

#     except AttributeError:
#         return None

#     # Use the base url to create an absolute url
#     img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

#     return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        # df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
        
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=True)
        
        url = 'https://marshemispheres.com/'
        browser.visit(url)
        
        df = pd.read_html(url)
        
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

            return hemisphere

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Image', 'Title']
    df.set_index('Title', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())

