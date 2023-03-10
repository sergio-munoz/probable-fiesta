"""Command Queue class."""
from .command_factory import CommandFactory
from .command import Command

class CommandQueue():

    def __init__(self):
        self.queue = []
        self.history = []
        self.length = 0

    def add_command(self, command):
        if command is not None:
            self.queue.append(command)
            self.length += 1

    def add_new_command(self, name, function, *args):
        c = CommandFactory().new_command(name, function, *args)
        if c is not None:
            self.queue.append(c)
            self.length += 1

    def remove(self, command):
        removed = self.queue.remove(command)
        if removed:
            self.length -= 1

    def clear(self):
        self.queue = []
        self.length = 0

    def run_command(self, command):
        self.length -= 1
        self.history.append(command.invoke())
        return self

    def run_all(self):
        if self.length <= 0:
            print("No commands in queue")
            return None
        elif self.length == 1:
            self.run_command(self.queue.pop())
        else:
            for c in self.queue:
                self.run_command(c)
        return self
    
    def get_history(self):
        "Get history and clears it."
        if len(self.history) <= 0:
            print("No commands in history")
            return None
        elif len(self.history) == 1:
            return self.history.pop()
        else:
            temp = self.history
            self.history = []
            return temp

    def show(self):
        return self.queue

    def __str__(self):
        return f'CommandQueue: loaded commands: {self.length} executed commands: {self.history} '

    def print_queue(self):
        for c in self.queue:
            print(c)

    @staticmethod
    def new_empty():
        return CommandQueue()

    @staticmethod
    def new(queue):
        command_queue = CommandQueue()
        if queue is not None:
            if isinstance(queue, list):
                for command in queue:
                    if not isinstance(command, Command):
                        print("Invalid command type: %s", type(command))
                    else:
                        command_queue.add_command(command)
            elif isinstance(queue, CommandQueue):
                command_queue = queue
            elif isinstance(queue, Command):
                command_queue.add_command(queue)
            else:
                print("Invalid queue type: %s", type(queue))
        else:
            print("Creating empty queue: %s", queue)
        return command_queue

    class Factory():
        @staticmethod
        def new_command_queue(command_or_queue):
            return CommandQueue().new(command_or_queue)

    factory = Factory()