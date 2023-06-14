import requests
import pandas as pd
import numpy as np
import time
import json

def find_geo_from_ip(ip_address, service_http ='https://app.ipgeolocation.io/ipgeo?=apikey='+'bcd172b50c204dd7876421ec9045cfe1'+'&ip='+'192.168.88.214'):
 ##  'https://geolocation-db.com/jsonp/'
 ## 'https://freegeoip.net/json/'
 ##  'https://api.freegeoip.app/json/?apikey=35f27d80-ac11-11ec-9a0c-43a31c36f34e'
 ## 'https://api.freegeoip.app/json/',apikey = 'clqaseYZzn8GhRumN5f66RXDcZ3a8wPG3DhrYaKo&ip'
    try:
        url = service_http
        response = requests.get(url)
        result = response.content.decode()
        result = json.loads(result)

        print("Geolocation taken: ")
        print(result)
        return result
    except:
        return np.nan

def take_field(field_json, field_name = 'country_name'):
    try:
        return field_json[field_name]
    except:
        return np.nan

tt = time.time()

df = pd.read_csv("2022-04-27-data_export.csv.zip")
print(df.head())
print(df.shape)
df = df.head(10).copy()

##country_code,  country_name,  city,  postal, latitude, longitude
df['geo_info' ] = df['Source IP'].apply(find_geo_from_ip)
df['Source Country Code'] = df['geo_info'].apply(lambda x: take_field(x,field_name='country_code') )
df['Source Country Name'] = df['geo_info'].apply(lambda x: take_field(x,field_name='country_name') )
df['Source City'] = df['geo_info'].apply(lambda x: take_field(x,field_name='city') )
df['Source Postal'] = df['geo_info'].apply(lambda x: take_field(x,field_name='postal') )
df['Source Latitude'] = df['geo_info'].apply(lambda x: take_field(x,field_name='latitude') )
df['Source Longitude'] = df['geo_info'].apply(lambda x: take_field(x,field_name='longitude') )
df.drop('geo_info', axis = 1, inplace = True)
print(df.head())
ttt = time.time()

print("Time taken: "+ str(ttt - tt))

df.to_csv("df_saved7.csv")

new_df = pd.read_csv("df_saved7.csv")
print(new_df.dtypes)
print(new_df)