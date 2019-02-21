import pandas as pd


class data_test:

    def __init__(self, path_of_data=''):
        self.path = path_of_data
        self.data = pd.read_csv(self.path)