from flask import Flask,request, render_template
from typing import NewType
import requests
from requests.api import post
path = '/home/jatrhead/path/to/flask_app_directory'
#just checking name probably the user
app = Flask(__name__)
def bazaarsearch(a):
    
    item = a
    data = requests.get("https://api.hypixel.net/skyblock/bazaar?c8262998-f925-414d-8c84-a17accddec0a&productId={item}").json()
    
    try:
        print(data["products"][item]["buy_summary"][0]["pricePerUnit"])
        print(data["products"][item]["sell_summary"][0]["pricePerUnit"])
        print(data["products"][item]["buy_summary"][0]["amount"])
        a= (data["products"][item]["buy_summary"][0]["pricePerUnit"])
        b= (data["products"][item]["sell_summary"][0]["pricePerUnit"])
        c = a-b
        return c
    except KeyError:
        return "no"
        
def search(a):
    items = a
    print(items)
    datatwo = requests.get("https://www.googleapis.com/customsearch/v1?key=AIzaSyDOCVpIpvA9nDCFD4T7jU2XjdvWeVk_gAw&cx=7e0287b28799017cb&q="+ str(items) ).json()
    data = datatwo["items"][0]["link"]
    data1 = datatwo["items"][1]["link"]
    data3 = datatwo["items"][2]["link"]

    dataone = (data,data1,data3)
   
    return (dataone)
    
def bazaarcheck():
    from typing import NewType
    import requests
    # gets in json


    dataone = requests.get("https://api.hypixel.net/skyblock/bazaar?c8262998-f925-414d-8c84-a17accddec0a&page=0").json()
    # gets the auctions

    auction1 = dataone["products"]
    #with pages
    totalbazaar = []
    items = []

    i=0
    data = requests.get("https://api.hypixel.net/skyblock/bazaar?c8262998-f925-414d-8c84-a17accddec0a&productId={item}").json()
    # adds the auction that is a bin
    tempprice = 0
    tempsell = 0
    profit = []
    list1 = list[0]




    try: 
        
        for a in data["products"]:
            print(a)
            tempprice = int(data["products"][a]["buy_summary"][0]["pricePerUnit"])
            tempsell = int(data["products"][a]["sell_summary"][0]["pricePerUnit"])
            product = tempprice-tempsell
            profit.append([a,product])
        #enchanted carrot on stick broken + bazaar cookie for some reason remove them from products
        #print(profit)
    except IndexError:
        
        for a in data["products"]:
            if a != "ENCHANTED_CARROT_ON_A_STICK" :
                if a != "BAZAAR_COOKIE":
                    print(a)
                    c= (data["products"][a]["buy_summary"][0]["pricePerUnit"])
                    b= (data["products"][a]["sell_summary"][0]["pricePerUnit"])
                    pro = (c-b)
                    profit.append([a,pro])
    profit.sort(key=lambda x:x[1], reverse=True)
    print(profit)
    return profit
def auction(a):
    data = requests.get("https://api.hypixel.net/skyblock/auctions").json()
    
    dataone = requests.get("https://api.hypixel.net/skyblock/auctions").json()


    auction1 = dataone["auctions"]
    #with pages
    totalauction = []
    items = []
    item2 = []
    item = a
    i=0
    total = data["totalPages"]
    # adds the auction that is a bin
    while i != total:
        updatepage = requests.get("https://api.hypixel.net/skyblock/auctions?c8262998-f925-414d-8c84-a17accddec0a&page="+str(i)).json()
        auctions = updatepage["auctions"]
        
        totalauction += auctions
        i+=1
        for auction in auctions:
            try:
                if auction["bin"] :
                    if str(auction["item_name"]).count(item.title()) > 0:
                        items.append([auction["item_name"],auction["starting_bid"],  auction["category"], auction["auctioneer"]])
                else:
                    if str(auction["item_name"]).count(item.title()) > 0:
                        item2.append([auction["item_name"],auction["starting_bid"],  auction["category"], auction["auctioneer"]])
                    
            except KeyError:
                pass
    #  for auctionaa in auctions:
            #try:
                #if auctionaa["bin"]:
                    #if str(auctionaa["item_name"]).count(item.title()) > 0:
                        #item2.append([auctionaa["item_name"], auctionaa["starting_bid"], auctionaa["category"], auctionaa["auctioneer"]])
            #except KeyError:
                #pass
        

    Newvalue = []
    OldValue = []
    item2.sort(key=lambda x:x[1])
    # sorts by the prices, use items.sort(key=lambda x:x[1], reverse=True) for highest prices first
    items.sort(key=lambda x:x[1])

    return items
  

    
  

    


@app.route("/")
def index_page():
    
    return render_template('Homepage.html')
@app.route("/home")
def home():
    folder = ["Computer Science","Math","English","Chinese","Chemistry","Biology","Physics","Economics","History"]
    return render_template('main-original.html', personName="Jared",folder=folder)
@app.route("/login")
def login():
    return"Login Here. Pass=_____ User=____"
@app.route("/logout")
def logout():
    return"Please do not leave"
@app.route("/register")
def register():
    return"Register here"
@app.route('/Enter')
def Enter():

   return render_template('Template1.html')
@app.route('/sb')
def sb():
# gets in json

    return render_template('Template1 - Copy.html')   
@app.route('/sb', methods = ['POST'])
def sb_search():
# gets in json
   text = request.form['text']
   item1 = auction(text)
   return render_template('AuctionSearchup.html',text=text, item1 = item1)

@app.route('/meeopp')
def meeopp(): 
   return render_template('iphone12ProMax1.html')

@app.route('/bazaar')
def bazaarchecks():
    bazaarlist = bazaarcheck()
    return render_template("Bazaarcheck.html",bazaarlist=bazaarlist)
@app.route('/bazaar', methods = ['POST'])
def bazaar_search():
# gets in json
   text = request.form['text']
   item1 = bazaarsearch(text)
   return render_template('Bazaarsearch.html',text=text, item1 = item1)
@app.route('/mario')
def trte():
    return render_template('Mario Game.html')
@app.route('/quick')
def quick():
   
   return render_template('Bazaarsearch.html')
@app.route('/quick', methods = ['POST'])
def quicksearch():
   text = request.form['text']
   item1 = search(text)
   return render_template('Bazaarsearch.html',text=text, item1 = item1)
if __name__ == "__main__":
    #this allows it to run on any network, thats why there is 0.0.0.0 
    # like the web router things, port is the computers
    #the port number is lika flat number in a building
    # so essentially its saying go to a building then send this package
    #to a particular program
    app.run(host="0.0.0.0", port=80, debug=True)
#USING HTML LETS GOOOOO
# revision remember
#there are opening and ending tags
# example: <p> Hello </p> to end, we can add images etc
# a href: hyperlink
#image= <img src="picture link.jpg">
# divs <div></div>
#we can have classes for divs
# <div class = "Green"> then <p>hi</p> </div>
# Css is the painitng and stuff, HTML is structure is basically that