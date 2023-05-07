import requests
from bs4 import BeautifulSoup

def get_stock_price(company):
    # Construct the Google search URL
    url = f"https://www.google.com/search?q={company}+stock+price"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the stock price in the parsed HTML content
    try:
        stock_price = soup.find("div", class_="BNeawe iBp4i AP7Wnd").get_text()
    except:
        stock_price = f"Unable to get stock price for {company}"

    return stock_price

# Example usage
stock_price = get_stock_price("Tesla")
print(stock_price)
