from constants import MIN_TEXT_LENGTH, MAX_TEXT_LENGTH


def check_text(text):
    return MIN_TEXT_LENGTH <= len(text) <= MAX_TEXT_LENGTH
