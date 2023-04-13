from sqlite_helpers.sqlite_utils import SQLiteActions
from src.helper_functions.helpers import load_config, load_sic_descs
from logging_functions.class_logging import Logger


class LoadPopulations:
    logger = Logger("PopulationsMetaData").logger
    def __init__(self):
        self.config = load_config()
        self.db = self.config['db']['full']
        self.actions = SQLiteActions(self.db)
        self.sic_desc = load_sic_descs()
        self.data = {}
        self.extract_data()
        self.dfs_to_records_dict()
    def extract_data(self):
        self.logger.info('loading companies data and aggregated granularities')
        self.data.update({'companies': self.actions.load_table_data(table_name='companies')})
        self.data.update({'section_pops': self.section_granularity()})
        self.data.update({'division_pops': self.division_granularity()})
        self.data.update({'group_pops': self.group_granularity()})
        self.data.update({'sic_pops': self.sic_granularity()})

    def section_granularity(self):
        self.logger.info(f'aggregating for section granularity')
        df = self.data['companies'].groupby(['section']).size().reset_index(name='count')
        desc_gran = self.sic_desc[self.sic_desc['level headings'] == 'SECTION']
        desc_gran = desc_gran[['description', 'section']].rename(columns={'description': f'section_description'})
        df['section'] = self.format_string_key(df['section'])
        desc_gran['section'] = self.format_string_key(desc_gran['section'])
        df = df.merge(desc_gran, how='left', on='section').dropna()
        df['%_of_total'] = round((df['count'] / df['count'].sum()) * 100, 2)
        df = df[['section_description', 'section', 'count', '%_of_total']]
        return df

    def division_granularity(self):
        self.logger.info(f'aggregating for division granularity')
        df = self.data['companies'].groupby(['division']).size().reset_index(name='count')
        desc_gran = self.sic_desc[self.sic_desc['level headings'] == 'Division']
        desc_gran = desc_gran[['description', 'division']].rename(columns={'description': f'division_description'})
        df['division'] = self.format_string_key(df['division'])
        desc_gran['division'] = self.format_string_key(desc_gran['division'])
        df = df.merge(desc_gran, how='left', on='division').dropna()
        df['%_of_total'] = round((df['count'] / df['count'].sum()) * 100, 2)
        df = df[['division_description', 'division', 'count', '%_of_total']]
        return df

    def group_granularity(self):
        self.logger.info(f'aggregating for group granularity')
        df = self.data['companies'].groupby(['group']).size().reset_index(name='count')
        desc_gran = self.sic_desc[self.sic_desc['level headings'] == 'Group']
        desc_gran = desc_gran[['description', 'group']].rename(columns={'description': f'group_description'})
        df['group'] = self.format_string_key(df['group'])
        desc_gran['group'] = self.format_string_key(desc_gran['group'])
        df = df.merge(desc_gran, how='left', on='group').dropna()
        df['%_of_total'] = round((df['count'] / df['count'].sum()) * 100, 2)
        df = df[['group_description', 'group', 'count', '%_of_total']]
        return df

    def format_string_key(self, series):
        return [str(val).strip() for val in series]

    def sic_granularity(self):
        self.logger.info(f'aggregating for full sic granularity')
        df = self.data['companies'].groupby(['sic']).size().reset_index(name='count')
        desc_gran = self.sic_desc[self.sic_desc['level headings'] == 'Class']
        desc_gran = desc_gran[['description', 'sic']].rename(columns={'description': f'sic_description'})
        df['sic'] = self.format_string_key(df['sic'])
        desc_gran['sic'] = self.format_string_key(desc_gran['sic'])
        df = df.merge(desc_gran, how='left', on='sic').dropna()
        df['%_of_total'] = round((df['count'] / df['count'].sum()) * 100, 2)
        df = df[['sic_description', 'sic', 'count', '%_of_total']]
        return df

    def dfs_to_records_dict(self):
        self.logger.info(f'transforming all dfs to records dictionaries')
        for key, df in self.data.items():
            self.data.update({key: df.to_dict('records')})

if __name__ == '__main__':
    test = LoadPopulations()
    a=1
    a=1