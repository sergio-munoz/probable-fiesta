from ..v1 import MyArgumentParser

class Parser:
    def __init__(self, parser=None, add_help=True, description=None):
        if parser is not None:
            self.parser = parser
        else:
            self.parser = MyArgumentParser(add_help=add_help, description=description)
        self.valid = False
        self.parsed_args = None
        self.error = None

    def __str__(self):
        return f"Parser: {self.__dict__}"

    def add_argument(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)
        return self

    def get_parsed_args(self):
        return self.parsed_args 

    def get_parsed_arg(self, arg):
        try:
            return self.parsed_args[arg]
        except KeyError:
            return None

    def validate(self, args=None):
        self.valid = True
        self.parsed_args = self.parser.parse_args(args)
        if self.parser.error_message:
            self.error = self.parser.error_message
            self.valid = False
        if not self.parsed_args:
            self.valid = False
        return self.valid

    @staticmethod
    def new_parser(parser=None, add_help=True, description=None):
        return Parser(parser, add_help, description)

    class Factory():
        @staticmethod
        def new(parser=None, add_help=True, description=None):
            return Parser.new_parser(parser, add_help, description)

    factory = Factory()