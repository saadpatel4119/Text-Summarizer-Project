from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from pathlib import Path
from textSummarizer.entity import (DataIngestionConfig,DataValidationConfig)

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([Path(self.config.artifacts_root)])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([Path(config.root_dir)])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source_URL = config.source_URL,
            local_data_file = Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )
        
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        
        create_directories([Path(config.root_dir)])
        
        data_validation_config = DataValidationConfig(
            root_dir = Path(config.root_dir),
            status_file = config.status_file,
            ALL_REQUIREMENTS_FILE = config.ALL_REQUIREMENTS_FILE
        )
        
        return data_validation_config