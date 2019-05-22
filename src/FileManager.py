from src.lib import trpad
from typing import List
import os

DataType = List[List[int]]

class FileManager:
    def __init__(self, filename: str, rows: int, columns: int):
        self.filename = filename
        self.rows = rows
        self.columns = columns
        self.data: DataType = None

        self.data_dir = 'data'

    def create_data_dir_if_not_exist(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def create_data_file_if_not_exist(self):
        file_path = '{0}/{1}'.format(self.data_dir, self.filename)
        if not os.path.isfile(file_path):
            with open(file_path, 'w') as fp:
                print('No file named {0} exists in data folder. Creating file.'.format(self.filename))

    def read(self) -> None:
        self.create_data_dir_if_not_exist()
        self.create_data_file_if_not_exist()
        with open('data/{0}'.format(self.filename), 'r') as fp:
            data = fp.readlines()
            data = [[int(e) for e in d.strip()] for d in data]
        self.data = data

    def write(self) -> None:
        with open('data/{0}'.format(self.filename), 'w') as fp:
            for r in self.data:
                fp.write('{0}\n'.format(''.join('{0}'.format(e) for e in r)))
        print('successfully written data to file')

    def is_data_corrupt(self) -> bool:
      all_elements_1_or_0 = all(all(e == 1 or e == 0 for e in r) for r in self.data)
      all_rows_has_correct_number_of_columns = all(len(r) == self.columns for r in self.data)
      valid_number_of_rows = (len(self.data) >= self.rows) and (len(self.data) % self.rows == 0)
      return (not all_elements_1_or_0) or (not all_rows_has_correct_number_of_columns) or (not valid_number_of_rows)

    def fix_data(self) -> None:
      self.data = [trpad([(0 if e == 0 else 1) for e in r], self.columns, 0) for r in self.data]
      while ((not (len(self.data) % self.rows == 0)) or (len(self.data) < self.rows)):
        self.data.append([0] * self.columns)
