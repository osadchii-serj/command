from dataclasses import dataclass

from interface import Command


@dataclass
class RemoteControl:

    command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
