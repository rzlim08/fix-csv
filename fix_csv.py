from typing import List
import pandas as pd
from difflib import SequenceMatcher


class FixCSV:
    def __init__(
        self, delimiter: str = ",", autofix: bool = False, quiet: bool = False
    ):
        self.possible_values = []
        self.delimiter = delimiter
        self.autofix = autofix
        self.quiet = quiet

    def set_possible_values(self, possible_values: List[str]):
        self.possible_values = possible_values

    def add_possible_value(self, possible_value: str):
        self.possible_values.append(possible_value)

    def get_possible_values(self) -> List[str]:
        return self.possible_values

    def fix_csv_column(self, csv_path: str, column: int) -> List[str]:
        csv = pd.read_csv(csv_path, delimiter=self.delimiter, header=None)
        csv_column = list(csv.iloc[:, column])
        fixed_column = [self.validate_string(val) for val in csv_column]
        return fixed_column

    def validate_string(self, string_to_validate: str):
        if string_to_validate in self.possible_values:
            return string_to_validate
        else:
            fixed_val = self.edit_string(string_to_validate)
        return fixed_val

    def edit_string(self, string_to_validate):
        ratios = [
            SequenceMatcher(None, val, string_to_validate).ratio()
            for val in self.possible_values
        ]
        if self.autofix:
            fixed_val = self.autofix_string(ratios, string_to_validate)
        else:
            fixed_val = self.manual_fix_string(ratios, string_to_validate)
        return fixed_val

    def manual_fix_string(self, ratios, string_to_validate: str):
        # via https://stackoverflow.com/questions/13070461/get-index-of-the-top-n-values-of-a-list-in-python
        sorted_ratios = sorted(
            range(len(ratios)), key=lambda i: ratios[i], reverse=True
        )
        print(string_to_validate)
        for i in range(1, 4):
            print(
                "[{}]: {} - {}".format(
                    i,
                    self.possible_values[sorted_ratios[i - 1]],
                    ratios[sorted_ratios[i - 1]],
                )
            )
        print("[4]: manual input")
        print("[5]: do not modify")
        valid_input = False
        while not valid_input:
            val = input("Top 3 most similar values: select an option: ")
            try:
                selection = int(val)
                if selection >= 1 and selection <= 5:
                    valid_input = True
                    if selection == 5:
                        selected_value = string_to_validate
                    elif selection == 4:
                        selected_value = input(
                            "Write the input you want to replace the string with: "
                        )
                    else:
                        selected_value = self.possible_values[
                            sorted_ratios[selection - 1]
                        ]
                    print("You have selected: ", selected_value)

                else:
                    print("You have entered a number that is not an option")
            except:
                print("You have entered an invalid response")

        return selected_value

    def autofix_string(self, ratios, string_to_validate):
        max_ind = [ind for ind, val in enumerate(ratios) if val == max(ratios)]
        if len(max_ind) > 1:
            print("Warning: more than one values with max value")
        fixed_val = self.possible_values[max_ind.pop()]
        if not self.quiet:
            print(string_to_validate, "->", fixed_val)
        return fixed_val
