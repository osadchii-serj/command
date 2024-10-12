from gift_service import GiftService

from dataclasses import dataclass

from interface import Command


@dataclass
class SendGiftCommand(Command):

    service: GiftService
    gift: str

    def execute(self):
        self.service.send_gift(self.gift)
