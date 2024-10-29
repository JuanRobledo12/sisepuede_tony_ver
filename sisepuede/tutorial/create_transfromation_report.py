import os
import yaml
import pandas as pd

class CreateTransformationReport:
    
    def __init__(self, country_transformations_path):
        
        self.country_transformations_path = country_transformations_path

        # TODO: PFLO also belongs to energy, we need to fix this
        self.spp_sectors = {
             'AFOLU': ['AGRC', 'LVST', 'LNDU', 'LSMM', 'SOIL'],
             'CircularEconomy': ['WALI', 'WASO'],
             'Energy': ['TRNS', 'INEN', 'SCOE', 'TRDE', 'ENTC', 'FGTV', 'CCSQ'],
             'IPPU': ['IPPU', 'TRWW']
             'All Sectors': ['PFLO']
        }

    def get_yaml_names(self):
            file_names = os.listdir(self.country_transformations_path)
            yaml_file_names = [i for i in file_names if i.startswith('transformation')]
            return yaml_file_names
    
    def get_data_from_yaml(self, yaml_file_name):
         
         # Load the YAML file
        with open(os.path.join(self.country_transformations_path, yaml_file_name), 'r') as file:
            data = yaml.safe_load(file)

        # Extract the desired values
        description = data.get('description')
        transformation_code = data.get('identifiers', {}).get('transformation_code')
        transformation_name = data.get('identifiers', {}).get('transformation_name')
        magnitude = data.get('parameters', {}).get('magnitude')

        metadata_dict = {
             'transformation_code': transformation_code,
             'transformation_name': transformation_name,
             'description': description,
             'magnitude': magnitude
        }

        return metadata_dict

    def get_transformations_metadata(self):

        transformations_metadata = {}

        # get transformation yaml files
        yaml_file_names = self.get_yaml_names()
        # print(yaml_file_names)
        # print(len(yaml_file_names))

        for file_name in yaml_file_names:             
             # Create a dictionary key with the file name and the value will be a dict with metadata
             transformations_metadata[file_name] = self.get_data_from_yaml(file_name)
        # print(transformations_metadata)
        return transformations_metadata
        
         
    
    def generate_report(self):

        # get data from yaml files
        transformations_metadata = self.get_transformations_metadata()

        df = pd.DataFrame.from_dict(transformations_metadata, orient='index').reset_index(drop=True)

        # Eliminate the Default value prefix from the transformation_name column
        df['transformation_name'] = df['transformation_name'].str.replace(r'^Default Value - [A-Z]+: ', '', regex=True)
        
        # generate the subsector column
        df['subsector'] = df.transformation_code.apply(lambda x: x.split(':')[1])

        # generate the sector column

        # Create the reverse mapping dictionary
        subsector_to_sector = {subsector: sector for sector, subsectors in self.spp_sectors.items() for subsector in subsectors}

        # Map the 'subsectors' column to 'sectores' using the reverse mapping
        df['sectors'] = df['subsector'].map(subsector_to_sector)

        return df
