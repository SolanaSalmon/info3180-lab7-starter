import requests
from bs4 import BeautifulSoup
import urlparse


url = "https://www.walmart.com/ip/54649026"

def get_imgsList(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    # This will look for a meta tag with the og:image property
    og_image = (soup.find('meta', property='og:image') or
                    soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        pass
        #print og_image['content']
        #print ''

    # This will look for a link tag with a rel attribute set to 'image_src'
    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        pass
        #print thumbnail_spec['href']
        #print ''



	# This returns a list of image URLs
    imgsList = [] 
    for img in soup.findAll("img", src=True):
        
        imgsList.append(urlparse.urljoin(url, img["src"]))
        
    return imgsList
    
print get_imgsList(url)