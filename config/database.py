from pymongo import MongoClient
# configure you mongo server here
client = MongoClient("mongodb+srv://Nischay999:Nischay999@cluster0.5kufo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client['yt-downloader']
users_collection = db['users']
giftcodes_collection = db['giftcodes']
subscriptions_collection = db['subscriptions']
