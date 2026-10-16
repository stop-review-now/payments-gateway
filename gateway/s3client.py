import boto3

def client():
    """Return an S3 client for archival storage."""
    return boto3.client('s3')
