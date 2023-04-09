import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import json
import time

# github: @omerahat

def get_data_from_amazon(url):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.google.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'
}
    response=requests.get(url,headers=header)
    soup=bs(response.content,"html.parser")
    
    
    title_element=soup.find('span', {'id': 'productTitle'})
    title = title_element.text.strip()
    
    price_element=soup.find("span",{"class":"a-offscreen"})
    price=price_element.text.strip()

    rating_element = soup.find('span', {'class': 'a-icon-alt'})
    rating=rating_element.text.split(" ")[0]
    
    review_element = soup.find("span",{"id":"acrCustomerReviewText"})
    review_str=review_element.text.split(" ")[0].split(",")
    review=int("".join(review_str))
    
    

    data_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data={"platform":"amazon","time": data_time,"title":title,"price":price,"review":review,"rating":rating}
    json_data=json.dumps(data)
    return json_data
"""
example:    
url = "https://www.amazon.com/dp/B09KQPHLMZ/ref=twister_B09BQGZFT1"
print(get_data_from_amazon(url))
"""


def get_data_from_ebay(url):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.google.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'
}
    response=requests.get(url,headers=header)
    soup=bs(response.content,"html.parser")
    
    
    title_element=soup.find('span', {'id': 'vi-lkhdr-itmTitl'})
    title = title_element.text.strip()

    price_element=soup.find("span",{"itemprop":"price"})
    price=price_element.text.strip()

    data_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data={"platform":"ebay","time": data_time,"title":title,"price":price}
    json_data=json.dumps(data)
    return json_data

"""
example:
url = "https://www.ebay.com/itm/185702498085?hash=item2b3cbb3f25:g:sowAAOSw--JjnX-S&amdata=enc%3AAQAHAAAA4CCfncyOGBY5iOCkVNC6iQcU46VWN8WWOHKzGK%2BXOpaPzni7zhRf0jMHkQxVvgPqgx8oznM0gnAQJLZoUPluHENVFjQYGxwC27Yvi5sbNf9rLQpLUIArLUi%2BGEj0d6E3NWwwvX9Kk0Kd1ymMNZS0%2B%2BCc5foKdP31klK9OYWczkh7FdCQPtO1bYOS9WuqG7jRQgqNJl4dpFOD9WT%2Fg5KuZFU6eHyMgXSkj2zCAlxzmrdWfkix%2B7KwSTNPk4fuyBkwFhMX7IXMN%2FNpF6sSEZ1JJ42OZBiPu%2FaMg0jRKDjSl1vP%7Ctkp%3ABFBM5PuJuOxh"
print(get_data_from_ebay(url))
"""


def get_data_from_hepsiburada(url):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.google.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'
}
    response=requests.get(url,headers=header)
    soup=bs(response.content,"html.parser")
    
    
    title_element=soup.find('h1', {'id': 'product-name'})
    title = title_element.text.strip()
    
    price_element_whole=soup.find("span",{"data-bind":"markupText:'currentPriceBeforePoint'"})
    price_element_deciminal=soup.find("span",{"data-bind":"markupText:'currentPriceAfterPoint'"})
    price=price_element_whole.text.strip()+"."+price_element_deciminal.text.strip()+" TL"
    
    rating_element = soup.find('span', {"class":"rating-star"})
    rating=rating_element.text.strip()
    

   # review_element = ???
    

    data_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data={"platform":"hepsiburada","time": data_time,"title":title,"price":price,"rating":rating}
    json_data=json.dumps(data)
    return json_data
"""
example:
url = "https://www.hepsiburada.com/philips-hd9867-90-premium-airfryer-xxl-fritoz-p-hbcv000004vgkw"
print(get_data_from_hepsiburada(url))
"""


def get_data_from_trendyol(url):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.google.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'
}
    response=requests.get(url,headers=header)
    soup=bs(response.content,"html.parser")
    
    title_element=soup.find('h1', {"class":"pr-new-br"})
    title = title_element.text.strip()

    price_element=soup.find("span",{"class":"prc-dsc"})
    price=price_element.text.strip()
    
    #review = ???
    
    #rating = ???
    

    data_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data={"platform":"trendyol","time": data_time,"title":title,"price":price}
    json_data=json.dumps(data)
    return json_data
        
"""
example:
url = "https://www.trendyol.com/kahve-dunyasi/lavi-cikolata-1-kg-bayram-hediyesi-p-102419395?boutiqueId=61&merchantId=106690&sav=true"
print(get_data_from_trendyol(url))
"""


def get_data_from_teknosa(url):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.google.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'
}
    response=requests.get(url,headers=header)
    soup=bs(response.content,"html.parser")
    
    title_element=soup.find("h1", {"class":"pdp-title"})
    title = title_element.text.strip()
    
    price_element=soup.find("span",{"class":"prc prc-last"})
    price=price_element.text.strip()

    rating_element = soup.find('div', {'class': 'prr-score-val'})
    rating=rating_element.text.split()[0]

    
    data_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data={"platform":"teknosa","time": data_time,"title":title,"price":price,"rating":rating}
    json_data=json.dumps(data)
    return json_data
"""
example:
url = "https://www.teknosa.com/apple-iphone-11-128gb-akilli-telefon-siyah-p-125077799"
print(get_data_from_teknosa(url))
"""


def get_data_from_vatan(url):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.google.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'
}
    response=requests.get(url,headers=header)
    soup=bs(response.content,"html.parser")
    
    title_element=soup.find("h1", {"class":"product-list__product-name"})
    title = title_element.text.strip()

    price_element=soup.find("span",{"class":"product-list__price"})
    price=price_element.text.strip()
    

    data_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data={"platform":"vatan","time": data_time,"title":title,"price":price}
    json_data=json.dumps(data)
    return json_data
"""
example:
url = "https://www.vatanbilgisayar.com/acer-aspire-3-7-nesil-ryzen-5-7520u-8gb-256gb-ssd-15-6inc-w11.html"
print(get_data_from_vatan(url))
"""