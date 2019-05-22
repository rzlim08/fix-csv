import unittest
import sys, os

sys.path.append(os.path.abspath(sys.path[0]) + "/../")
from fix_csv import FixCSV


class TestFixCSV(unittest.TestCase):
    def setUp(self):
        self.fcsv = FixCSV()

    def test_add_possible_value(self):
        self.fcsv.add_possible_value("possible")
        self.assertEqual(len(self.fcsv.get_possible_values()), 1)
        self.fcsv.add_possible_value("values")
        self.assertEqual(len(self.fcsv.get_possible_values()), 2)

    def test_add_possible_list(self):
        self.fcsv.set_possible_values(["possible", "values"])
        self.assertEqual(len(self.fcsv.get_possible_values()), 2)

    def test_dkefs_fake_data(self):
        possible_values = [
            "ACGA",
            "ACGA_FU2",
            "ACGVA",
            "ACTA_FU2",
            "ACVA",
            "AGA_FU2",
            "AGCA_FU2",
            "CCGV3",
            "CCGVA",
            "CCV3",
            "CTGV3",
        ]
        self.fcsv.set_possible_values(possible_values)
        self.fcsv.fix_csv_column("DKEFSFAKEDATA.csv", 9)


if __name__ == "__main__":
    unittest.main()
