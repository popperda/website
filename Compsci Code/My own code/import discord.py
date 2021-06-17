import discord
import requests
import json

client = discord.Client()
data = requests.get("https://random-words-api.vercel.app/word").json()
word = (data[0]["word"]).lower()
def search(a):
    items = a
    print(items)
    datatwo = requests.get("https://www.googleapis.com/customsearch/v1?key=AIzaSyDOCVpIpvA9nDCFD4T7jU2XjdvWeVk_gAw&cx=7e0287b28799017cb&q="+ str(items) ).json()
    data = datatwo["items"][0]["link"]
    data1 = datatwo["items"][1]["link"]
    data3 = datatwo["items"][2]["link"]
    data2 =  data3.replace("%27","")
    print(data2)
    dataone = datatwo["context"]["title"]
   
    return (data,data1,data2, "DONE")

def hangman(a,b):
    
    word = b.lower()
    print(word)
    correct = 0
    mistakes = 0
    unknown = (len(word) * '_')
    listed = ["_"]*len(word)
    
    cr = ("correct:"+str(correct) )
    ms = ("incorrect:" + str(mistakes))
    print(cr)
    print(ms)
    correctmeter = 0
    print (unknown)

    print(listed)
    x = a
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
    if mistakes == len(word):
        print("FAIL")
    return(listed,cr,ms)


    
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    print(json_data)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith("bye"):
        await message.channel.send("Bye!")
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('-'):
        msg = message.content
        x = msg.replace("-"," ")
        google = search(x)
        await message.channel.send(google)
    
    if message.content.startswith('hangman'):
        data = requests.get("https://random-words-api.vercel.app/word").json()
        word = (data[0]["word"])
        for n in range (0,len(word)):
            msg = message.content
            x = msg.replace("hangman"," ")
            google = hangman(x,word)
            await message.channel.send(google)
            
       

    



client.run('ODUzOTQ2OTYxNTcyMjY1OTg0.YMcyFQ.YbC79aqzTe7OEy3r2splyXTSUUA')
