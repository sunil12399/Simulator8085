class Hexadecimal8bitValueError(ValueError):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg = msg

    def __str__(self):
        return self.msg


class Hexadecimal16bitValueError(ValueError):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg = msg

    def __str__(self):
        return self.msg


class SyntaxErrorException(SyntaxError):
    def __init__(self,msg,lineno):
        super().__init__(msg)
        self.lineno = lineno

    def __str__(self):
        return self.msg


class LexicalException(SyntaxError):
    def __init__(self,msg):
        super().__init__(msg)

    def __str__(self):
        return self.msg


class RegisterError(ValueError):
    def __init__(self, msg=None):
        super().__init__(msg)
        self.msg = msg

    def __str__(self):
        return self.msg


class NotNoneError(ValueError):
    def __init__(self, msg=None):
        super().__init__(msg)
        self.msg = msg

    def __str__(self):
        return self.msg


class EndException(EOFError):
    def __init__(self, msg=None):
        self.msg = msg
        super().__init__(msg)

    def __str__(self):
        return self.msg