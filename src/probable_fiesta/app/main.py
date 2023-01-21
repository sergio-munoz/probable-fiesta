""""Main module for probable_fiesta app."""
import sys

from ..logger.logging_config import get_logger
from ..__about__ import __package_name__
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
    print("Starting package main_app_builder:\n")

    # Create test app
    my_app_builder = MyAppBuilder()
    test_app = my_app_builder.name.set_name("test").build()
    print(f"Test app created: {test_app.name}")

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
    print(f"Main app created: {main_app.name}")
    print("MAIN_APP:", main_app)
    if main_app.error:
        print("MAIN_APP_ERROR:", main_app.error)
        return main_app.error
    main_app.run()
    history = main_app.context.command_queue.get_history()
    print("MAIN_APP_HISTORY:", history)
    print(f"Finished running main_app.")
    return history

# Get current name and version from config
def get_version() -> str:
    """Get package version.

    Returns:
        str: Current package version.
    """
    return f"{pd.NAME} v.{vd.VERSION}"


if __name__ == "__main__":
    # Note: sys.argv might have to be removed from here.
    # Depends on how pip installs the package.
    main(sys.argv[1:])