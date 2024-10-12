from payment_service import PaymentService

from dataclasses import dataclass

from interface import Command


@dataclass
class TransferMoneyCommand(Command):

    service: PaymentService
    amount: int | float

    def execute(self):
        self.service.transfer_money(self.amount)
