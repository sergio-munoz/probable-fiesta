# Obtain args from CLI
# Validate args
# Obtain env variables from module config
# Override env variables from CLI
# Create AppProcessManager
# Iterate through args

# Create precedence order for env variables
# Create precedence for args
import sys

from .builder.app import App

from ..config.main import main as config_main
from ..command.command_builder import CommandListFactory
from ..cli.v1 import create_argument_parser


class AppBuilder:  # facade
    def __init__(self, app=None):
        if app is None:
            self.app = App()
        else:
            self.app = app

    def __repr__(self):
        return f"AppBuilder: {self.app}"

    @property
    def args(self):
        return AppArgs(self.app)

    @property
    def variables(self):
        return AppVariables(self.app)

    @property
    def config(self):
        return AppConfig(self.app)
    
    @property
    def command(self):
        return AppCommand(self.app)

    @property
    def command_list(self):
        return AppCommandList(self.app)

    @property
    def command_list_builder(self):
        return AppCommandListBuilder(self.app)

    @property
    def command_queue(self):
        return AppCommandQueue(self.app)

    def build(self):
        return self.app

class AppArgs(AppBuilder):
    def __init__(self, app):
        super().__init__(app)

    def get_from_cli(self):
        args = sys.argv[1:]
        if len(args) <= 0:
            self.app.args = None
        else:
            self.app.args = args
        return self
    
    def validate_args(self, args=None):
        if self.app.args:
            args = self.app.argument_parser.parse_args(self.app.args)
        else:
            args = self.app.argument_parser.parse_args(args)

        if self.app.argument_parser.error_message:
            self.app.error = f"{self.app.argument_parser.error_message}"
        if not args:
            self.app.validated_args = None
        else:
            self.app.validated_args = args

        return self

    def get_from_args(self, args):
        self.app.args = args
        return self

    def add_argument_parser(self, parser):
        self.app.argument_parser = parser
        return self

    def validate_args(self, args=None):
        if self.app.args:
            args = self.app.argument_parser.parse_args(self.app.args)
        else:
            args = self.app.argument_parser.parse_args(args)

        if self.app.argument_parser.error_message:
            self.app.error = f"{self.app.argument_parser.error_message}"
        if not args:
            self.app.validated_args = None
        else:
            self.app.validated_args = args

        return self

    def get_args(self, args, argument_parser):
        self.get_from_cli()
        self.add_argument_parser(argument_parser)
        self.validate_args()
        return self

class AppConfig(AppBuilder):
    def __init__(self, app):
        super().__init__(app)

    def get_from_module_config(self):
        self.app.config = config_main()  # modify in config/main.py
        return self

class AppVariables(AppBuilder):
    def __init__(self, app):
        super().__init__(app)

    def get_from_module_config(self):
        self.app.variables = None
        return self

class AppCommand(AppBuilder):
    def __init__(self, app):
        super().__init__(app)

    def add_command_list_builder(self, command_list_builder):
        self.app.command = command_list_builder
        return self

    def run_command(self, command):
        return self.app.command.run(command)

class AppCommandListBuilder(AppBuilder):
    def __init__(self, app):
        super().__init__(app)

    def set_command_list_builder(self, command_list_builder):
        self.app.command_list_builder = command_list_builder
        return self

class AppCommandList(AppBuilder):
    def __init__(self, app):
        super().__init__(app)
    
    def set_command_list(self, command_list):
        self.app.command_list = command_list
        return self

    def add_command(self, command):
        self.app.command_list.append(command)
        return self

    def remove_command(self, command):
        self.app.command_list.remove(command)
        return self

    def clear_command_list(self):
        self.app.command_list = []
        return self

    def run_command_list(self):
        for command in self.app.command_list:
            self.app.command.invoke(command)
        return self

class AppCommandQueue(AppBuilder):
    def __init__(self, app):
        super().__init__(app)

    def add_command(self, command):
        self.app.command_queue.append(command)
        return self

    def add_new_command(self, name, function, args):
        self.app.command_queue.add_new_command(name, function, args)
        return self

    def remove_command(self, command):
        self.app.command_queue.remove(command)
        return self

    def clear_command_queue(self):
        self.app.command_queue = []
        return self

    def run_command_queue(self):
        for command in self.app.command_queue:
            self.app.command.invoke(command)
        return self

class AppFactory():
    @staticmethod
    def new_app_with_command_builder(args, command_list_builder, argument_parser=None):
        # Create argument parser
        if argument_parser is None:
            aP = create_argument_parser()
        else:
            aP = argument_parser

        aB = AppBuilder()
        app = aB\
            .args\
                .get_from_cli()\
                .add_argument_parser(aP)\
                .validate_args(args)\
            .config\
                .get_from_module_config()\
            .command_list_builder\
                .set_command_list_builder(command_list_builder)\
            .build()
        return app

    @staticmethod
    def new_app(args=None, command_list=None, argument_parser=None):
        # Create argument parser
        if argument_parser is None:
            aP = create_argument_parser()
        else:
            aP = argument_parser

        # create command list builder
        cLB = CommandListFactory().new_command_list_builder(command_list)
        print(cLB)
        print(f"created command_list_builder: {cLB.get()}")

        # Create app builder
        aB = AppBuilder()
        app = aB\
            .args\
                .get_from_cli()\
                .add_argument_parser(aP)\
                .validate_args(args)\
            .config\
                .get_from_module_config()\
            .command_list\
                .set_command_list(cLB)\
            .build()
        return app