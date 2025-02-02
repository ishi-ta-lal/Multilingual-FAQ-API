from googletrans import Translator


def translate_text(text, dest_lang):
    """Translate text to a specified language using Google Translate API."""
    if not text:
        return None  # If no text, return None

    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        print(f"Translation Error: {e}")
        return text  # Return original text in case of an error
