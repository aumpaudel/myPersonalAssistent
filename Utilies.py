import re
import random
from Dictionaries import RESPONSES, FILLER_WORDS, MUSIC_SYNONYMS, PLATFORM_CONNECTORS

def extract_number(text):
    """
    The function `extract_number` takes a text input and returns the first number found in the text as
    an integer, or None if no number is found.
    
    :param text: You have provided a function named `extract_number` that takes a text input as a
    parameter. The function attempts to extract a number from the input text using a regular expression.
    If a number is found in the text, it is converted to an integer and returned. If no number is found,
    the
    :return: The `extract_number` function is returning an integer value if a number is found in the
    input text, otherwise it returns None.
    """
    if not text:
        return None

    match = re.search(r'\d+', text)
    if match:
        return int(match.group())

    return None

def pick_response(key,humour_enabled=True):
    """
    The function `pick_response` selects a response based on a given key, with an option to include
    humorous responses if enabled.
    
    :param key: The `key` parameter in the `pick_response` function is used to specify the key for which
    a response is to be retrieved from the `RESPONSES` dictionary
    :param humour_enabled: The `humour_enabled` parameter is a boolean flag that determines whether the
    function should include humorous responses in its output. If set to `True`, the function will
    consider both neutral and humorous responses when selecting a response. If set to `False`, only
    neutral responses will be considered, defaults to True (optional)
    :return: The function `pick_response` returns a response based on the provided key. If
    `humour_enabled` is set to `True`, it will return a random response from the "neutral" and "humour"
    categories combined. If `humour_enabled` is set to `False` or not provided, it will return a random
    response from the "neutral" category only. If no responses are
    """
    responses = RESPONSES.get(key, {})
    if humour_enabled:
        return random.choice(
            responses.get("neutral", []) +
            responses.get("humour", [])
        )

    neutral = responses.get("neutral", [])
    return random.choice(neutral) if neutral else ""

def extract_music_name(command: str):
    """
    The `extract_music_name` function takes a command as input, removes filler words, music synonyms,
    and platform connectors from the text, and returns the cleaned text as the extracted music name.
    
    :param command: It looks like you have provided a function named `extract_music_name` that processes
    a command to extract the music name from it. The function removes filler words, music synonyms, and
    platform connectors from the command text to isolate the music name
    :type command: str
    :return: The function `extract_music_name` returns the extracted music name from the input `command`
    after removing filler words, music synonyms, and platform connectors. If no music name is extracted
    or the input is empty, it returns `None`.
    """
    if not command:
        return None

    text = command.lower()

    for group in FILLER_WORDS.values():
        for phrase in sorted(group, key=len, reverse=True):
            text = re.sub(re.escape(phrase), '', text)

    for group in MUSIC_SYNONYMS.values():
        for word in group:
            if word.isascii():
                text = re.sub(rf'\b{re.escape(word)}\b', '', text)
            else:
                text = text.replace(word, '')

    for word in PLATFORM_CONNECTORS:
        text = re.sub(rf'\b{re.escape(word)}\b', '', text)

    text = re.sub(r'\s+', ' ', text).strip()
    return text if text else None
