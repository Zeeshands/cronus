from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter
import string
interpreter = Interpreter.load('nlu/model/default/model_20210128-131936')
#while(1):
# str=input('Enter input:')
# print( interpreter.parse(str)['intent'] )

l1=["hey",
"hello",
"helo",
"hi",
"hiya",
"good morning",
"good evening",
"good afternoon",
"hey there",
"hello there"]


l2=["what is your gender",
"are you male or female",
"what is your sex",
"are you male",
"are you female",
"are you a transgender",
"tell me your gender",
"are you masculine",
"are you feminine",
"are you male female"]


l3=["your dob",
"your date of birth",
"what's your birthday",
"when is your birthday",
"when is your birthdate",
"when were you born",
"when is your birthday party",
"can i have your date of birth please",
"what is your date of birth",
"what is your dob",
"your dob",
"may i know your dob",
"may i ask your dob",
"can you share your dob",
"tell me your birthdate",
"do you mind if i ask your birthdate",
"when were you born or created",
"do you know your date of birth",
"when were you created"]


l4=["what is your age",
"your age",
"how old did you get",
"how old are you",
"how old are you now",
"how old did you turn",
"may i ask your age",
"may i get to know you age",
"do you mind if i ask how old you are",
"tell me your age",
"please tell me your age",
"what is your current age",
"how old are you right now",
"what is your present age",
"by the way what is your age"]


l5=["your name",
"what is your name",
"can you tell me your name",
"may i ask you what your name is",
"how may i address you",
"how do they call you",
"how is one to call you",
"could i ask your name",
"i forgot your name could you please remind me",
"what should i call you",
"can i call you cronus",
"is it okay if i call you cronus",
"whats your name",
"what do your friends call you",
"how do people call you",
"what do your owner call you",
"what do others call you",
"may I know your name",
"who are you",
"tell me briefly about yourself",
"tell me about yourself",
"can you introduce yourself"]


l6=["your city",
"where are you from",
"what is your city",
"could you tell me where you are from",
"where do you stay",
"where are you from",
"where do you live",
"where do you reside",
"where do you live currently",
"where are you now",
"are you in Abu Dhabi",
"your birth place",
"where you belong from",
"may i know which city you belong to"]


l7=["your job",
"your profession",
"what is your work",
"what do you do for a living",
"what do you do",
"what is your job",
"what kind of work do you do",
"what line of work are you in",
"i would be interested to hear about what you do",
"what you do",
"what is your nature of work",
"what is your nature of job",
"what you do as a chatbot",
"what is your key responsibility on a job",
"tell me about your job",
"where are you working"]



l8=["how much study you have done",
"what is your educational background",
"tell me about your educational qualifications",
"what are your qualifications",
"what college have you been to",
"your college",
"your school",
"where did you get your degree from",
"what is your education",
"your education",
"tell me about your studies",
"what have you studied",
"what course have you studied",
"what is your major in studies",
"what is your education level",
"tell me how much education you have received",
"have you got your degree",
"do you have a degree"]



l9=["what are your hobbies",
"your hobbies",
"tell about your hobbies",
"what do you do in your spare time",
"what do you do in your leisure time",
"what things do you find most interesting",
"what are your interests",
"your interests",
"how do you make your spare time interesting",
"what activities you find yourself intrigued about the most",
"can you list your activities which you are most interested in",
"do you even have anything interesting to do other than this",
"tell one intriguing activity you would love to indulge in",
"what is your favourite hobby",
"how many things do you do in your free time",
"how many activities do you do in your free time",
"can you tell me about your hobbies",
"what is interesting for you to do to make you happy"]


l10=["what is your country",
"your country",
"which country do you belong to",
"in which country do you live",
"in what part of the world you reside",
"what nationality do you hold",
"what is your nationality",
"i am very curious about your nationality",
"may i know which state you belong to",
"are you from america",
"are you a british national",
"which country’s nationality do you have",
"are you dual national",
"may I know your nationality",
"how many nationalities do you have"]


l11=["whose music you like the most",
"what is your favourite song",
"who is your favourite musician",
"tell me about your kind of music and who do you like to listen most",
"tell me about your favourite music makers",
"who is the best among all the music producers in the world",
"what is your favourite song",
"which is your favourite song",
"your favourite music",
"your favourite musician",
"do you like music",
"what is your favourite music",
"which type of music do you like most",
"which style of music do you like to listen",
"which style of music do you want to listen",
"is there any favourite song of yours",
"who is your favourite singer"]

l12=["what is your favourite color",
"your favourite color",
"which color do you like",
"what shades in clothing you like to wear most often",
"what kind of hues you prefer to wear",
"defines yourself in a shade or hue you like the most",
"which color do you like the most",
"do you prefer specific color while selecting clothes",
"which shade of color do you like most",
"what is your favorite color"]


l13=["do you have any brother",
"how many brothers do you have",
"do you have any sister",
"how many sister do you have",
"how many siblings do you have",
"do you have any siblings",
"any brothers or sisters",
"how many brothers and sisters do you have",
"how many kinsmen do you have and what do you call them",
"what do you call your kinsman",
"how do you call out your kinsman",
"name all your male kinsfolk",
"how many kinswomen do you have and what do you call them",
"what do you call your kinswoman",
"how do you call out your kinswoman",
"name all your female kinsfolk",
"do you have elder sister brother",
"do you have younger sister brother",
"how many siblings",
"younger or older among siblings"]

