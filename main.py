

import beepy
import requests
import pandas as pd
import threading
import time
import pymsgbox

from datetime import datetime
stop_sound_boolean=False
response_df_available_old=pd.DataFrame()
threads={}
headers = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

def play_sound(n=6):

    for i in range(0,n):
        if stop_sound_boolean==True:
            return
        beepy.beep(sound=6)

def get_play_sound_boolean(*names):
    global stop_sound_boolean
    try:
        names="\n".join(names)
        print(names)
    except:
        names="\n"
    msg_val = pymsgbox.alert('Vaccine Available!!!'+"\n"+names, 'Vaccine Available!!!',timeout=22000)  # closes after 2000 milliseconds (2 seconds)
    #print(msg_val)
    stop_sound_boolean =True if msg_val!= 'Timeout' else False
    print(stop_sound_boolean)

    return stop_sound_boolean


def find_vaccine_locations(district_id,date=datetime.now().date()):
    global response_df_available_old,stop_sound_boolean,threads
    date = date.strftime('%d-%m-%Y')
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='+str(district_id)+'&date='+date
    r = requests.get(url, headers=headers)
    response = r.json()
    try:
        response_df = pd.DataFrame(response['centers']).explode('sessions')
        response_df = pd.concat([response_df, response_df['sessions'].apply(pd.Series)], axis=1)
        print(response_df.name)
    except:
        print('No vaccination centers found in district')
        return
    try:
        response_df=response_df.explode('vaccine_fees')
        response_df = pd.concat([response_df, response_df['vaccine_fees'].apply(pd.Series)], axis=1)
        response_df = response_df.drop(columns=['sessions', 'vaccine_fees'])
    except:
        print('no paid locations')
    response_df_available = response_df.query('available_capacity > 0 and fee_type=="Paid"')
    if len(response_df_available)>0 and len(response_df_available)!=len(response_df_available_old) and not response_df_available.equals(response_df_available_old):
        stop_sound_boolean=False
    if not stop_sound_boolean:
        datetimenow=datetime.now()
        threads = threading.Thread(target=play_sound)  # we need [] to tell python it's a list
        threads.start()
        # thread_in[i] = threading.Thread(na            thread.restart()me=i,target=get_play_sound_boolean,args=response_df_available.name)
        # thread_in[i].start()thread.restart()
        #play_sound()
        get_play_sound_boolean(*response_df_available.name.tolist())
        #thread.join()
        print(stop_sound_boolean)
        if stop_sound_boolean:
            response_df_available_old=response_df_available.copy(deep=True)
            return
#%%
play_sound(1)
stop_sound_boolean=True
i = 0
district_ids = [307, 303]
date = datetime.now().date()
while True:


    for district_id in district_ids:
        find_vaccine_locations(district_id,date=date)
        print(i,datetime.now())
    time.sleep(10)

    if i%15==0:
        beepy.beep(sound=4)
        date = datetime.now().date()
    i += 1




#%%

