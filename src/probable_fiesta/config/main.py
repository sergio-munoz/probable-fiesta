from .config_builder import ConfigBuilder
from .variables import PackageDefaults,LoggerDefaults

config = None

def main():
    cB = ConfigBuilder()
    config = cB\
        .package\
            .set_package_name(PackageDefaults.NAME)\
        .logger\
            .set_logger_level(LoggerDefaults.LEVEL)\
            .set_logger_dir(LoggerDefaults.DIRECTORY)\
            .set_logger_format(LoggerDefaults.FORMAT)\
            .set_logger_name(LoggerDefaults.NAME)\
        .variables\
            .set_variable('VERSION', '0.0.1')\
        .build()
    
    print("config: ", config)  #log this
    return config

if __name__ == "__main__":
    main()