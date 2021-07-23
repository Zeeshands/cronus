from flask import Flask,request,redirect
from flask import request,session
from flask_cors import CORS
from flask import render_template
app = Flask(__name__)
app.secret_key = "sha256"
CORS(app)
import pdb,json,string,sys
import requests,urllib.request
import time
from parlai.core.agents import create_agent
from parlai.core.worlds import create_task
from parlai.scripts.interactive import setup_args
from typing import Dict, Any
HOST_NAME = 'localhost'
PORT = 8080
SHARED: Dict[Any, Any] = {}
#last_res=''
import pdb
import datetime,random,nltk,re
from rasa_nlu.model import Metadata, Interpreter
interpreter = Interpreter.load('nlu/model/default/model_20210128-131936')
from db_connect import get_cp,get_up,get_all_user_attribute_pattern
from online_services import user_horoscope,weather_fun,user_location,get_user_horoscope,get_news,get_time
from utility import preprocess,extract_multi,extract_single,sent_format,log_chat,log,wiki,checkforWiki,remove_non_ascii

from cp import cronus_personality
@app.route('/')
def index():
    return render_template('index.html', title='Cronus')

@app.route('/index.html')
def mainpage():
    return render_template('index.html', title='Cronus')

@app.route('/cronus', methods=['GET'])
def cronus_info():
   if request.method == "GET":
     #pdb.set_trace()
     original_data = data = request.args.get('field',"inoo").strip()
     data = preprocess(data)
     if len(data.split()) == 1 and data.strip() in ['why','what','when','whom','how','which','whta','wyh','whan','then','than']:
        res = 'Did not get your query'
        return res
     res = response(data,original_data)
     return res

@app.route('/info', methods=['GET'])
def info1():
 if request.method == "GET":
  original_data = data = request.args.get('field',"inoo").strip()
  data = preprocess(data)
  if len(data.split()) == 1 and data.strip() in ['why','what','when','whom','how','which','whta','wyh','whan','then','than']:
    res = 'Did not get your query'
    return res
  res = response(data,original_data)
  return res


uap = get_all_user_attribute_pattern()
checker = {'get_horoscope':'zodiac_sign','get_weather':'city'}
back_questions={'Oops, tell me your full name':'name','Oops, tell me your date of birth again':'dob'}
cease_conv_words=('thanks','okay','ok','nice','cool')
user_attributes=('name','dob')
back_questions_1={'What is your full name?':'name','What is your date of birth?':'dob'}

