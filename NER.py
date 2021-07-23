
import spacy
from spacy import displacy
import en_core_web_lg
nlp = en_core_web_lg.load()
import neuralcoref
neuralcoref.add_to_pipe(nlp)

def printPronounReferences(doc):
    for token in doc:
        if token.pos_ == 'PRON' and token._.in_coref:
            result = []
            for cluster in token._.coref_clusters:
                print(token.text + " => " + cluster.main.text)
                result.append(token.text + " => " + cluster.main.text)
            return result

def extractor(sentence):
    #sentence = input('Enter sentence here : ')

    doc = nlp(sentence.title())
    print([(X.text, X.label_ , X.start , X.end ) for X in doc.ents])
    labels = [(X.text, X.label_, X.start , X.end) for X in doc.ents]
    #displacy.render(nlp(str(doc)), jupyter=True, style='ent')

    coref = printPronounReferences(doc)
    return (labels,coref )

#extractor('my name is Jacob')

l1=['my city is Ifrah','I am Known as Uzair','I am called Zubair','I work for Google','my favourite color is Green','I like to play Cricket' ]

l2=['I like to play Baseball','my favourite sports is Badminton',
'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'
]
l3=['my name is favourite food is Pizza']
l4=['I live in karachi', 'I live in New york', 'Paris is my city','london','London','Ibiza','Bombay','I was born on 01-01-1961','Lets meet on comming wednesday 29th december 1990'  ]

l='it is also great to live in london though and karachi is also great.google is my employer. my name is kashif'.title()
l='Karachi is also great. Gjkjdf is my employer. my name is Kashifnndf'
s1='European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and  and ordered the company to alter its practices'
l5=['i like to go to bahrain in summer vacation','pune is a hot place','the weather was cold in mumbai lately']
#print( str(extractor(l)),str(l) )
for l in l5:
 print(extractor(l) ,l )

#'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

#example sentence for extractin coref
#ali is going to London tomorrow and he will be back by next Friday.
#My sister has a dog and she loves him.
#My sister has a dog and she loves him. He is cute.

