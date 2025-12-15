class AssistantState:
    def state_update(self, state: str):
        """
        The `state_manager` function sets specific boolean flags based on the input state string
        provided.
        
        :param state: The `state_manager` function you provided is a method that takes a `state`
        parameter of type `str`. The function sets boolean attributes (`idle`, `thinking`, `speaking`,
        `listening`) based on the value of the `state` parameter. If the `state` matches one of
        :type state: str
        """
        self.idle = False
        self.thinking = False
        self.speaking = False
        self.listening = False
        
        if state == "idle":
            self.idle = True
            self.state = "idle"
        elif state == "thinking":
            self.thinking = True
            self.state = "thinking"
        elif state == "speaking":
            self.speaking = True
            self.state = "speaking"
        elif state == "listening":
            self.listening = True
            self.state = "listening"
        else:
            raise ValueError(f"Invalid state: {state}. Must be 'idle', 'thinking', 'speaking', or 'listening'")
    
    def set_sleep_mode(self, value: bool):
        self.sleep_mode = value
        if value:
            self.state_update("idle")

    def __init__(self):
        """
        The function initializes various attributes for a coding assistant.
        """
        self.humour = True
        self.last_intent = None
        self.last_action = None
        self.last_value = None
        self.network = True
        self.sleep_mode = False
        self.state_update("idle")
        self.stop = False

a = AssistantState()