def response(data,original_data):
 try:
  #pdb.set_trace()
  #session.pop(request.remote_addr,"None")
  #session.pop(request.remote_addr+'-last_res',"None")
  user_attribute = check_user_attribute_1(data)
  if(user_attribute!='none' and user_attribute!='name1'):
      log('condition 1 true')
      res = absorb_userinfo_1(data, user_attribute)
      log_chat(data,res)
      return res

  if(session.get(request.remote_addr+'-last_res',"None") in back_questions.keys()
     or session.get(request.remote_addr+'-last_res',"None") in back_questions_1.keys()):
      log('condition 2 true')
      log('last responce to user '+request.remote_addr+' = '+session.get(request.remote_addr+'-last_res',"None"))
      a = session[request.remote_addr+'-last_res']
      if a in back_questions_1:
       passvalue=back_questions_1[a]
      else:
       passvalue=back_questions[a]

      res = absorb_userinfo_1(data,passvalue)
      log('res='+res)
      log_chat(data,res)
      return res

  if any(wrd==data for wrd in cease_conv_words):
    #pdb.set_trace()
    log('condition 3 true')
    d=session.get(request.remote_addr,{})
    d.pop('age',None)
    d.pop('horoscope',None)
    if(d=={} or len(d)<len(user_attributes)):
      for k,v in back_questions_1.items():
       if v not in d.keys():
          session[request.remote_addr+'-last_res'] = res = k
          return res
       else:
          continue

  if user_attribute=='name1' and extract_single(data,'name')!="" : # extracting user name for 'i am','this is' variant
     log('condition 4 true')
     res = absorb_userinfo_1(data, 'name')
     log('res='+res)
     log_chat(data,res)
  else:
    dict = interpreter.parse(data)
    if(dict['intent']['confidence']>=0.40) and len(data.split()) >= 2:
     #print('>>>>>>>>>>>>>>',data,dict['intent']['confidence']>=0.40)
     party = str(dict['intent']['name']).split('_')[0]
     if party=="user":
       res = user_personality(dict['intent']['name'])
       #res = '[user personality] '+res
     elif party=="cronus":
       #tup1 = cronus_personality[dict['intent']['name']]
       tup1 = get_cp(str(dict['intent']['name']).split('_')[1])  #to be load in memory once at startup
       res = tup1[random.randint(0,len(tup1)-1)]
       #res = '[cronus personality] '+res
     else:
       #pdb.set_trace()
       res = call_online_service(dict)
       #res = remove_non_ascii(res)
       #res = '[online service] '+res
     log_chat(data,res+'\n'+ str(dict['intent']))
     #log_chat(data,res)
    else:
         #pdb.set_trace()
         #t1 = time.time()
         #str_gpt3 = gpt3_responce(data)
         #elapsed_time1 = time.time()-t1
         #str_gpt3 = str_gpt3 +' ('+str(round(elapsed_time1,1))+' sec)' 
         #pdb.set_trace()
         url_java = "http://ai.cronusbot.com/cronus/webresources/aiquestion/query?question="+data.replace(' ','%20')
         t1 = time.time()
         response_java = urllib.request.urlopen(url_java)
         response_java = remove_non_ascii(response_java.read())
         json_java = json.loads(response_java)
         java_res = json_java['comment']
         elapsed_time1 = time.time()-t1
         if java_res=="Unable to reply" or java_res=="M2" or java_res=="" or java_res is None:
           if checkforWiki(data,original_data):
             res = wiki(data)
             if res=='':
               t2 = time.time()
               m2_res = M2(data)
               elapsed_time2 = time.time()-t2
               res = m2_res #+' ('+str(round(elapsed_time2,1))+' sec)'
           else:
             res=M2(data)
         else:
           res = java_res
           M2(data) #calling M2 so that it retains context of last response
           #res='[Java]->'+java_res+'<hr>'+'[M2]->'+m2_res+' ('+str(round(elapsed_time2,1))+' sec)'


         ''' 
         pdb.set_trace()
         from concurrent.futures import ThreadPoolExecutor,as_completed
         executor = ThreadPoolExecutor(max_workers=2)
         a = executor.submit(java_calling)
         b = executor.submit(m2_calling)

         a_com = as_completed(a)
         b_com = as_completed(b)
         #if a[1]=="Unable to reply" or a[1]=="M2" or a[1]=="" or len(a[1])==0 or a[1] is None:
         #  res = b
         #else:
         #  res = a
         res = a_com.result()
         '''
         ''' 
         import concurrent.futures
         Y = []
         l_tasks = []
         with concurrent.futures.ThreadPoolExecutor() as executor:
            l_tasks.append(executor.submit(java_calling(data)))
            l_tasks.append(executor.submit(m2_calling(data)))
            for task in concurrent.futures.as_completed(l_tasks):
             Y.append(task.result())
         '''
         #if Y[0][1]=="Unable to reply" or Y[0][1]=="M2" or Y[0][1]=="" or len(Y[0][1])==0 or Y[0][1] is None:
         # res = Y[1]
         #else:
         # res = Y[0]
         
         log_chat(data,res)

 except Exception as e:
   res='exception in responce():'+repr(e)
   #res='Cannot answer this at the moment'
   log(res)
 finally:
  log('-------------------------------------------')
  return res

def java_calling(data):
         url_java = "http://ai.cronusbot.com/cronus/webresources/aiquestion/query?question="+data.replace(' ','%20')
         t = time.time()
         response_java = urllib.request.urlopen(url_java)
         response_java = remove_non_ascii(response_java.read())
         json_java = json.loads(response_java)
         res = json_java['comment'].strip()
         elapsed_time = time.time()-t
         #t=('Java',res,elapsed_time)
         return res

def m2_calling(data):
         t = time.time()
         m2_res = M2(data)
         res = m2_res
         elapsed_time = time.time()-t
         #t=('M2',res,elapsed_time)
         return res

def M2(data):
   model_response = _interactive_running(data)
   json_str = json.dumps(model_response)
   y = json.loads(json_str)
   res = sent_format(y['text'])
   if "my name is" in res.lower():
     res = (res.lower().split('my name is')[0]).capitalize()+'my name is Cronus'
   res = res.split('.')[0]
   return res

lst=[]
gpt3_last_responce=''

import openai

#def gpt3_responce1(data):
#  p = data+'.\nAI:'
#  gpt3res = gpt3_chat(p)
#  return gpt3res

#def gpt3_store1(prompt):
# if len(lst)==1:
#   lst.pop(0)
# lst.append(prompt)
# return "".join(lst)

