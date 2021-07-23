import requests
import pdb
from timezonefinder import TimezoneFinder
import datetime
import pytz
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
session = HTMLSession()
from geopy.geocoders import Nominatim
from unidecode import unidecode

geolocator = Nominatim(user_agent='myapplication')
tf = TimezoneFinder()

def user_horoscope(sign):
    try:
        url = "http://ohmanda.com/api/horoscope/"+str(sign).lower()
        response = requests.get(url)
        future = sign.capitalize()+ " -> "+response.json()['horoscope']
        return future
    except:
        return 'horoscope service is unable to respond at this time'

def KelvintoC(para):
  #return ((str(round(float(para)- 273.15,2)))+'°C')
   return ((str(round(float(para)- 273.15,2)))+'C')

def weather_fun(par):
    try:
        d={'uk':'England','uae':'United Arab Emirates','usa':'United States','us':'United States'}
        if par in d.keys():
           par=d[par]
        response = requests.get(f"https://community-open-weather-map.p.rapidapi.com/forecast?q={par}",
                                headers={"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com","X-RapidAPI-Key": "e39a34ebb4msh122e4a0d1c05fcep1f0251jsn46a232b766f4"})
        res=response.json()
        res['list'][0]['main']['temp_max']=KelvintoC(res['list'][0]['main']['temp_max'])
        res['list'][0]['main']['temp'] = KelvintoC(res['list'][0]['main']['temp'])
        res['list'][0]['main']['feels_like'] =KelvintoC(res['list'][0]['main']['feels_like'])
        res['list'][0]['main']['temp_min'] = KelvintoC(res['list'][0]['main']['temp_min'])
        st = "Weather conditions in "+par.capitalize()+" is as follows  "+'\n Temperature : '+str(res['list'][0]['main']['temp'])+'\n Feels Like : '+str(res['list'][0]['main']['feels_like'])+'\n Minimum Temperature : '+str(res['list'][0]['main']['temp_min'])+'\n Maximum Temperature : '+str(res['list'][0]['main']['temp_max'])+'\n Pressure : '+str(res['list'][0]['main']['pressure'])+'\n Sea Level : '+str(res['list'][0]['main']['sea_level'])+'\n Ground Level : '+str(res['list'][0]['main']['grnd_level'])+'\n Humidity : '+str(res['list'][0]['main']['humidity'])+'%'
        return st
    except Exception as e :
        print(e)
        return("weather service is unable to respond at this time")

def user_location(ip):
    try:
        url = 'http://ip-api.com/json/'+str(ip)
        res= requests.get(url).json()
        return 'Your location is '+res['city']+' '+res['country']
    except:
        return "Location telling service is unable to respond at this time"

from utility import star_from_dob
def get_user_horoscope(dob):
    try:
       sign = star_from_dob(dob)
       future = user_horoscope(sign)
       return future
    except:
       return 'horoscope service is unable to respond at this time'


def get_time(q):
    try:
        if 'uae' in q:
          q=q.replace('uae','United Arab Emirates')
        location = geolocator.geocode(q)
        position =location[1]
        latitude, longitude =position
        my_date = datetime.datetime.now(pytz.timezone(tf.timezone_at(lng=longitude, lat=latitude)))
        res = 'Day & time in '+q.title()+' is '+my_date.strftime("%A,%d %B, ")+str(my_date.time()).split('.')[0]
        return res
    except:
        return f'Unable to find time of {q}'

def get_news(q):
    try:
        url = "https://newscatcher.p.rapidapi.com/v1/search"
        querystring = {"media":"True","sort_by":"relevancy","lang":"en","page":"1","q":q}
        headers = {
                  'x-rapidapi-host': "newscatcher.p.rapidapi.com",
                  'x-rapidapi-key': "32a704f13dmsh559e298171601d4p1a336fjsne42c33bf65b6"
                  }
        response = requests.request("GET", url, headers=headers, params=querystring)
        res = ''
        for i in response.json()['articles']:
            res = res+'<b>'+i['title']+'</b>'+'<br>'+i['published_date'].split()[0]+'<br>'+i['summary'].split('. Updated Update')[0]+'<br><br><br>'
        return res
    except:
        return 'No news was found'


def get_info(q):
    try:
        q=q.replace(' ','+')
        r = session.get(f'https://www.google.com/search?q={q}')
        if r.status_code == 200:
            soup= bs(r.text,'lxml')
            try:
                res = soup.find('div',class_='Z0LcW XcVN5d').text
                return res
            except:
                res = soup.find('div',class_='LGOjhe').text
                return res
        else :
            return 'Sorry i do not know the answer'
    except Exception as e:
        print(repr(e))
        return 'Sorry i do not know the answer'

def remove_non_ascii(text):
    return unidecode(str(text, encoding = "utf-8"))
