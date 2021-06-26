class ValidationHelper:
    def __init__(self, data, options):
        self.options = options
        self.data = data
        self.messages = {}
        self.is_valid = True

    def __del__(self):
        pass

    def valid(self):
        try:
            for key in self.options.keys():
                if self.options[key].get('required') and (key not in self.data or self.data.get(key) == ''):
                    self.messages[key] = "This field cannot be left blank"
                    self.is_valid = False

            return {
                'is_valid': self.is_valid,
                'messages': self.messages
            }
        except Exception as e:
            return e
