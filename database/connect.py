from pymongo import MongoClient

client = MongoClient('mongodb://192.168.76.216:27017')
taxi_db = client['taxi-drivers']

drivers = taxi_db['drivers']
cars = taxi_db['cars']