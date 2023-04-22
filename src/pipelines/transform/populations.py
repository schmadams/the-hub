from src.helper_functions.helpers import load_sic_descs

class TreeMapDescriptions:
    def __init__(self):
        self.sic_desc = load_sic_descs()

    def add_section_description(self, data):
        desc_gran = self.sic_desc[self.sic_desc['level headings'] == 'SECTION']
        desc_gran = desc_gran[['description', 'section']].rename(columns={'description': f'section_description'})
        data_new = data.merge(desc_gran, how='left', on='section')
        data_new['section_description'] = [f'{x}-{y}' for x, y in
                                            zip(data_new['section'], data_new['section_description'])]
        return data_new

    def add_division_description(self, data):
        desc_gran = self.sic_desc[self.sic_desc['level headings'] == 'Division']
        desc_gran = desc_gran[['description', 'division']].rename(columns={'description': f'division_description'})
        data_new = data.merge(desc_gran, how='left', on='division')
        data_new['division_description'] = [f'{x}-{y}' for x,y in
                                            zip(data_new['division'], data_new['division_description'])]
        return data_new

    def add_group_description(self, data):
        desc_gran = self.sic_desc[self.sic_desc['level headings'] == 'Group']
        desc_gran = desc_gran[['description', 'group']].rename(columns={'description': f'group_description'})
        data['group'] = self.format_string_key(data['group'])
        desc_gran['group'] = self.format_string_key(desc_gran['group'])
        data_new = data.merge(desc_gran, how='left', on='group')
        data_new['group_description'] = [f'{x}-{y}' for x, y in
                                            zip(data_new['group'], data_new['group_description'])]
        return data_new

    def add_sic_description(self, data):
        desc_gran = self.sic_desc[self.sic_desc['level headings'] == 'Class']
        desc_gran = desc_gran[['description', 'sic']].rename(columns={'description': f'sic_description'})
        data['sic'] = self.format_string_key(data['sic'])
        desc_gran['sic'] = self.format_string_key(desc_gran['sic'])
        data_new = data.merge(desc_gran, how='left', on='sic')
        data_new['sic_description'] = [f'{x}-{y}' for x, y in
                                            zip(data_new['sic'], data_new['sic_description'])]
        return data_new

    def format_string_key(self, series):
        return [str(val).strip() for val in series]