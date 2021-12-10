class ErrorDict:
    def __init__(self):
        self.dict = {}

    def add(self, key, value):
        self.dict[key] = value

    def remove(self, key):
        self.dict.pop(key)

    def get_error(self, key):
        return self.dict[key]

# object containing dictionary of possible errors
errors = ErrorDict()


errors.add("404", "This page does not exist")
errors.add("403", "You do not have a manager account")
errors.add("400", "You need an account to perform this action")
