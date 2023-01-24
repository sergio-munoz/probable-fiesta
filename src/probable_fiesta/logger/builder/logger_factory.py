from .logger import Logger

class LoggerFactory:
    @staticmethod
    def new_logger(name=None, level=None, fmt=None, directory=None):
        return Logger.new(name, level, fmt, directory)

    def new_logger_flask(app, name, level, fmt, directory):
        file_handler = Logger.Factory.create_file_handler(name, level, fmt, directory)
        app.logger.addHandler(file_handler)
        return app.logger