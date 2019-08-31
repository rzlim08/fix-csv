import unittest
from test_fixcsv.data.getdata import get_test_data
from fix_csv.fix_csv import FixCSV


class TestCSV(unittest.TestCase):
    def test_read_csv(self):
        data_path = get_test_data()
        fc = FixCSV(csv_path=data_path)
        fc.set_possible_values(["test"])
        vals = fc.fix_csv_column(0)
        self.assertEqual("test", vals.pop())

