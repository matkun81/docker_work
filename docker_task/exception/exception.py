class TerminalCommandException(Exception):
    def __init__(self, text_exception):
        self.text = text_exception
