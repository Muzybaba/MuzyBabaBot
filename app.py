import logging
import pywhatkit
from whatsapp import send_whatsapp_message
from commands import handle_command

logging.basicConfig(filename='logs/bot_logs.txt', level=logging.INFO)

def handle_message(message):
    text = message.lower()
    if text.startswith('muzzy'):
        send_menu()
    else:
        handle_command(text)

def send_menu():
    menu = """
    MUZY BABA IceZone
    *MAIN MENU*
    Muzzy help - Display available commands
    Muzzy about - Information about MUZY BABA Bot
    Muzzy version - Bot version
    ...
    """
    send_whatsapp_message(menu)

def main():
    whatsapp = pywhatkit.whatsapp()
    while True:
        message = whatsapp.get_latest_message()
        handle_message(message)

if __name__ == '__main__':
    main()
