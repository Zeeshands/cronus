import spacy

nlp = spacy.load("en_core_web_lg")

while(1):
 str=input('Enter text:')
 doc = nlp(str.title())
 print([(X.text, X.label_ ) for X in doc.ents] ,str)
 print('------------------------')
 print([nc.text for nc in doc.noun_chunks] ,str)

#for nc in doc.noun_chunks:
# print(nc.text)
