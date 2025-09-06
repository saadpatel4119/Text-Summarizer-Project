import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_files(self) -> bool:
        try:
            logger.info("Starting all files validation")
            status = True
            
            for file in self.config.ALL_REQUIREMENTS_FILE:
                file_path = os.path.join(self.config.root_dir, file)
                if not os.path.exists(file_path):
                    logger.info(f"File: {file} is not present")
                    status = False
            
            if status:
                logger.info("All files are present")
            else:
                logger.info("Some files are missing")
            
            with open(self.config.status_file, 'w') as f:
                f.write(str(status))
                
            logger.info("Completed all files validation")
            return status
        except Exception as e:
            raise e