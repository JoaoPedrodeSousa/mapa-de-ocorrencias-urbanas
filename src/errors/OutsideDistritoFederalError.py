class OutsideDistritoFederalError(Exception):
    def __init__(self, message: str = "Ponto marcado fora do Distrito Federal"):
        self.message = message
        super().__init__(message)