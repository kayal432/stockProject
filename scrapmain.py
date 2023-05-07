from functions import *

from bs4 import BeautifulSoup 


import requests

page_main=requests.get('https://www.google.com/search?q=exide+stock+price&rlz=1C1YTUH_enIN990IN990&oq=exide+stock+&aqs=chrome.1.69i57j0i512l9.8008j1j7&sourceid=chrome&ie=UTF-8').text
print(page_main)