def gpt3_responce(data):
  global gpt3_last_responce
  if len(lst)==0:
   p = ''
  else:
   p = gpt3_last_responce

  p = p + '\nHuman:'+data+'.\nAI:'
  gpt3res = gpt3_last_responce = gpt3_chat(p)
  return gpt3res

def gpt3_store(prompt):
 if len(lst)==3:
   lst.pop(0)
 lst.append(prompt)
 return "".join(lst)

def gpt3_chat(prompt):
    openai.api_key = "sk-HrGKrdflw0Ck6r2SwxWdMfBmCrzWMlXLY34a7NG3"
    engines="davinci"
    max_tokens=150
    temperature=0.75
    presence_penalty=0.6
    top_p=1
    prompt=gpt3_store(prompt)
    log(prompt)

    response = openai.Completion.create(
        engine=engines,
        prompt = prompt,
        temperature = temperature,
        max_tokens = max_tokens,
        top_p = top_p,
        presence_penalty = presence_penalty,
        stop = ["\n", " Human:", " AI:"]
    )

    #return 'responce from AI\n'
    return response['choices'][0]['text']

def call_online_service(dict):
  try:
   service = dict['intent']['name']
   if service=='get_horoscope':
    val = dict['entities'][0]['value']
    res = user_horoscope(val)
   elif service == 'get_location':
    res = user_location(request.remote_addr)
   elif service =='get_news':
    res = get_news(dict['text'])
   elif service == 'get_time':
     if dict['entities']:
       val = dict['entities'][0]['value']
       res = get_time(val)
     elif 'time' in dict['text'] or 'date' in dict['text'] or 'day' in dict['text']:
       res = get_time(user_location(request.remote_addr).replace('Your location is ',''))

   elif service == 'get_weather':
    for l in ['weather','atmosphere','climate','raining','hot','cold','temperature','sunny']:
     if re.search(l,dict['text']):
      #if 'abu dhabi' in dict['text']:
      #  res = weather_fun('abu dhabi')
      #  break
      if dict['entities']:
       val =  dict['entities'][0]['value']
       res = weather_fun(val)
       break
      else:
       res = weather_fun(user_location(request.remote_addr).replace('Your location is ','').split()[0])
       break
    else:
     res = 'Did not get your query'
  except Exception as e:
    res = 'exception in call_online_service:'+repr(e)
    #res='Cannot answer this at the moment'
    log(res)
  return res

def absorb_userinfo_1(data,user_attribute):
 try:
    #pdb.set_trace()
    log('1 in absorb_userinfo_1 sent to user '+request.remote_addr+' = '+session.get(request.remote_addr+'-last_res',"None"))
  #session.pop(request.remote_addr+'-last_res',None)
  #log('2 in absorb_userinfo_1 sent to user '+request.remote_addr+' = '+session.get(request.remote_addr+'-last_res',"None"))
  #values = extract_multi(data)
  #log('len(values)='+str(len(values)))
  #if len(values)>1:
  #  res = extract_multiple_user_attribute(values)
  #else:
    value = extract_single(data,user_attribute)
    log('absorb_userinfo_1 ' +value)
    if value != "":
      mod=sys.modules[__name__]
      setattr(mod, user_attribute, value)
      log('\nabsorb_userinfo_1-> '+user_attribute+' '+value)
      if session.get(request.remote_addr,"None")=="None":
          d={user_attribute : value}
          if user_attribute=='dob': #if user telling dob adjust his age,horoscope
            if re.findall(r'\d{4}',value)==[]:
              value=value+' 1980'
            d['age'] = int(datetime.datetime.now().year) - int(re.findall(r'\d{4}',value)[0])
            d['horoscope'] = get_user_horoscope(value)
          session[request.remote_addr]=d
      else:
          d=session[request.remote_addr]
          d[user_attribute]=value
          if user_attribute=='dob':
            if re.findall(r'\d{4}',value)==[]:
              value=value+' 1980'
            session[request.remote_addr]['age'] = int(datetime.datetime.now().year) - int(re.findall(r'\d{4}',value)[0])
            session[request.remote_addr]['horoscope'] = get_user_horoscope(value)
          session[request.remote_addr]=d

    #session[request.remote_addr][user_attribute]=value
    #if user_attribute=='dob':
    # session[request.remote_addr]['age'] = int(datetime.datetime.now().year) - int(re.findall(r'\d{4}',value)[0])
      log('final->'+str(session[request.remote_addr]))
      res="Okay"
      session.pop(request.remote_addr+'-last_res',None)
    else: #if could'nt catch the a user attrubite value on first attempt then fire back question
      log ('in else of absorb_userinfo_1')
      res = [k for k,v in back_questions.items() if v == user_attribute][0]
      log('here _1 '+session.get(request.remote_addr+'-last_res',"None"))
      if session.get(request.remote_addr+'-last_res',"None")=="None":
        session[request.remote_addr+'-last_res']=res
      else:
        session.pop(request.remote_addr+'-last_res',None)
      log ('here _2 '+session.get(request.remote_addr+'-last_res',"None"))
 except Exception as e:
  res='Exception in absorb_userinfo_1 '+repr(e)
  #res='Cannot answer this at the moment'
 finally:
  log('finally from absorb_userinfo_1 res = '+res)
  #log('from absorb_userinfo_1 session var is = '+session.get(request.remote_addr+'-last_res',"Nothing"))
  return res

