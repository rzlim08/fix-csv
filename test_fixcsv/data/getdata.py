import os

FILEPATH = os.path.dirname(os.path.abspath(__file__))


def get_test_data():
    return os.path.join(FILEPATH, "testdata.csv")
