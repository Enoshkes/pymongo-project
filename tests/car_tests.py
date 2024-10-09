import pytest
from pymongo.collection import Collection


@pytest.fixture(scope="function")
def cars_collection(init_test_data):
    return init_test_data['cars']


def test_find_all_cars(cars_collection):
    all_cars = list(cars_collection.find())
    assert len(all_cars) > 0


def test_indexes(cars_collection: Collection):
    cars_collection.create_index({'brand': 1})
    cars_collection.create_index({'brand': 1, 'color': 1})
    cars_collection.drop_index([('brand', 1), ('color', 1)])
    cars_collection.drop_indexes()
    info = cars_collection.index_information()
