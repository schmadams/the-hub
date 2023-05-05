import yaml
from pathlib import Path
import pandas as pd
import numpy as np
from logging_functions.class_logging import Logger

def load_config():
    for file in Path(__file__).parent.parent.glob('*'):
        if str(file).endswith('yaml'):
            with open(str(file), "r") as stream:
                return yaml.safe_load(stream)


def load_sic_descs():
    xlsx_path = load_config()['sic_hieracrhy']
    sic_descs = pd.read_excel(xlsx_path, sheet_name='reworked structure')
    for col in sic_descs.columns:
        sic_descs = sic_descs.rename(columns={col: col.lower().strip()})
    return sic_descs.rename(columns={'most disaggregated level': 'sic'})

def join_sic_descs(df, key='sic'):
    sic_desc = load_sic_descs()
    df = df.merge(sic_desc, how='left', on=key)
    return df.drop(columns=['class', 'sub class', 'level headings'])

def header_strings(string):
    return string.lower().strip().replace('_', ' ').title()

def data_table_content(data):
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)
    columns = [{'name': header_strings((col)), 'id': col} for col in data.columns]
    return data.to_dict('records'), columns

def load_nav_logo():
    for file in Path(__file__).parent.parent.parent.glob('*'):
        if str(file).endswith('resources'):
            for resource in file.glob('*'):
                if str(resource).endswith('logo.png'):
                    logo_file = resource
    return str(logo_file)

def load_custom_css():
    for file in Path(__file__).parent.parent.parent.glob('*'):
        if str(file).endswith('resources'):
            for resource in file.glob('*'):
                if str(resource).endswith('.css'):
                    customcss = resource
    return str(customcss)

if __name__ == '__main__':
    sic_desc = load_sic_descs()
    a=1
    a=1