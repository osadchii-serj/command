from message_service import MessageService

from dataclasses import dataclass

from interface import Command


@dataclass
class SendMessageCommand(Command):

    service: MessageService
    message: str

    def execute(self):
        self.service.send_message(self.message)
