from typing import NewType
import requests
# gets in json


dataone = requests.get("https://api.hypixel.net/skyblock/bazaar?c8262998-f925-414d-8c84-a17accddec0a&page=0").json()
# gets the auctions
datatwo = requests.get("https://www.googleapis.com/customsearch/v1?key=AIzaSyDOCVpIpvA9nDCFD4T7jU2XjdvWeVk_gAw&cx=017576662512468239146:omuauf_lfve&q=lectures")
auction1 = dataone["products"]
#with pages
totalbazaar = []
items = []
item2 = []
item = input("hi")
i=0
data = requests.get("https://api.hypixel.net/skyblock/bazaar?c8262998-f925-414d-8c84-a17accddec0a&productId={item}").json()
# adds the auction that is a bin
tempprice = 0
tempsell = 0
profit = []
list = (data["products"][item]["buy_summary"])
list1 = list[0]

print(data["products"][item]["buy_summary"][0]["pricePerUnit"])
print(data["products"][item]["sell_summary"][0]["pricePerUnit"])
print(data["products"][item]["buy_summary"][0]["amount"])
a= (data["products"][item]["buy_summary"][0]["pricePerUnit"])
b= (data["products"][item]["sell_summary"][0]["pricePerUnit"])
print(a-b)
products =[data["products"]]



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
updatepage = requests.get("https://api.hypixel.net/skyblock/bazaar?c8262998-f925-414d-8c84-a17accddec0a&page="+str(i)).json()
bazaar = data["products"]


 
#if str(data["products"]).count(item.upper()) > 0:
    #items.append([ data["products"][item]["quick_status"]["buyOrders"],  data["products"][item]["quick_status"]["buyOrders"]["buyPrice"]])


print(items)

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
for b in item2:
    print(b)
    OldValue.append(b[1])
print(OldValue)


for a in items:
    print(a)
    Newvalue.append(a[1])
print(Newvalue)
