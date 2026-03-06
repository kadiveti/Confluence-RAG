import boto3
from botocore.exceptions import ClientError
from cofig import config

class S3Storage:
    def __init__(self):
       self.s3 = boto3.client( 
           's3',
           aws_access_key_id=config.AWS_ACCESS_KEY_ID,
           aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
       )

       self.bucke = config.AWS_BUCKET_NAME

       def upload_file(self, file_obj,filename):
        try:
            self.s3.upload_fileobj(file_obj, self.bucket, filename)
            print(f"File {filename} uploaded successfully to bucket {self.bucket_name}.")
            return True
        except ClientError as e:
            print(f"Error uploading file: {e}")
            return False

        def get_file(self, filename):
            try:
                response = self.s3.get_object(Bucket=self.bucket, Key=filename)
                return response['Body']
            except ClientError as e:
                print(f"Error retrieving file: {e}")
                return None