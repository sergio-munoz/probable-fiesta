from abc import ABC
from enum import Enum, auto
#from .my_app_builder import MyAppBuilder
#from ...command.builder.command_builder import CommandBuilder
#from .context_factory import ContextFactory
#from ...config.default_config import get_config
#from ...config.
#from ...cli.builder.args_parser_factory import ArgsParserFactory

from .logger_factory import LoggerFactory

class AbstractLogger(ABC):
    def get(self):
        pass

class LoggerDefault(AbstractLogger):
    def get(self):
        print("Getting default logger")

class LoggerFlask(AbstractLogger):
    def get(self):
        print("Getting flask logger")

class LoggerAbstractFactory(ABC):
    def create_logger(self, name, level, fmt, directory):
        pass

    def get(self):
        pass

class LoggerDefaultFactory(LoggerAbstractFactory):
    def create_logger(self, name, level, fmt, directory):
        print("Creating default logger")
        logger = LoggerFactory().new_logger(name, level, fmt, directory)
        return logger

    def get(self):
        print("Getting default logger")
        return LoggerDefault()

class LoggerFlaskFactory(LoggerAbstractFactory):
    def create_logger(self, name, level, fmt, directory):
        print("Creating flask logger")
        logger = LoggerFactory().new_logger(name, level, fmt, directory)
        return logger

    def get(self):
        print("Getting flask logger")
        return LoggerFlask()

class MyappFactory(AppFactory):
    def create_app(self, name, context, args_parse, args, config):
        print("Creating my app")
        my_app_builder = MyAppBuilder()
        my_app = my_app_builder\
            .name\
                .set_name(name)\
            .context\
                .set_context(context)\
            .arguments\
                .validate_with_args_parse(args_parse, args)\
            .config\
                .set_config(config)\
            .build()
        return my_app

    def prepare(self):
        print("Preparing my app")
        return MyApp

    def prepare_default(self):
        print("Preparing default my app sample")
        args = ["--test"]
        function = lambda x: (x)

    def create_app(self, name, context, args_parse, args, config):
        print("Creating metrics app")
        my_app_builder = MyAppBuilder()
        my_app = my_app_builder\
            .name\
                .set_name(name)\
            .context\
                .set_context(context)\
            .args_parse\
                .set_args_parse(args_parse)\
            .arguments\
                .set_arguments(args)\
            .config\
                .set_config(config)\
            .build()
        return my_app

    def prepare(self):
        msg = "Preparing metrics app"
        print(msg)
        return msg

class AppMachine:
    class AvailableApps(Enum):
        MYAPP = auto()
        METRICSAPP = auto()
    
    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableApps:
                name = d.name[0] +  d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def __str__(self):
        return f"AppMachine: Available apps: {self.factories}"

    def prepare_app(self):
        print("Available apps:")
        for f in self.factories:
            print(f[0])
        s = input(f'Please pick app (0-{len(self.factories)-1}):')
        idx = int(s)
        # specify app name
        return self.factories[idx][1].prepare()

    def prepare_default_app(self):
        return self.factories[0][1].prepare_default()

def prepare_app(type):
    if type == 'my_app':
        return MyappFactory().prepare()
    elif type == 'metrics_app':
        return MetricsappFactory.prepare()
    else:
        print("Invalid app type")
        return None

def prepare_default_app(type):
    if type == 'my_app':
        return MyappFactory().prepare_default()
    else:
        print("Only my_app is supported")
        return None

def flow():
    pass
    # specify app name
    # specify app context
    ## specify app context command_queue
    # specify app args
    # specify app args_parse
    # specify app config