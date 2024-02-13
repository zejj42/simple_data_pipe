from .s3_wrapper import S3Wrapper


def get_storage_service(service_type, config):
    if service_type == "S3":
        return S3Wrapper(config)
    else:
        raise ValueError(f"Unsupported storage service type: {service_type}")
