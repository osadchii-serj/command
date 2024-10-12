# Команда

>Реализация паттерна - "Команда" - учебный репозиторий.


![Image alt](https://github.com/osadchii-serj/command/raw/main/svg/pattern_command.svg)

***

Проект "День влюблённых" представляет собой интерактивное приложение, созданное для организации и празднования Дня Святого Валентина. Основная цель проекта — помочь пользователям выразить свои чувства и сделать этот день особенным для своих близких.
Краткое описание проекта
Цель:
Создание платформы для отправки подарков, поздравлений, открыток и цветов, а также возможности перевода денег и планирования романтических мероприятий. Функциональные возможности:

    Отправка подарков: Пользователи могут выбирать и отправлять подарки (цветы, шоколад и т.д.) через приложение.
    Поздравления: Возможность отправлять текстовые или голосовые поздравления.
    Открытки: Создание и отправка виртуальных открыток с персональными сообщениями.
    Перевод денег: Интеграция с сервисами денежных переводов для отправки средств партнёру.

Технология:
Приложение использует паттерн проектирования "Команда", что позволяет инкапсулировать каждое действие (например, отправка подарка или поздравления) в отдельный объект команды. Это упрощает управление действиями пользователя и позволяет легко добавлять новые функции.

***

### Классы

    Command (Команда): Абстрактный класс для определения интерфейса команды.
        execute(): Метод для выполнения команды.

    GiftService (Сервис подарков): Приемник, отвечающий за отправку подарков.
        send_gift(gift): Метод для отправки выбранного подарка.

    MessageService (Сервис сообщений): Приемник для отправки поздравлений и сообщений.
        send_message(message): Метод для отправки сообщения.

    PaymentService (Сервис платежей): Приемник для осуществления денежных переводов.
        transfer_money(amount): Метод для перевода указанной суммы.

    SendGiftCommand (Команда отправки подарка): Конкретная команда для отправки подарка.
        execute(): Выполняет действие по отправке подарка.

    SendMessageCommand (Команда отправки сообщения): Конкретная команда для отправки поздравления.
        execute(): Выполняет действие по отправке сообщения.

    TransferMoneyCommand (Команда перевода денег): Конкретная команда для перевода денег.
        execute(): Выполняет действие по переводу средств.

    RemoteControl (Вызывающий объект): Управляет выполнением команд.
        set_command(command): Устанавливает текущую команду.
        press_button(): Вызывает выполнение текущей команды.

### Методы

    Основные методы классов команд:
        execute(): Основной метод, который будет реализован в каждой конкретной команде для выполнения соответствующего действия.
    Методы сервисов:
        send_gift(gift): Отправляет выбранный подарок.
        send_message(message): Отправляет текст или голосовое сообщение.
        transfer_money(amount): Переводит указанную сумму на счёт партнёра.
