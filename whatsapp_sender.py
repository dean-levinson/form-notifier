import pywhatkit

SPECIALIST_TO_PHONE_NUMBER = {
    "DR. Dean": "+972546449501",
    "DR. Barak": "+972587505557"
}

# move it to consts.py
FORM_URL = "ThisSupposeToBeURL.com"

def send_form_to_specialist(intern, specialist):
    specialist_phone_number = SPECIALIST_TO_PHONE_NUMBER[specialist]
    pywhatkit.sendwhatmsg_instantly(specialist_phone_number,
     f'Hey how are you! I\'m python.\nIntern {intern} has filled a form.\nPlease fill this form about him - {FORM_URL}')