from ..v1 import MyArgumentParser

class Parser:
    def __init__(self, parser=None):
        if parser is not None:
            self.parser = parser
        else:
            self.parser = MyArgumentParser()

    def __str__(self):
        return f"Parser: {self.__dict__}"
    
    def create_parser(self, description=None):
        self.parser = MyArgumentParser(add_help=True, description=description)
        return self

    def add_argument(self, short_flag, long_flag=None, action=None, help=None):
        #self.parser.add_argument(short_flag, long_flag, action=action, help=help)

        self.parser.add_argument("--version", action='store_true', help=f"Current version")
        return self

    def parse_args(self, args=None):
        self.parser.parse_args(args)
        return self

    def get_parsed_args(self):
        return self.parser.get_parsed_args()

    @staticmethod
    def new_parser(parser=None):
        return Parser(parser)

    class Factory():
        @staticmethod
        def new_parser(parser=None):
            return Parser(parser)

    factory = Factory()