import requests
import json
from typing import NewType
def search(a):
    items = a
    print(items)
    datatwo = requests.get("https://www.googleapis.com/customsearch/v1?key=AIzaSyDOCVpIpvA9nDCFD4T7jU2XjdvWeVk_gAw&cx=7e0287b28799017cb&q="+ str(items) ).json()
    data = datatwo["items"][0]["link"]
    data1 = datatwo["items"][1]["link"]
    data3 = datatwo["items"][2]["link"]

    dataone = datatwo["context"]["title"]
   
    return (data,data1,data3)
message = input("hello")
quote = message
print(quote)
google = search(quote)
print(google)
data = requests.get("https://random-words-api.vercel.app/word").json()
word = (data[0]["word"]).lower()
print(word)
correct = 0
mistakes = 0
unknown = (len(word) * "_")
listed = ["_"]*len(word)
while len(word) > mistakes:
    print("correct:"+str(correct) )
    print("incorrect:" + str(mistakes))
    correctmeter = 0
    print (unknown)

    print(listed)
    x = input("guess a letter")
    print(x)
    for n in range(0,len(word)):
        if x == word[n] & listed[n]!= x:
            print(n)
            listed[n] = x
            correct +=1
            print(listed)
            correctmeter +=1

    if correctmeter == 0:
            
        mistakes += 1
    if correct == len(word):
        print("DONE CONGRATS")
        break



