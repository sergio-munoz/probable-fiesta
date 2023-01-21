from .builder.command import Command

class CommandBuilder:

    def __init__(self):
        self.command = Command()
        self.command.command_list = list()

    def __repr__(self):
        return f"CommandBuilder: {self.command}"

    def add_command(self, name, function, args):
        self.command.name = name
        self.command.function = function
        self.command.args = args
        return self

    def set_command_list(self, command_list):
        self.command.command_list = command_list
        return self

    def build(self):
        return self.command

class CommandListBuilder(CommandBuilder):

    def set_command_list(self, command_list):
        self.command.command_list = command_list
        return self

    def get(self):
        return self.command.command_list

    def add(self, command):
        if not command:
            print("No command to add")
            return self
        self.command.command_list.append(command)
        return self
    
    def add_all(self):
        for command in self.command.command_list:
            self.add(command)
        return self

    def remove(self, command):
        self.command.command_list.remove(command)
        return self

    def clear(self):
        self.command.command_list = []
        return self

    def invoke(self):
        if isinstance(self.command , list):
            for command in self.command.command_list:
                command.invoke()
        self.command.invoke()

    def undo(self):
        for command in self.command.command_list:
            command.undo()

    def __iter__(self):
        return iter(self.command)
        #return iter(self.command.command_list)

    def __repr__(self):
        return f"command_list: {self.command.command_list}"

    def run_command(self, command):
        return command.invoke()

class CommandListRunner(CommandListBuilder):

    def add_command(self, command):
        self.command.command_list.add(command)
        return self
    
    def set_command_list(self, command_list):
        self.command.command_list = command_list
        return self

    @staticmethod
    def run_command(command):
        return command.invoke()
    
    def run_command_list(self):
        stdout = []
        for command in self.command.command_list:
            stdout.append(command.invoke())
        return stdout

class CommandBuilderFactory():
    @staticmethod
    def new_command(name, function, args=None) -> CommandBuilder:
        cB = CommandBuilder()
        cB.add_command(name, function, args)
        cB.build()
        return cB

class CommandListFactory():
    @staticmethod
    def new_command_list_builder(commandList) -> CommandBuilder:
        command_builder = CommandListBuilder()
        command_builder.set_command_list(commandList) 
        command_builder.build()
        return command_builder

    @staticmethod
    def new_command_list(command_list) -> CommandListBuilder:
        cLB = CommandListBuilder()
        if command_list is not None:
            if isinstance(command_list, list):
                for command in command_list:
                    if not isinstance(command, Command):
                        raise TypeError(f"Expected type Command, got {type(command)}")
                    else:
                        cLB.add(command)
                        print(f"appended from list: {command}")
            # not a list
            elif isinstance(command_list, CommandListBuilder):
                cLB = command_list
            elif isinstance(command_list, Command):
                cB = CommandFactory.new_command(command_list.name, command_list.function, command_list.args)
                if not isinstance(cB, CommandBuilder):
                    raise TypeError(f"Could not convert to type BuilderCommand, got {type(cB)}")
                cLB.add(cB.command)
            else:
                cLB.add(command_list)
                print(f"appended from not list: {command_list}")
        cLB.build()
        return cLB