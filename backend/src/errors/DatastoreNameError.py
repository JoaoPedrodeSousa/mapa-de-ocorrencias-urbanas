class DatastoreNameError(Exception):
    def __init__(self, message: str = "Existe um datastore com esse nome"):
        self.message = message
        super().__init__(message)