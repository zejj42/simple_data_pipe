class DatabaseWrapper:
    def __init__(self, config):
        self.config = config

    def connect(self):
        raise NotImplementedError("Subclasses must implement this method")

    def fetch_data(self, query):
        raise NotImplementedError("Subclasses must implement this method")

    def get_all_orders(self):
        raise NotImplementedError("Subclasses must implement this method")
