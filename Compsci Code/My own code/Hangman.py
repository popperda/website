import requests
import json
from typing import NewType
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
        if x == word[n] and listed[n]!= x:
            print(n)
            listed[n] = x
            correct +=1

            correctmeter +=1

    if correctmeter == 0:
            
        mistakes += 1
    if correct == len(word):
        print("DONE CONGRATS")
        break
print("FAIL")


