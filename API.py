import requests
import pyttsx3

print('______________________________________________Hi______________________________________________')
print('*you get https://nomics.com ,only submit email received APIKey and see all price crypto coin,\n So you can only BTC price without see website')
select_api=input('you receive APIKey?,plese enter APIKey otherwise enter NO :')
if select_api == 'NO':
    res =requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    x=res.json()
    result=x['bpi']['USD']['rate']
    price=int(float(result.replace(',','')))
else :
    crypto=input("Plese enter symbol crypto(ex:ETH):")
    response=requests.get(f'https://api.nomics.com/v1/currencies/ticker?key={select_api}&ids={crypto}&interval=1d,30d&convert=USD')
    data=response.json()
    result=data[0]['price']
    price=float(result)
    if price < 1 :
        price = format(price,'.4f')
    else:
        price=int(float(price))
print(price)
eng=pyttsx3.init()
eng.say(f'{price}')
eng.runAndWait()