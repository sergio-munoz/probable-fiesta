class Config():
    def __init__(self):
        self.package = {}
        self.logger = {}
        self.variables = {}
        self.dotenv = None

    def __str__(self):
        return f"Config: {self.package}, {self.logger}, {self.variables}"

class ConfigBuilder():
    def __init__(self, config=None):
        if config is None:
            self.config = Config()
        else:
            self.config = config

    @property
    def package(self):
        return ConfigPackage(self.config)

    @property
    def logger(self):
        return ConfigLogger(self.config)

    @property
    def variables(self):
        return ConfigVariables(self.config)

    def build(self):
        return self.config

class ConfigPackage(ConfigBuilder):
    def __init__(self, config):
        super().__init__(config)

    def set_package_name(self, name):
        self.config.package['name'] = name
        return self

    def set_root_dir(self, directory):
        self.config.package['root_directory'] = directory
        return self

class ConfigLogger(ConfigBuilder):
    def __init__(self, config):
        super().__init__(config)

    def set_logger_level(self, level):
        self.config.logger['level'] = level
        return self

    def set_logger_dir(self, directory):
        self.config.logger['directory'] = directory
        return self

    def set_logger_format(self, log_format):
        self.config.logger['format'] = log_format
        return self

    def set_logger_name(self, name):
        self.config.logger['name'] = name
        return self

    def get_logger_level(self):
        return f"{self.config.logger['level']}".capitalize()


class ConfigVariables(ConfigBuilder):
    def __init__(self, config):
        super().__init__(config)

    def set_variable(self, name, value):
        self.config.variables[name] = value
        return self

    def set_variables(self, variables):
        self.config.variables.update(variables)
        return self

    def get_from_module_config(self):
        self.config.variables.update(self.config.variables.module_config)
        return self

class ConfigDotEnv(ConfigBuilder):
    def __init__(self, config):
        super().__init__(config)

    def get_from_dotenv(self):
        try:
            import dotenv
        except ImportError:
            print("Warning: dotenv package not installed.")
            dotenv = None
        if dotenv is not None:
            self.config.dotenv.update(dotenv.load_dotenv())
        return self