l14=["who made you",
"who is your developer",
"who are your developers",
"who developed you",
"who is your owner",
"who owns you",
"who created you",
"tell me about your owner",
"who updated you",
"please introduce your owner",
"tell me about your owner",
"tell me about your developer",
"who is responsible of you",
"who takes your responsibility"]


l15=["name of your organization",
"name of your company",
"name of your firm",
"your organization",
"your company",
"your firm",
"can you tell me about your organization",
"can you tell me about your company",
"can you tell me about your firm",
"where are you working",
"which company are you working",
"which organization are you working",
"which firm are you working for",
"which company do you work for",
"which organization do you work for",
"which firm do you work for"]


l16=["are you married",
"are you single",
"do you have a husband",
"do you hava a wife",
"do you have a spouse",
"do you have a significant other",
"have you got a spouse",
"what is your marital status",
"when you have plan to get married"]


l18=["who is your favourite poet",
"your favourite poet",
"your most liked poet",
"whose poetry you like the most",
"whose poetry you like",
"whose poems are your favourite",
"do you like shakespeare poems",
"whose poetry would you prefer to read",
"whose poetry is your favourite",
"name the poet in whose poetry you are interested",
"i like poetries do you like it",
"do you like poetries"]


l20=["what is your favourite sportsman",
"who is your favourite sportsman",
"what sports person is your favourite",
"who inspires you the most in sports",
"because of whom do you like a sport",
"which sports personality do you like",
"which sports personality do you like most",
"which sports celebrity do you like most",
"do you like any sportsman",
"who do you think the most talented sportsman",
"who is your personal hero",
"your favourite sportsman"]


l21=["do you have any parents",
"do you have a mother",
"do you have a father",
"do you have a father or mother",
"what do you call your matriarch",
"can i know the name of the woman who gave birth to you",
"who is the woman birthed you",
"i am interested in knowing your mom official title",
"are your parents alive",
"to whom you are more closer in your parents",
"tell me about your family",
"what does your father do",
"is your mother a housewife",
"tell me about your family",
"do you have a family",
"how many members in your family"]

l22=["your favourite actor actress",
"your favorite celebrity",
"who is your favourite actor",
"who is your favourite actress", 
"who is your favourite male celebrity",
"who is your favourite female celebrity",
"i want to know about your favourite celebbrity",
"name one celebrity you like to watch",
"which celebrity is your all time favourite",
"do you like any celebrity",
"is there any celebrity you like to watch",
"is there any actor or actress you like to watch",
"can you tell me the name of famous actor"]


l23=["your favourite book",
"your most favourite book",
"which is your most favourite book",
"what is your most favourite book",
"which type of books do you love to read",
"what book you would like to read the most",
"name one good book read of yours",
"what book keeps you captivated",
"which book you always enjoy whenever you read",
"which book compels you to read many times",
"any book which you read many times",
"which type of books do you like to read",
"which book do you like very much",
"can you tell me about your favourite book",
"tell me about your favourite book",
"which is intresting book you find",
"any specific genre you like to read"]

l24=["bye",
"bye",
"bye bot",
"bye bye",
"bye bye bot",
"bye for now",
"bye was nice talking to you",
"catch you later",
"farewell",
"good bye",
"good night",
"goodbye",
"goodbye",
"goodnight",
"gotta go",
"ok bye",
"ok bye",
"see u later",
"see ya",
"see you",
"see you bye",
"take care",
"then bye",
"tlak to you later",
"exit",
"byr"]

l25=[
"what is my name",
"can you tell me my name",
"please tell me my name",
"tell me my name",
"what am I called",
"my name",
"whats my name",
"what do they call me",
"who I am",
"do you know my name",

"do you know what is my name",
"do you know whats my name",
"can you tell me my name",
"what is my name",
"hey do you remember my name",
"who i am",
"who am i"
]

l26=["what is my age",
"can you tell me my age",
"please tell me my age",
"tell me my age",
"how old am i",
"my age",
"whats my age",
"how old did i get"
]

l27=[
"what is my location",
"can you tell me my location",
"please tell me my location",
"tell me my location",
"my location",
"whats my location",
"where am i located",
"where do i live",
"where i live",
"what is my city",
"can you tell me my city",
"please tell me my city",
"tell me my city",
"my city",
"whats my city",
"okay tell me about my city",
"tell me about my city",
"what is the name of my city",
"do you know where I am from",

"what is the name of my city",
"do you know the name of my city",
"have you remembered where i am from",
"tell me the name of my city"

]

l28=[
"tell me my birthday",
"do you know my birthday",
"what is my dob",

"my dob",
"my date of birth",
"what's my birthday",
"when is my birthday",
"when is my birthdate",
"when was I born",
"when is my birthday party",
"can i have my date of birth please",
"what is my date of birth",
"what is my dob",
"may i know my dob",
"may i ask my dob",
"can you share my dob",
"tell me my birthdate",
"do you mind if i ask my birthdate",
"when were you born or created",
"do you know my date of birth",
"when were you created",
"tell me what is my birthdate",
"tell me my birthday",
"do you know my birthday",
"what is my dob"
]

