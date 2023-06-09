from bs4 import BeautifulSoup
import requests
# Eldorado returns status code 503
# DNS returns status code 403
# only Citilink works fine so I'm parsing it
def parse():
    url = 'https://www.citilink.ru/catalog/smartfony/APPLE'
    try:
        page = requests.get(url)
        print('Connection status code: ' + str(page.status_code))
        soup = BeautifulSoup(page.text, 'html.parser')
    except:
        print('An error occured while connecting to the site...')
        return -1

    blocks = soup.findAll('span',class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price')
    prices = []
    for data in blocks:
        prices.append(int(str(data.text).replace(' ', '').replace('\n', '')))
    print('Prices for iPhones found: ' + str(len(prices)))
    print('------------------------------------')
    print('Max price: ' + str(max(prices)))
    print('Min price: ' + str(min(prices)))
    print('Average price: ' + str(sum(prices) / len(prices)))

if __name__ == '__main__':
    parse()