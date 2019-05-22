from typing import List
import pandas as pd
from difflib import SequenceMatcher


class FixCSV:
    def __init__(self, delimiter: str = ",", autofix: bool = False):
        self.possible_values = []
        self.delimiter = delimiter
        self.autofix = autofix

    def set_possible_values(self, possible_values: List[str]):
        self.possible_values = possible_values

    def add_possible_value(self, possible_value: str):
        self.possible_values.append(possible_value)

    def get_possible_values(self) -> List[str]:
        return self.possible_values

    def fix_csv_column(self, csv_path: str, column: int):
        csv = pd.read_csv(csv_path, delimiter=self.delimiter, header=None)
        csv_column = list(csv.iloc[:, column])
        print("hello world")

    def validate_string(self, string_to_validate: str):
        if string_to_validate in self.possible_values:
            return string_to_validate
        else:
            ratios = [
                SequenceMatcher(None, val, string_to_validate).ratio
                for val in self.possible_values
            ]
            sorted_ratios = sorted(ratios)
            if self.autofix:
                return sorted_ratios.pop(0)
            else:
                for i in range(1, 4):
                    print("[{}]: {}".format(i, sorted_ratios[i - 1]))
                print("[4]: manual input")
                input("Top 3 most similar values: select an option")
