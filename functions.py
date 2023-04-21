from constants import MIN_TEXT_LENGTH, MAX_TEXT_LENGTH


def check_text(text):
    """Checks if text match requirements"""
    return (MIN_TEXT_LENGTH <= len(text) <= MAX_TEXT_LENGTH) and ("\n" not in text)
