""""Main module for probable_fiesta app."""
import sys

from ..config.variables import PackageDef as pd
from ..config.variables import VariablesDef as vd
from ..app.builder.my_app_builder import MyAppBuilder
from ..app.builder.context_factory import ContextFactory
from ..command.builder.command_builder import CommandBuilder
from ..cli.v1 import create_argument_parser

def main(args=None):
    """Main function for probable_fiesta app.


    Args:
        args (list): List of arguments. Defaults to None.
    """
    # Get args from cli if not provided
    if not args:
        args = sys.argv[1:]

    # Create app builder
    my_app_builder = MyAppBuilder()

    # Create command queue for main_app
    command_builder = CommandBuilder()
    command = command_builder.queue\
        .add_new_command("version", get_version)\
        .build()

    # Create context for main_app for running commands
    context = ContextFactory.new_context(pd.NAME, command)

    # Create args parser
    parser = create_argument_parser()

    # Create main app
    main_app = my_app_builder\
        .name\
            .set_name(pd.NAME)\
        .context\
            .set_context(context)\
        .arguments\
            .validate_with_args_parse(parser, args)\
        .build()

    # Get errors
    if main_app.error:
        return main_app.error

    # Run main app
    main_app.run()

    # Get command execution history
    history = main_app.context.command_queue.get_history()
    print("Command history: ", history)

    # Return command execution history
    return history

# Get current name and version from config
def get_version() -> str:
    """Get package version.

    Returns:
        str: Current package version.
    """
    return f"{pd.NAME} v.{vd.VERSION}"


if __name__ == "__main__":
    main(sys.argv[1:])