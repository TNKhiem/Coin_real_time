import requests
#Ham xuat ra gia dong tien ao theo loai tien te duoc chon
def GetData(api_key,loai_tien_ao,loai_tien_te):
     price=[]
     url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
     headers = {
              'Accepts': 'application/json',
              'X-CMC_PRO_API_KEY': api_key
     }
     parameters = {
         'convert': loai_tien_te
     }
     response = requests.get(url, headers=headers, params=parameters)
     response_json = response.json()
     btc_price = response_json['data'][loai_tien_ao]
     price.append(btc_price['quote'][loai_tien_te]['price'])
     return price

#api_key="d4e19d4e-eef3-48da-aea8-6bb8c9826532"
#price=GetData(api_key,loai_tien_ao=0,loai_tien_te='VND')
#print(price)




