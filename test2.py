from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
import string
from utility import preprocess

from rasa_nlu.model import Metadata, Interpreter
#interpreter = Interpreter.load(model_directory)
interpreter = Interpreter.load('nlu/model/default/model_20210128-131936')

while(1):
 str=input('Enter input:')
 #str = str.translate(str.maketrans('', '', string.punctuation)).lower()
 str = preprocess(str)
 print(str)
 dict = interpreter.parse(str)
 print( dict['intent'],dict['entities'] )
 #print(dict)

