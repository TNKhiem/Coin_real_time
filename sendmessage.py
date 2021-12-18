import requests
#Ham gui tin nhan dinh ki
def SendMessage(ds,bot_token,chat_id,loai_tien_ao,loai_tien_te):
    if loai_tien_ao==0:
        ten_tien_ao='Bitcoin'
    else:
        ten_tien_ao='Etherum'
    for i in range(len(ds)):
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text=Gia {ten_tien_ao} vao luc {ds[i][1]} la {(ds[i][0])} {loai_tien_te}"

    # send the message
    requests.get(url)

#Ham gui tin nhan khan cap
def SendAlert(price_date,bot_token,chat_id,loai_tien_ao,loai_tien_te):
    if loai_tien_ao==0:
        ten_tien_ao='Bitcoin'
    else:
        ten_tien_ao='Etherum'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text=Canh bao!!!!!! gia {ten_tien_ao} vao luc {price_date[1]} la {(price_date[0])} {loai_tien_te}"

    # send the message
    requests.get(url)
#bot_token='5025869025:AAGffurHxmAosrwlpMjQ9qEEDH--z5Tpekw'
#chat_id= '5019415587'
#ds=[[10, '20:17:23'],[15,'20:30:35']]
#SendMessage(ds,bot_token,chat_id)
