class StorageServiceWrapper:
    def __init__(self, config):
        self.config = config

    def upload_file(self, file_name, bucket, object_name=None):
        raise NotImplementedError("Subclasses must implement this method")
