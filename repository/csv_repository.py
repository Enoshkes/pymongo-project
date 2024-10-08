import csv

from database.connect import texi_db, drivers, cars


def read_csv(csv_path):
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row


def init_texi_drivers():
    drivers.drop()
    cars.drop()

    for row in read_csv('../data/practice_data.csv'):
        car = {
            'license_id': row['CarLicense'],
            'brand': row['CarBrand'],
            'color': row['CarColor']
        }

        car_id = cars.insert_one(car).inserted_id

        address = {
            'city': row['City'],
            'street': row['Street'],
            'state': row['State']
        }

        driver = {
            'passport': row['PassportNumber'],
            'first_name': row['FullName'].split(' ')[0],
            'last_name': row['FullName'].split(' ')[1],
            'car_id': car_id,
            'address': address
        }

        drivers.insert_one(driver)

init_texi_drivers()

res = list(drivers.aggregate([
  { '$lookup': { 'from': 'cars', 'localField': 'car_id', 'foreignField': '_id', 'as': 'car' } },
  { '$match': { 'car.brand': { '$ne': 'Honda' } } }
]))
print(res)