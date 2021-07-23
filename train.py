from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

train_data = load_data('nlu/data2_path.md')
trainer = Trainer(config.load("nlu/config_spacy.yaml"))
#trainer = Trainer(config.load("nlu/conf1.yaml")) 
trainer.train(train_data)
model_directory = trainer.persist('nlu/model/')

from rasa_nlu.model import Metadata, Interpreter
interpreter = Interpreter.load(model_directory)
#interpreter = Interpreter.load('nlu/model/default/model_20200625-130235')

print(str(model_directory))
ret = interpreter.parse(u"what is your age")
print(ret['text'],ret['intent'])