def check_user_attribute_1(data):
 try:
  res='none'
  for i in range(len(uap)):
   #log('uap[i][0]='+uap[i][0])
   if uap[i][0] in data:
    res = uap[i][1]
    break
 except Exception as e:
  res = 'exception in check_user_attribute_1 '+repr(e)
  #res='Cannot answer this at the moment'
 finally:
  #log('check_user_attribute_1:'+res)
  return res

def check_user_attribute_2(data):
 try:
  res='none'
  data_tokenized = nltk.word_tokenize(data)
  for i in range(len(uap)):
   log('1 is '+str(nltk.word_tokenize(uap[i][0])))
   log('2 is '+str(data_tokenized))
   if all(elem in data_tokenized for elem in nltk.word_tokenize(uap[i][0])) is True:
    res = uap[i][1]
    break
 except Exception as e:
  res = 'exception in check_user_attribute_1 '+repr(e)
  # res='Cannot answer this at the moment'
 finally:
  return res

def extract_multiple_user_attribute(values):
 try:
   dmapping={'PERSON':'name','DATE':'dob','CARDINAL':'dob','GPE':'fav-place'}
   d={}
   for i,j in values:
     d[dmapping[j]] = i
     if j=='DATE':
       d['age'] = int(datetime.datetime.now().year) - int(re.findall(r'\d{4}', i )[0])
       d['horoscope'] = get_user_horoscope(i)

   u=session.get(request.remote_addr,{})
   u.update(d)
   session[request.remote_addr]=u

   log('final->'+str(session[request.remote_addr]))
   res="Okay"
   #if session.get(request.remote_addr,"None")=="None":
   #       session[request.remote_addr]=d
   #else:
   #       u=session[request.remote_addr]
   #       u.update(d)
   #       session[request.remote_addr]=u

 except Exception as e:
   res='exception in extract_multiple_user_attribute:'+repr(e)
   #res='Cannot answer this at the moment'
 finally:
  return res

def user_personality(intent):
 try:
    log('in user_personality with intent='+intent)
    if session.get(request.remote_addr,"None")=="None":
     res = 'I don\'t have any information of yours'
     return res

    #print(type(session[request.remote_addr]))
    user_attribute = intent.split('_')[1]
    if user_attribute in dict(session[request.remote_addr]):
      res = 'Your '+user_attribute+' is '+str(session[request.remote_addr][user_attribute])
    else:
      res = 'I don\'t know it yet'

 except Exception as e:
    res = 'exception in user_personality: '+repr(e)+'\n'
    #res='Cannot answer this at the moment'
    log(res)
 finally:
    return res

def _interactive_running( reply_text):
        reply = {'episode_done': False, 'text': reply_text}
        SHARED['agent'].observe(reply)
        model_res = SHARED['agent'].act()
        return model_res

def setup_interactive(shared):
    """
    Build and parse CLI opts.
    """
    parser = setup_args()
    parser.add_argument('--port', type=int, default=PORT, help='Port to listen on.')
    parser.add_argument(
        '--host',
        default=HOST_NAME,
        type=str,
        help='Host from which allow requests, use 0.0.0.0 to allow all IPs',
    )

    SHARED['opt'] = parser.parse_args(print_args=False)
    SHARED['opt']['task'] = 'parlai.agents.local_human.local_human:LocalHumanAgent'

    # Create model and assign it to the specified task
    agent = create_agent(SHARED.get('opt'), requireModelExists=True)
    SHARED['agent'] = agent
    SHARED['world'] = create_task(SHARED.get('opt'), SHARED['agent'])

    # show args after loading model
    parser.opt = agent.opt
    parser.print_args()
    return agent.opt


if __name__ == '__main__':
    opt = setup_interactive(SHARED)
    app.run(host='0.0.0.0',port=9000)
