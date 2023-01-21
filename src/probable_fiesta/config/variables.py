import os
from logging import INFO

class LoggerDef():
    """Default values for the logger config."""
    ROOT_DIR = str(os.path.dirname(os.path.abspath(__file__)).rsplit("/config")[0])
    LEVEL = INFO                        
    DIRECTORY = f'{ROOT_DIR}/logger'    
    FORMAT = 'simple'                   
    NAME = 'main_log'

class PackageDef():
    """Default values for the package config."""
    NAME = 'probable_fiesta'

class VariablesDef():
    """Default values for the variables config."""
    VERSION = '0.0.1'

class DotEnvDef():
    """Default values for the dotenv config."""
    # This has precedence over the PackageDefaults
    PACKAGE_NAME = 'probable_fiesta'
    # Add more variables here