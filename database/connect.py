from pymongo import MongoClient

client = MongoClient('mongodb://192.168.76.216:27017')
texi_db = client['texi-drivers']

drivers = texi_db['drivers']
cars = texi_db['cars']