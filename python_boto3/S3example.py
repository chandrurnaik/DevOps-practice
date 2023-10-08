import boto3

AWS_REGION = "us-west-2"
AWS_ACCESS_KEY_ID = "AKIAZNTAAFYOEJC4VV5Y"
AWS_SECRET_KEY = "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"

aws_session = boto3.Session(region_name=AWS_REGION, 
                            aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY)
s3_resource = aws_session.resource('s3')
s3_client = aws_session.client('s3')


def createS3Bucket(name):
    response = s3_client.create_bucket(
        Bucket=name,
        CreateBucketConfiguration={
            'LocationConstraint' : 'us-west-2'
        }
    )
    print(response)

# createS3Bucket("bucket-may-2023")
# createS3Bucket("bucket-jun-223")
# createS3Bucket("bucket-jul-223") 

def uploadFileToBucket(file_name, bucket, object_name):
    response = s3_client.upload_file(file_name, bucket, object_name)
    print(response)
# uploadFileToBucket('./file1.jpg', 'bucket-may-2023', 'file01.jpg')
# uploadFileToBucket('./file2.jpg', 'bucket-may-2023', 'file02.jpg') 

def deleteObjectsBucket(bucket_name, key_name):
    response = s3_client.delete_object(Bucket=bucket_name, Key=key_name)
    print(response)
# deleteObjectsBucket("bucket-may-2023", "file02.jpg")
# deleteObjectsBucket("bucket-may-2023", "file01.jpg") 

def deleteS3Bucket(bucket_name):
    response = s3_client.delete_bucket(Bucket=bucket_name)
    print(response)
# deleteS3Bucket("bucket-may-2023")
# deleteS3Bucket("bucket-jun-223")
# deleteS3Bucket("bucket-jul-223")