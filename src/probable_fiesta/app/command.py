from abc import ABC
from enum import Enum

class Command(ABC):
    def __init__(self):
        self.commands = []

    def invoke(self):
        pass

    def undo(self):
        pass

    def __repr__(self):
        return f"Command: {self.__dict__}"

class CommandList(Command):
    def __init__(self, commands=None):
        super().__init__()
        if commands is not None:
            self.commands = commands

    def invoke(self):
        for command in self.commands:
            command.invoke()

    def undo(self):
        for command in self.commands:
            command.undo()

class RunCommand(Command):
    def __init__(self, function, args=None):
        self.function = function
        self.args = args

    def invoke(self):
        self.function(*self.args)

    def undo(self):
        pass

class CommandBuilder():
    def __init__(self, command=None):
        if command is None:
            self.command = Command()
        else:
            self.command = command

    def __repr__(self):
        return f"CommandBuilder: {self.command}"

    @property
    def commands(self):
        return CommandMaker(self.command)

    def build(self):
        return self.command

class CommandMaker(CommandBuilder):
    def __init__(self, command):
        super().__init__(command)

    def add(self, command):
        self.command.commands.append(command)
        return self

    def invoke_one(self, command):
        command.invoke()
        return self        

    def invoke(self):
        for command in self.command.commands:
            command.invoke()

    def undo(self):
        for command in self.command.commands:
            command.undo()

if __name__ == "__main__":

    def test_function(*args):
        cmd = RunCommand(test_function, args)
        cmd.invoke()
        print("test_function invoked", cmd)


    test_function("ls", "-la")