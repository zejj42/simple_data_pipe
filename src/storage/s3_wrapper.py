import boto3
from boto3.exceptions import S3UploadFailedError
from datetime import datetime
import logging
import os
from .storage_service_wrapper import StorageServiceWrapper


class S3Wrapper(StorageServiceWrapper):
    def __init__(self, config):
        super().__init__(config)
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=self.config["access_key"],
            aws_secret_access_key=self.config["secret_key"],
        )

    def upload_file(self, file_path, bucket):
        try:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            object_name = f"{timestamp}_{os.path.basename(file_path)}"
            self.s3_client.upload_file(file_path, bucket, object_name)
            logging.info(f"File {file_path} uploaded to {bucket}/{object_name}")
        except S3UploadFailedError as e:
            logging.error(f"File upload failed: {e}")
            raise e