l29=[
"please tell me my email address",
"what is my email address",
"i forgot my email address can you help me in this"
]

l30=["my name is Uzair","my name is Kashif","I am known as John","my city is karachi","I live in lahore",
"I am called John","people call me John","i was born on wednesday 20 july 2020"
]


l31=["what my star says aquarius",
"what my horoscope says pisces",
"how will be aries day today",
"how will be my day today taurus",
"what gemini says today",
"tell me horoscope of cancer",
"tell me horoscope of leo today",
"what is the horoscope of virgo",
"what does libra horoscope tell",
"may i have todays horoscope of scorpio",
"is something new in todays horoscope of sagittarius",
"how will be the day of capricorn today",
"how will be the day of libra",
"tell me about horoscope cancer",
"horoscope capricon",
"horoscope cancer",
"please tell me about todays horoscope of leo"
]

l32=["what is the weather in tokyo",
"how is weather in karachi",
"what a weather in toronto",
"tell me weather update in miami",
"weather in london",
"is it raining in australia",
"may i have know weather of paris",
"tell me weather in karachi",
"karachi weather",
"what is the temperature of dubai",
"is it raining in sydney",
"what is the weather update of today in karachi",
"climate of karachi",
"tokyo climate",
"japan atmosphere",
"atmosphere in karachi",
"climate in china",
"temprature in china",
"paris temprature",
"how is temprature in sweden",
"what is temprature in karachi",
"how is climate in karachi",
"what a climate in toronto",
"tell me climate update in miami",
"may i have know climate of paris",
"weather in lahore",
"tell me climate in karachi",
"temprature of sweden",
"karachi atmosphere",
"what is the climate of dubai",
"what is the climate update of today in karachi",
"what is the climate update of paris",
"how is atmosphere in sweden",
"what is atmosphere in karachi",
"how is atmosphere in karachi",
"what a atmosphere in toronto",
"atmosphere of paris",
"tell me atmosphere update in miami",
"may i know atmosphere of paris",
"tell me atmosphere in karachi",
"temprature of sweden",
"atmosphere of paris",
"karachi atmosphere",
"what is the atmosphere of dubai",
"what is the atmosphere update of today in karachi",
"what is the atmosphere update of paris",
"weather of karachi",
"temperature in tokyo",
"tell me the weather in tokyo",
"tell me the weather updates in mumbai",
"is there hot in dubai",
"how much temperature in dubai",
"tell me weather update of saudi arabia",
"do you know weather condition of karachi",
"weather report india",
"weather of mumbai",
"how much wind in pakistan",
"what is the weather in saudi arabia like",
"what is the weather in islamabad like",
"what is the weather in slovakia like"
]

l34=[
"what's new in libra's horoscope",
"what's new in Libra's horoscope?",
"I want to know about Taurus horoscope"]

l35=[
"what is the temperature of Saudi Arabia",
"What is the weather of Saudi Arabia",
"what is the weather update of Saudia arabia",
"Do you tell me weather of India",
"Tell me how much humidity in weather of Sri lanka"]

l36=[
"I wanted to ask you about the weather updates in karachi",
"can you tell me about the weather condition in dubai",
"weather updates of Dubia",
"tell me about the weather updates of Karachi"
]

l37=[
"can you tell me about leo horoscope",
"please horoscope of libra",
"please tell horoscope of virgo",
"i bet you can tell taurus horoscope too",
"ok i promis this is last tell horoscope of capricorn",
"do you know horoscope of cancer",
"horoscope of pisces",
"do you know horoscope of scorpio",
"tell horoscope of aries"
]

l38=[
"How old am I?",
"how old did i get",
"what is my age?",
"guess what my age is?",
"remember my age?",
"know how old I am?",
"my age"
]

ls= l1+l2+l3+l4+l5+l6+l7+l8+l9+l10+l11+l12 +l13+ l14+l15 +l16+l18+l20+l21+l22+l23+l24+l25+l26+l27 +l28+l29+l30+l31+l32
#ls = l1+l2+l3+l4+l5+l6+l7+l8+l9+l10+l11+l12+l13
#ls = l14+l15+l16+l17+l18+l19+l20


c1=c2=0
'''
for l in ls:
 l=l.translate(str.maketrans('', '', string.punctuation)).lower()
 c1+=1
 dict=interpreter.parse(l)
 if dict['intent']['confidence']<0.41:
  print(l,dict['intent'],dict['entities'],'\n')
  c2+=1
'''

for l in l38:
 c1+=1
 l=l.translate(str.maketrans('', '', string.punctuation)).lower()
 #if interpreter.parse(l)['intent']['confidence']<0.4:
 print(l,interpreter.parse(l)['intent'])
 c2+=1

print('\ntotal:'+str(c1)+', below threshold:'+str(c2)+'\npercent below threshold:'+str(round(c2*100/c1 ,2)) )
