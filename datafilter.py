import datetime
#Ham xuat ra list bao gom gia tien ao va thoi gian cap nhat [price,time-date]
def Data_Filter(price):
    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime('%H:%M:%S, %d/%m/%Y')
    price.append(dt_now)
    return price

#api_key="d4e19d4e-eef3-48da-aea8-6bb8c9826532"
#price=getdata.GetData(api_key,loai_tien_ao=0,loai_tien_te='VND')
#print(price)
#price_date=Data_Filter(price)
#print(price_date)