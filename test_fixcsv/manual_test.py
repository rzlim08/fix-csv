import sys
import os

sys.path.append(os.path.abspath(sys.path[0]) + "/../")
from fix_csv.fix_csv import FixCSV


def main():
    fcsv = FixCSV(auto_fix=False)
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
    fcsv.set_possible_values(possible_values)
    fixed_column = fcsv.fix_csv_column("DKEFSFAKEDATA.csv", 9)


if __name__ == "__main__":
    main()
