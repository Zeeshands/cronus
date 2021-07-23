




import spacy

nlp = spacy.load("en_core_web_lg")

str="it is also great to live in london though and karachi is also great.google is my employer. my name is kashif"
str1='european authorities fined google a record $5.1 billion on wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'
str="john is my name and I live in california I earn $75000 a year"

l1=["my name is harry","harry is my name","i live in lahore",
    'uzair is my name and I live in california I earn $75000 a year. no my name is harry',
    'i want to read the book why nation fail' ]

s1="hello this is ifrah"
s2="harry is my name"
s3="i live in maine"
s4=" no kashif is my name"
s5='sana was my name till last year but now i am known as ifrah'
s6='my name is google'
str=s6
#print(str)
#str=str.title()
#print(str1)

#for str in l1:
# doc = nlp(str.title())
# print([(X.text, X.label_ , X.start , X.end ) for X in doc.ents] ,str)

#for ent in doc.ents:
#    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    #print(ent)
#str="ahmed uzair ali asif kashif zeeshan farhan jawwad fawwad fawad batool micheal speedman"
#str='i was born on 01/01/1961 no on 01-01-1961 or or yesterday .i was born on 27th-oct-2015. ifrah was hired by infinilogics on 24-september-1994'
doc = nlp(str.title())
print([(X.text, X.label_ ) for X in doc.ents] ,str)

