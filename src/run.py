from transfer_money_command import TransferMoneyCommand
from send_message_command import SendMessageCommand
from send_gift_command import SendGiftCommand

from message_service import MessageService
from payment_service import PaymentService
from gift_service import GiftService

from remote_control import RemoteControl


if __name__ == "__main__":

    gift_service = GiftService()
    message_service = MessageService()
    payment_service = PaymentService()

    remote = RemoteControl()

    # Отправка подарка
    send_gift = SendGiftCommand(gift_service, "Цветы")
    remote.set_command(send_gift)
    remote.press_button()

    # Отправка сообщения
    send_message = SendMessageCommand(message_service, "С Днём влюблённых!")
    remote.set_command(send_message)
    remote.press_button()

    # Перевод денег
    transfer_money = TransferMoneyCommand(payment_service, 10000)
    remote.set_command(transfer_money)
    remote.press_button()
