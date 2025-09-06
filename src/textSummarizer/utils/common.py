import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
import unittest
if not hasattr(unittest.TestCase, "assertRaisesRegexp"):
    unittest.TestCase.assertRaisesRegexp = unittest.TestCase.assertRaisesRegex
from ensure import ensure_annotations   
from box import Box, ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"YAML file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
        
    Returns:
        None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def get_size(file_path: Path) -> str:
    """
    Returns the size of a file in bytes.
    
    Args:
        file_path (Path): Path to the file.
        
    Returns:
        int: Size of the file in bytes.
    """
    size_in_kb = round(os.path.getsize(file_path) / 1024, 2)
    return f"{size_in_kb} KB"