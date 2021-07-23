import re,string,nltk,requests,datetime,dateparser,wikipedia
from flask import request
from unidecode import unidecode

def preprocess(data):
  data = remove_non_ascii_2(data)
  data = re.sub("['][s]", '', data) #remove apostrophy 's
  data = data.translate(str.maketrans('', '', '''!"#$%&',.:;<=>?@[\]^_`{|}~\n''')).lower()  #removed /-+* from string.pun$ 
  #data = data.replace('cronus','').replace('do you know','').replace('can you','').replace('could you','').replace('please','').replace('tell me','').replace('kindly','').strip()
  data = data.replace('cronus','').replace('can you','').replace('can i','').replace('could you','').replace('my god','').replace('i am asking','').replace('tell me about','').replace('may i know','').replace('i see','').replace('oh','').replace('+',' plus ').strip()
  if len(data.split()) > 2:
   data = data.replace('please','').replace('kindly','').replace('great','').replace('well','')
  data = re.sub('\s+',' ',data)
  return data

import spacy
nlp = spacy.load("en_core_web_lg")

def remove_non_ascii(text):
    return unidecode(str(text, encoding = "utf-8"))
    #return re.sub(r'[^\x00-\x7F]+','', text)

def remove_non_ascii_2(text):
   return ''.join([i if ord(i) < 128 else '' for i in text])

def extract_multi(sentence):
    doc=nlp(sentence.title())
    lables=[(X.text, X.label_ ) for X in doc.ents if X.label_ in ("PERSON","DATE","CARDINAL","GPE")]
    return lables

def extract_single(sentence,user_attribute):
    doc=nlp(sentence.title())
    lables=[(X.text, X.label_ ) for X in doc.ents]
    #d={'name':'PERSON','dob':'DATE'}
    ret_val=""
    for i in range(len(lables)):
      lbl=lables[i][1]
      if lbl=="PERSON" and user_attribute=="name":
        ret_val=lables[i][0]
      elif (lbl=="DATE" or lbl=="CARDINAL") and (user_attribute=="dob"):
        ret_val=lables[i][0]
      elif (lbl=="GPE") and (user_attribute=="fav-place"):
        ret_val=lables[i][0]

    return ret_val

def wiki(data):
  text_tokens=nltk.word_tokenize(data)
  tokens_without_sw=[word for word in text_tokens if not word in nlp.Defaults.stop_words]
  data=(' ').join(tokens_without_sw)
  try:
    res = wikipedia.summary(data,sentences=3)
    res = remove_non_ascii_2(res)
    log('user query:'+data)
    log('wiki answer:'+res)
  except Exception as e:
    log('Exception in wiki: '+repr(e))
    res=''
  return res

def checkforWiki(data,original_data):
  ret=False
  if any(word in ' '.join(data.split(' ')[0:3]) for word in ['what','where','when','who','which','how']):
    ret=True
  if 'tell me about' in original_data.lower():
    ret=True
  if 'i want to know about' in original_data.lower():
    ret=True

  return ret

def sent_format(sent):
    sent= nltk.tokenize.sent_tokenize(sent)
    x=' '.join(list(map(lambda x: x.strip().capitalize(), sent)))
    x=re.sub('\s+',' ', x)
    x=re.sub("[\s]+[!]", "!",x)
    x=re.sub("[\s]+[?]", "?",x)
    x=re.sub("[\s]+[.]", ".",x)
    x=re.sub("[\s]+[,]", ",",x)
    x=re.sub("[\s]+[']+[\s]", "'",x)
    x=re.sub("[\s]+[']", "'",x)
    x=re.sub("[']+[\s]", "'",x)
    return x

def log_chat(data,res):
    f = open(request.remote_addr+'.txt','a')
    f.write('\n'+ str(datetime.datetime.now())[0:19])
    f.write('\nuser->'+data+'\ncronus->'+res+'\n')
    f.close()

def log(msg):
    f = open('log.txt','a')
    #f.write('\n'+ str(datetime.datetime.now()))
    f.write(str(msg)+'\n')
    f.close()

def zodiac_sign(day, month):
   # checks month and date within the valid range
   # of a specified zodiac
    #print(day,month)
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == 11:
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
    return astro_sign


def star_from_dob(dob):
    res = dateparser.parse(dob)
    day = res.day
    month = res.month
    res  = zodiac_sign(day, month)
    return res

