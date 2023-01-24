"""Logger class."""
import logging

class Logger:

    def __init__(self, name=None, level=None, fmt=None, directory=None):
        self.name = name
        self.level = level
        self.fmt = fmt
        self.directory = directory
        self.logger = None 
        self.file_handler = None

    def __str__(self) -> str:
        return f"Logger: {self.__dict__}"

    def get_logger(self, name=None):
        if name is None:
            self.name = name
        _logger = logging.getLogger(self.name)
        _logger.setLevel(self.level)
        if self.file_handler is None:
            self.create_file_handler()
        _logger.addHandler(self.file_handler)
        self.logger = _logger
        return self.logger

    def create_file_handler(self):
        _file_handler = logging.FileHandler(self.directory)
        _file_handler.setLevel(self.level)
        _file_handler.setFormatter(self.fmt)
        self.file_handler = _file_handler
        return self.file_handler

    def set_logger(self, logger):
        self.logger = logger
        return self.logger

    @staticmethod
    def new(name=None, level=None, fmt=None, directory=None):
        return Logger(name, level, fmt, directory)

    @staticmethod
    def new_logger(name=None, level=None, fmt=None, directory=None):
        logger = Logger.new(name, level, fmt, directory)
        return logger.get_logger()


    class Factory():
        @staticmethod
        def new(name=None, level=None, fmt=None, directory=None):
            logger = Logger.new(name, level, fmt, directory)
            return logger

        @staticmethod
        def create_file_handler(name=None, level=None, fmt=None, directory=None) -> logging.FileHandler:
            logger = Logger.new(name, level, fmt, directory)
            return logger.create_file_handler()


    factory = Factory()



