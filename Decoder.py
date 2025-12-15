from Dictionaries import INTENTS, ACTIONS
from Utilies import extract_number
def detect_key(command, dictionary):
    """
    The `detect_key` function searches for specific words in a command and returns the corresponding key
    from a dictionary if found.
    
    :param command: The `command` parameter is a string representing a command or input that you want to
    analyze for specific keywords
    :param dictionary: The `dictionary` parameter in the `detect_key` function is expected to be a
    Python dictionary where the keys are identifiers and the values are lists of words associated with
    those identifiers. The function iterates over the dictionary to check if any of the words associated
    with each key are present in the `command
    :return: The function `detect_key` returns the key from the dictionary that contains a word present
    in the given command. If no match is found, it returns `None`.
    """
    for key, words in dictionary.items():
        for w in words:
            if w in command:
                return key
    return None

def decode_intent(command):
    command = command.lower()
    intent = detect_key(command, INTENTS)
    return intent
def decode_action(command):
    command = command.lower()
    action = detect_key(command, ACTIONS)
    return action
def decode(command):
    command = command.lower()
    value = extract_number(command)
    action = detect_key(command, ACTIONS)
    intent = detect_key(command, INTENTS)
    return intent, action, value