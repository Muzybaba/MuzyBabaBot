import pywhatkit

def send_whatsapp_message(phone_number, message, hour, minute):
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

def get_latest_message():
    # Implement getting latest message from WhatsApp Web
