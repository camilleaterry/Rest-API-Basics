import requests

# argument parser
# before run code helps defines what runtime argument
# parse the arguments



# '...' will be used to pass by the code block and come back later

def get_quote(stock, apikey):

    # replace the "demo" apikey below with
    # your own key from https://www.alphavantage.co/support/#api-key
    url = (
        'https://www.alphavantage.co/query?function=GLOBAL_QUOTE'
        f'&symbol={stock}'
        f'&apikey={apikey}'
        )
    r = requests.get(url)
    data = r.json()

    print(data)


# if __balh__ will allow you to use this command in other places

if __name__=='__main__':
    stock = input('Enter Stock: ')
    apikey = input('Enter API Key: ')
    get_quote(stock, apikey)
