from src.helper_functions.helpers import load_config, join_sic_descs, load_sic_descs
from sqlite_helpers.create_db_file import CreateNewDBFile
from sqlite_helpers.sqlite_utils import SQLiteActions
from src.pipelines.load.populations import LoadPopulations
from pathlib import Path, PurePath
import pandas as pd
import random
import numpy as np

class ChangeDataPoints:
    def __init__(self):
        self.data = {}
        self.config = load_config()
        self.entity_options = self.config['entity_types']
        self.db_config = self.config['db']
        self.full_path = PurePath(self.db_config['full'])
        self.actions = SQLiteActions(db_full=self.full_path)

    def create_change_table(self):
        self.actions.create_table(table='historical_data')

    def add_change_metadata(self, row, field):
        row['impacted_field'] = str(field)
        row['verified'] = 'N'
        row['change_date'] = pd.Timestamp.now()
        return row


    def entity_type(self, num_changes=3):
        data = LoadPopulations().data
        companies = pd.DataFrame(data['companies'])
        change_rows = []
        for i in range(num_changes):
            old_row = companies.sample(n=1)
            new_row = old_row.copy()
            new_options = [x for x in self.entity_options.copy() if x != list(new_row['entity_type'])[0]]
            new_row['entity_type'] = random.choice(new_options)
            companies.loc[new_row['index']] = new_row
            change_rows.append(self.add_change_metadata(old_row, field='entity_type'))
        a=1
        a=1


if __name__ == '__main__':
    ChangeDataPoints().entity_type()
