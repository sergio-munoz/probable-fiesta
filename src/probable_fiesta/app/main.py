""""Main module for probable_fiesta app."""
import sys

from ..config.variables import PackageDef as pd
from ..config.variables import VariablesDef as vd
from ..app.builder.app_builder import AppBuilder
from ..config.default_config import get_config
from ..app.builder.app_abstract_machine import AppMachine
from ..app.builder.context_factory import ContextFactory

def use_app_machine(args=None):
    print("using app machine")
    app_machine = AppMachine()
    my_app = app_machine.prepare_default_app()
    print(f"\n->Running sample app: {my_app}")
    #my_app.run()
    #history = my_app.context.command_queue.get_history()
    #print(history)


def main(args=None):
    """Main function for probable_fiesta app.


    Args:
        args (list): List of arguments. Defaults to None.
    """
    # Get args from cli if not provided
    if not args:
        args = sys.argv[1:]

    default_config = get_config(log_name="probable_fiesta")

    aB = AppBuilder()
    # [oui_la_la], ["oui la la"]
    clean_args, clean_argv = aB.arguments.clean_arg_function(args)
    if len(clean_argv) == 0:
        clean_argv.append(None)


    aB = AppBuilder()
    main_app = aB\
        .name\
            .set_name("main_app")\
        .arguments\
            .set_arguments(args)\
        .args_parser\
            .add_argument("--test-app", type=str, help="test app builder")\
            .add_argument("--version", action='store_true', help="show version builder")\
            .add_argument("--repeat", type=str, help="repeat input")\
        .context\
            .add_context(ContextFactory.new_context_one_new_command(
                "test_app","test_app_func", lambda x: x, "repeated"))\
            .add_context(ContextFactory.new_context_one_new_command(
                "version", "version", get_version, None))\
            .add_context(ContextFactory.new_context_one_new_command(
                "repeat", "repeat", repeat, clean_argv[0]))\
        .config\
            .set_config(default_config)\
        .validate()\
        .build()
    #print(main_app)

    #use_app_machine()

    # Get parser error
    if main_app.args_parser.error:
        return main_app.args_parser.error

    # Run main app
    #print(f"\n->Running main app: {main_app}")
    #print("WILL RUN COMMANDS:", main_app.cleaned_args)
    for command in main_app.cleaned_args:
        main_app.run(command)

    # Get command execution history new
    history_new = main_app.get_run_history()
    print(history_new)

    # Return command execution history
    return history_new

# Get current name and version from config
def get_version() -> str:
    """Get package version.

    Returns:
        str: Current package version.
    """
    return f"{pd.NAME} v.{vd.VERSION}"

def repeat(x):
    return(f"Repeating: {x}")

if __name__ == "__main__":
    main(sys.argv[1:])