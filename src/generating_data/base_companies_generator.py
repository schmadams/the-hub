from src.helper_functions.helpers import load_config, join_sic_descs, load_sic_descs
from sqlite_helpers.create_db_file import CreateNewDBFile
from sqlite_helpers.sqlite_utils import SQLiteActions
import pandas as pd
import random
import numpy as np
from pathlib import Path, PurePath
import uuid
class SynthesiseData:
    def __init__(self, total_pop=10000):
        self.data = {}
        self.config = load_config()
        self.entity_options = self.config['entity_types']
        self.total_pop = total_pop
        self.db_config = self.config['db']
        self.full_path = PurePath(self.db_config['full'])
        self.actions = SQLiteActions(db_full=self.full_path)

    def run(self):
        self.sics = self.load_sics()
        self.companies = self.generate_companies(self.total_pop)
        self.create_db()
        self.clear_tables()
        self.write_tables()
        print(self.actions.list_all_tables())

    def load_sics(self):
        sics = load_sic_descs()
        sics = sics[sics['level headings'] == 'Class'].reset_index()
        sics = sics.rename(columns={'description': 'desc'})
        return sics[['desc', 'sic']]

    def generate_companies(self, total_pop):
        companies = []
        while len(companies) < total_pop:
            sic = random.choice(self.sics['sic'])
            entity = self.gen_entity_type()
            count = np.random.randint(1, 25)
            for idx in range(count):
                companies.append((uuid.uuid4().hex[:8], sic, entity))
        companies = pd.DataFrame(companies, columns=['company_name', 'sic', 'entity_type']).drop_duplicates(subset='company_name')
        companies = join_sic_descs(df=companies, key='sic')
        self.data.update({'companies': companies})

    def gen_entity_type(self, out=None):
        for et in self.entity_options:
            if np.random.randint(1, 11) > 5:
                out = et
                break
        if None in [out]:
            out = self.entity_options[-1]
        return out

    def create_db(self):
        if any(str(file).endswith(self.db_config['name'] + '.db') for file in Path(self.db_config['path']).glob('*')):
            Path(PurePath(self.config['path'], self.config['name'])).unlink()
        else:
            print('file is not there')
            CreateNewDBFile(db_full=self.full_path).create_db()

    def clear_tables(self):
        for table in self.actions.list_all_tables():
            self.actions.drop_table(table=table)
    def write_tables(self):
        for table, data in self.data.items():
            print(table)
            self.actions.create_table(table=table, data=data)



if __name__ == '__main__':
    sics = SynthesiseData().run()
    a=1
    a=1