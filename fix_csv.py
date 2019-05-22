from typing import List
import pandas as pd


class FixCSV:
    def __init__(self, possible_values: List[str] = [], delimiter: str = ","):
        self.possible_values = possible_values
        self.delimiter = delimiter

    def set_possible_values(self, possible_values: List[str]):
        self.possible_values = possible_values

    def add_possible_value(self, possible_value: str):
        self.possible_values.append(possible_value)

    def get_possible_values(self):
        return self.possible_values

    def fix_csv_column(self, csv_path: str, column: int):
        csv = pd.read_csv(csv_path, delimiter=csv_path)
        csv_column = csv.iloc[:, column]
