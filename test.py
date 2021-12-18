import getdata
import sendmessage
import datafilter
import time
#____________________________________________________

api_key="d4e19d4e-eef3-48da-aea8-6bb8c9826532"
bot_token='5025869025:AAGffurHxmAosrwlpMjQ9qEEDH--z5Tpekw'
chat_id= '5019415587'

#_________________________________________________________
"""""
print("1.Bitcoin\n2.Etherum ")  #Bitcoin: 0
loai_tien_ao=int(input("Nhap so tuong ung loai tien ao: "))-1
loai_tien_te=input("Nhap loai tien te ").upper() #VND or USD
gia_canhbao=float(input("Nhap gia nguy hiem can canh bao ngay: "))
X=int(input("Nhap thoi gian giua hai lan thong bao (phut): "))*60
N=2    #So moc tien trong x phut
"""""
#test_______________________________________________

loai_tien_ao=0
loai_tien_te='VND'
X=10
N=2
gia_canhbao=1132

#______________________________________________________
ds=[]

end=False
while end==False:
    price = getdata.GetData(api_key, loai_tien_ao, loai_tien_te)
    price_date = datafilter.Data_Filter(price)
    if price_date[0] <= gia_canhbao:
       sendmessage.SendAlert(price_date,bot_token,chat_id,loai_tien_ao,loai_tien_te)
    ds.append(price_date)
    if len(ds)>=N:
       sendmessage.SendMessage(ds,bot_token,chat_id,loai_tien_ao,loai_tien_te)
       ds=[]
    time.sleep(X/N)


