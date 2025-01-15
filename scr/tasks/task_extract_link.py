import requests
from bs4 import BeautifulSoup
from prefect import task

URL = 'https://www.linkedin.com/jobs/search/?geoId=102927786&keywords='

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

@task(name='Extraer data de Linkein')
def task_extract_link(skill):
    url = requests.get(URL+skill, headers=HEADERS)
   
    offer_list = []
   
    if(url.status_code == 200):
        html = BeautifulSoup(url.text,'html.parser')
        ul_offers = html.find('ul',{'class':'jobs-search__results-list'})
        li_offers = ul_offers.find_all('li')
            
        for offer in li_offers:
            offer_title = offer.find('h3',{'class':'base-search-card__title'})
            offer_location = offer.find('span',{'class':'job-search-card__location'})
            offer_url = offer.find('a')
                        
            title = offer_title.get_text().strip() if offer_title else ''
            location = offer_location.get_text().strip() if offer_location else ''
            url_value = offer_url['href'].strip() if offer_url else None

            offer_list.append((title,location,url_value,skill))  
        return offer_list            
    else:
        print(f"error : {url.status_code}")
    
    

    